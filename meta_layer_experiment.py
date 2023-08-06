import json
import os
from datetime import datetime
from prompt_generator import PromptGeneratorGenerator
from tqdm import tqdm
import itertools
import openai
from tenacity import retry, stop_after_attempt, wait_exponential

class MetaLayerExperiment:
    def __init__(self, experiment, iterations=3, generations=3):
        self.name = experiment.name
        self.seed = experiment.seed
        self.tests = experiment.tests
        self.ranking = experiment.ranking
        self.model = experiment.model
        self.prompt_generators = []
        self.prompts = []
        self.iterations = iterations
        self.generations = generations
        self.winning_prompt_generator = None
        self.winning_prompt = None

    def expected_score(self, r1, r2):
        return 1 / (1 + 10**((r2 - r1) / 400))

    def update_elo(self, r1, r2, score1):
        e1 = self.expected_score(r1, r2)
        e2 = self.expected_score(r2, r1)
        return r1 + 32 * (score1 - e1), r2 + 32 * ((1 - score1) - e2)

    # Get Score - retry up to N_RETRIES times, waiting exponentially between retries.
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=70))
    def get_score(self, test_case, pos1, pos2, ranking_model_name, ranking_model_temperature):    
        score = openai.ChatCompletion.create(
            model=ranking_model_name,
            messages=[
                {"role": "system", "content": self.ranking},
                {"role": "user", "content": f"""Task:
                Brief: {test_case}
                Generation A: {pos1}
                Generation B: {pos2}"""}
            ],
            logit_bias={
                '32': 100,  # 'A' token
                '33': 100,  # 'B' token
            },
            max_tokens=1,
            temperature=ranking_model_temperature,
        ).choices[0].message.content
        return score

    def test_candidate_prompts(self, prompts, test_cases):
        print("Testing candidate prompts...")
        # Initialize each prompt with an ELO rating of 1200
        prompt_ratings = {i: 1200 for i in range(len(prompts))}
        # Calculate total rounds for progress bar
        total_rounds = len(test_cases) * len(prompts) * (len(prompts) - 1) // 2
        # Initialize progress bar
        pbar = tqdm(total=total_rounds, ncols=70)
        # For each pair of prompts
        for prompt1, prompt2 in itertools.combinations(prompts, 2):
            # For each test case
            for i in len(test_cases):
                # Update progress bar
                pbar.update()
                # Lookup output for each test case
                generation1 = prompt1.get_generation(i)
                generation2 = prompt2.get_generation(i)
                # Rank the outputs
                score1 = self.get_score(test_cases[i], generation1, generation2, self.model.name, self.model.ranking_temperature)
                score2 = self.get_score(test_cases[i], generation2, generation1, self.model.name, self.model.ranking_temperature)
                # Convert scores to numeric values
                score1 = 1 if score1 == 'A' else 0 if score1 == 'B' else 0.5
                score2 = 1 if score2 == 'B' else 0 if score2 == 'A' else 0.5
                # Average the scores
                score = (score1 + score2) / 2
                # Update ELO ratings
                r1, r2 = prompt_ratings[prompt1[-1]], prompt_ratings[prompt2[-1]]
                r1, r2 = self.update_elo(r1, r2, score)
                prompt_ratings[prompt1[-1]], prompt_ratings[prompt2[-1]] = r1, r2
                # Print the winner of this round
                if score > 0.5:
                    print(f"Winner: Prompt {prompt1[-1]}")
                    print(f"Score: {prompt_ratings[prompt1[-1]]}")
                elif score < 0.5:
                    print(f"Winner: Prompt {prompt2[-1]}")
                    print(f"Score: {prompt_ratings[prompt2[-1]]}")
                else:
                    print("Draw")

                with open("results.txt", 'w') as file:
                    file.write("Prompt Ratings (Ranked):\n")
                    ranked_ratings = sorted(prompt_ratings.items(), key=lambda item: item[1], reverse=True)
                    for rank, (prompt, rating) in enumerate(ranked_ratings, start=1):
                        file.write(f"(Rank: {rank}) Rating ({rating}): {prompt} \n")
                    file.write("\n")
        # Close progress bar
        pbar.close()
        print("Candidate prompts tested successfully.")
        return prompt_ratings

    def prompt_generator_search(self):
        # Run the experiment for i number of iterations
        for i in range(len(self.iterations)):
            # Generate prompt generators
            pgg = PromptGeneratorGenerator(self)
            self.prompt_generators = pgg.generate()
            
            # seed the past winning prompt generators into the end of self.prompt_generators list
            # ppg.seed()

            # Generate prompts from each generator
            for i in range(len(self.prompt_generators)):
                pg = self.prompt_generators[i]
                prompt = pg.generate()
                # Save each prompt set in same index of the prompt generator that generated the prompts.
                self.prompts.append(prompt)

            # Generate Outputs from each Prompt
            for i in range(len(self.prompts)):
                prompt_set = self.prompts[i]
                for prompt in range(len(prompt_set)):
                    # output data is saved within the prompt object itself
                    prompt.generate()

            # Rank Outputs Generated with Ranking Prompt
            self.test_candidate_prompts(self.prompts, self.tests)

            # record winning prompt generator and record winning prompts

        # return the last winning prompt generator
        pass

    def prompt_search(self):
         # Run the experiment for i number of iterations
        for i in range(len(self.iterations)):
            # Generate prompts with winning prompt generator
            pg = self.winning_prompt_generator
            prompt = pg.generate()
            # all prompts in index 0
            self.prompts = prompt
            
            # seed the past winning prompts into the end of self.prompts list
            # pg.seed()

            # Generate Outputs from each Prompt
            for i in range(len(self.prompts)):
                prompt_set = self.prompts[i]
                for prompt in range(len(prompt_set)):
                    # output data is saved within the prompt object itself
                    prompt.generate()

            # Rank Outputs Generated with Ranking Prompt
            self.test_candidate_prompts(self.prompts, self.tests)

            # record winning prompt 

    def save_experiment_results(self):
        experiment_folder = os.path.join("experiments", self.name)
        if not os.path.exists(experiment_folder):
            os.makedirs(experiment_folder)

        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(experiment_folder, f"{self.name}_{now}_results.json")
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    def run(self):
        self.prompt_generator_search(self)
        self.prompt_search(self)
        self.save_experiment_results(self)