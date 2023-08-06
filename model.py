import json
import os
from datetime import datetime
import openai

class Model:
    def __init__(self, model_name, generation_temperature=0.9, ranking_temperature=0.1):
        self.model_name = model_name
        self.generation_temperature = generation_temperature
        self.ranking_temperature = ranking_temperature
        
    def get_completion(self, system, human):
        output = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": human}
            ],
            temperature= self.ranking_temperature,
        ).choices[0].message.content
        return output

    def to_json(self):
        return {
            "model_name": self.model_name,
            "generation_temperature": self.generation_temperature,
            "ranking_temperature": self.ranking_temperature
        }

    @classmethod
    def from_json(cls, data):
        return cls(**data)