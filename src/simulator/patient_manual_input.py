# @author: Brunno Ronaldo
# @created: 2026-08-07
# @last updated: 2026-08-07
# @version: 0.5.0

import json

class PatientManualInput:
    def __init__(self, name, age, patient_id, conditions):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.conditions = conditions

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "patient_id": self.patient_id,
            "conditions": self.conditions
        }

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)