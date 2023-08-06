import json
import os
from model import Model
import openai
        
class Prompt:
    def __init__(self):
        pass

    def seed_generations(test_cases, prompts):
        print("Seeding generations...")
        generations = {}
        test = 1
        print("Test cases: " + str(len(test_cases)))
        for test_case in test_cases:
            print("Generating for test case " + str(test))
            generations[test_case["test"]] = {}
            for prompt in prompts:
                generation = revise_content(prompt[0], prompt[1], prompt[-1], test_case)
                generations[test_case["test"]][prompt[-1]] = generation
            test += 1
        print("Generations ready to test.")
        return generations

class PromptGenerator:
    def __init__(self, system, human):
        self.prompts = []
        
    def generate_candidate_prompts(test_cases, number_of_prompts):
        print("Generating " + str(NUMBER_OF_PROMPTS) + " candidate prompts.")
        outputs = openai.ChatCompletion.create(
            model=CANDIDATE_MODEL, # change this to gpt-3.5-turbo if you don't have GPT-4 access
            messages=[
                {"role": "system", "content": system_gen_system_prompt},
                {"role": "user", "content": f"Here are some sample inputs:`{test_cases}`\n\nRespond with your system prompt and human prompt dilineated by /// and nothing else. Be creative."}
                ],
            temperature=CANDIDATE_MODEL_TEMPERATURE,
            n=number_of_prompts)

        seeds = seed_candidate_prompts()

        prompts = []

        for i in outputs.choices:
            prompts.append(i.message.content.split("///"))

        print("Seeding " + str(len(seeds)) + " promising candidate prompts.")
        for i in seeds:
            prompts.append(i)

        for i in range(len(prompts)):
            prompts[i].append(i)

        print(str(len(prompts)) + " candidate prompts ready.")
        return prompts

class PromptGeneratorGenerator:
    def __init__(self, ml_experiment):
        self.ml_experiment = ml_experiment
        self.prompt_generators = []

    def generate(self):
        prompt_generators = openai.ChatCompletion.create(
            model=self.ml_experiment.model.name,
            messages=[
                {"role": "system", "content": self.ml_experiment.seed},
                {"role": "user", "content": f"Here are some sample inputs:`{self.ml_experiment.tests}`\n\nRespond with your system prompt and human prompt in json format with keys 'system' and 'human' and nothing else. Be creative."}
                ],
            temperature=self.ml_experiment.model.generation_temperature,
            n=self.ml_experiment.generations
        )
        self.prompt_generators = prompt_generators
        return prompt_generators