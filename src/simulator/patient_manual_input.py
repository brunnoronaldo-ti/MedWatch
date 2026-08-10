# @author: Brunno Ronaldo
# @created: 2026-08-07
# @last updated: 2026-08-09
# @version: 0.6.0

import json
import os
from typing import Dict

class PatientManualInput:
    def __init__(self, name, age, patient_id, conditions):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.conditions = conditions
 
    _disease_cache = None

    def load_diseases() -> Dict:
    
        # Load disease library from JSON file and cache result.
        # Returns dict of disease_name -> disease_attributes.

        if PatientManualInput._disease_cache is not None:
            return PatientManualInput._disease_cache

        disease_file = os.path.join(
            os.path.dirname(__file__),
            'disease_library.json'
        )

        try:
            with open(disease_file, 'r') as f:
                data = json.load(f)
                PatientManualInput._disease_cache = data.get('content', {}).get('disease_library', {})
                return PatientManualInput._disease_cache
        except FileNotFoundError:
            print(f"Warning: Disease library not found at {disease_file}")
            return {}
        except json.JSONDecodeError:
            print(f"Warning: Failed to parse disease library JSON")
            return {}

    def patient_details_simple(self, load_diseases):
        # User input for patient details
        name = input("Enter patient name: ").capitalize()
        age = int(input("Enter patient age: "))

        patient_manual = []
        while True:
            print("All conditions available in the disease library:")
            for cond in PatientManualInput.load_diseases():
                print(f" - {cond}")
            condition = input("Enter a medical condition (or type 'done' or 'feito' to finish): ")
            if condition.lower() == 'done' or condition.lower() == 'feito':
                break
            elif condition.lower() in load_diseases():
                disease_info = load_diseases()[condition.lower()]
            elif condition.lower() not in load_diseases():
                print(f"Warning: '{condition}' is not in the disease library.")
                confirm_input_condition = input("Do you want to add it anyway? (yes/no): ").strip().lower()
                if confirm_input_condition == 'no':
                    print("Condition not added. Please enter a valid condition.")
                    continue
                elif confirm_input_condition == 'yes':
                    print(f"Adding '{condition}' to the patient's conditions. Tell me more about this condition, please.")
                    severity = input("Enter the severity of the condition (mild/moderate/severe): ").strip().lower()
                    duration = input("Enter the duration of the condition (short-term/long-term): ").strip().lower()
                    description = input("Enter a description of the condition: ").strip()
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    continue

            patient_manual.append({
                "name": condition,
                "severity": severity,
                "duration": duration,
                "description": description
            })

        return {
            "name": name,
            "age": age,
            "conditions": patient_manual
        }

    def __str__(self):
            return (
                f"Patient: {self.name}\n"
                f"Age: {self.age}\n"
                f"ID: {self.patient_id}\n"
                f"Conditions: {self.conditions}"
            )

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