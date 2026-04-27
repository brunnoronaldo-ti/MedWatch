# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-04-22
# @version: 0.1.0

import random
import queue
import heapq
import itertools
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
        self._counter = itertools.count()  # Contador para desempate em heapq

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

    def __lt__(self, other):
        return False  # Ou define uma lógica secundária de desempate no futuro

    def priority_queue(self):
        queue = []
        for patient in self.config.patients:
            most_severe = patient.get_most_severe_condition()
            if most_severe:
                heapq.heappush(queue, (-most_severe.severity, next(self.config._counter),patient))
        return queue

    def tick(self):
        queue = self.priority_queue()
    
        while queue:
            _, patient = heapq.heappop(queue)

            for condition in patient.conditions[:]:
                recovery_chance = random.random()

                if recovery_chance < (0.1 / condition.severity):
                    patient.conditions.remove(condition)
                else:
                    # LÓGICA DE PIORA:
                    # Aumenta a severidade em 0.2 a cada tick para condições não tratadas
                    condition.severity += 0.2
                    
                    if condition.severity > 10:
                        condition.severity = 10
                        print(f"  {condition.name} reached CRITICAL state!")

            if not patient.conditions:
                self.config.discharge_patient(patient.patient_id)
    
    def deteriorate(self, patient):
        """Gera uma chance de piora clínica ou morte para pacientes não atendidos."""
        roll = random.random()
        
        # 2% de chance de morte
        if roll < 0.02:
            print(f"  CRITICAL: Patient {patient.patient_id} has passed away.")
            self.config.remove_dead_patient(patient.patient_id)
            return True # Paciente saiu do sistema

        # 15% de chance de desenvolver uma nova condição (comorbidade)
        elif roll < 0.17:
            new_condition = self.generate_random_condition() # add no futuro, a=sem função no momento
            patient.conditions.append(new_condition)
            print(f"  Warning: Patient {patient.patient_id} developed {new_condition.name}!")
        
        # Piora as condições existentes
        else:
            for cond in patient.conditions:
                cond.severity += 1.0 
                
        return False

class Simulation_time:
    # Atributo de classe (compartilhado)
    simulated_data = datetime(2026, 1, 1) 

    @staticmethod
    def next_day():
        # Acessamos o atributo via NomeDaClasse.variavel
        print(f"\n📅 Data Atual: {Simulation_time.simulated_data.strftime('%m/%d/%Y (%A)')}")
        
        # Incrementa o dia
        Simulation_time.simulated_data += timedelta(days=1)