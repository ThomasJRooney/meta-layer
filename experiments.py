import json
import os
from model import Model

class Experiments:
    def __init__(self, name, seed, tests, ranking, model):
        self.name = name
        self.seed = seed
        self.tests = tests
        self.ranking = ranking
        self.model = model

    def to_json(self):
        return {
            "name": self.name,
            "seed": self.seed,
            "tests": self.tests,
            "ranking": self.ranking,
            "model": self.model.to_json()  # Serialize the Model object using its to_json method
        }

    def save_to_file(self):
        directory = os.path.join("experiments", self.name)
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = os.path.join(directory, f"{self.name}.json")
        with open(filename, 'w') as file:
            json.dump(self.to_json(), file)

    @classmethod
    def from_json(cls, data):
        model_data = data.pop("model")
        model = Model.from_json(model_data)
        return cls(model=model, **data)

    @classmethod
    def load_from_file(cls, experiment_name):
        directory = "experiments"
        filename = os.path.join(directory, f"{experiment_name}_experiment.json")
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Experiment file '{filename}' not found.")

        with open(filename, 'r') as file:
            data = json.load(file)
        return cls.from_json(data)

    def __str__(self):
        return f"Experiment: {self.name}\nSeed: {self.seed}\nTests: {self.tests}\nRanking: {self.ranking}\nModel: {self.model}"

    
   