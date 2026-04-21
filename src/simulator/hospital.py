# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-04-21
# @version: 0.1.0

import random
from datetime import datetime, timedelta
from simulator.patient import Patient, Condition
from simulator.nurse import Nurse
from simulator.doctor import Doctor, Doctor_config

#this class hold all config
class Hospital_config:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.nurses = []
        self.doctors = []

    def admit_patient(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            return True
        return False

    def discharge_patient(self, patient_id):
        self.patients = [p for p in self.patients if p.patient_id != patient_id]

    def assign_nurse(self, nurse):
        self.nurses.append(nurse)

    def assign_doctor(self, doctor):
        self.doctors.append(doctor)

    def __str__(self):
        return f"Hospital {self.name} - Capacity: {self.capacity}, Patients: {len(self.patients)}, Nurses: {len(self.nurses)}, Doctors: {len(self.doctors)}"


class Hospital:
    def __init__(self, config: Hospital_config):
        self.config = config

    def tick(self):
        
        to_remove = []

        for patient in self.patients:
            print(f"\n{patient}")

            for condition in patient.conditions[:]:
                recovery_chance = random.random() #lucky number between 0 and 1

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

class Simulation_time:
    # Atributo de classe (compartilhado)
    simulated_data = datetime(2026, 1, 1) 

    @staticmethod
    def next_day():
        # Acessamos o atributo via NomeDaClasse.variavel
        print(f"\n📅 Data Atual: {Simulation_time.simulated_data.strftime('%m/%d/%Y (%A)')}")
        
        # Incrementa o dia
        Simulation_time.simulated_data += timedelta(days=1)