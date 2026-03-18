# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-03-15
# @version: 0.1.0

import random
from simulator import patient
from simulator import nurse


class Hospital:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.nurses = []

    def admit_patient(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            return True
        return False

    def discharge_patient(self, patient_id):
        self.patients = [p for p in self.patients if p.patient_id != patient_id]

    def assign_nurse(self, nurse):
        self.nurses.append(nurse)

    def __str__(self):
        return f"Hospital {self.name} - Capacity: {self.capacity}, Patients: {len(self.patients)}, Nurses: {len(self.nurses)}"
    
    def tick(self):
        print("\nSimulação rodando...")

        to_remove = []

        for patient in self.patients:
            print(f"\n{patient}")

            for condition in patient.conditions[:]:
                recovery_chance = random.random()

                if recovery_chance < (0.1 / condition.severity):
                    print(f"  Recovered from {condition.name}")
                    patient.conditions.remove(condition)
                else:
                    print(f"  Still has {condition.name}")

            if not patient.conditions:
                print(f"  Fully recovered → Discharged")
                to_remove.append(patient)

        for patient in to_remove:
            self.discharge_patient(patient.patient_id)

                                  