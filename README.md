Meta Layers
0. Experiment Input
    1. Seed Prompt
    2. Test Inputs
    3. Ranking Prompt
    4. Model Data
1. Prompt Generator Generator
2. Prompt Generator
3. Prompt Set
4. Output Set


Meta Layer Experiment:
1. Pass 1: Search for Optimal Prompt Generator
    1. Generate Prompt Generators
    2. Generate Prompts from each Generator
    3. Generate Outputs from each Prompt
    4. Rank Outputs Generated with Ranking Prompt
    5. Record Set of Best Prompts and Best Prompt Generators
    6. Rerun the Experiment a number of times each time seeding the best prompt generator from previous experiment.
    7. Declare an optimal prompt and move onto pass 2.
2. Pass 2: Search for the Optimal Prompt
    1. Generate Prompts from the winning Generator from pass 1
    2. Seed winning prompts from pass 1 and every run from pass 2.
    3. Generate Outputs from each Prompt
    4. Rank Outputs Generated with Ranking Prompt
    5. Record Best Prompt
    6. Rerun the Experiment a number of times each time seeding the best prompt from the previous experiment.
    7. Declare an optimal prompt and field test with live data/use case.


Cost and Complexity Analysis: