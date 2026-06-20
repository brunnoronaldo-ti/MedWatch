# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-05-31
# @version: 0.4.1

import random
import queue
import heapq
import itertools
from datetime import datetime, timedelta
from simulator.patient import Patient, Condition
from simulator.nurse import Nurse
from simulator.doctor import Doctor, DoctorConfig

#this class hold all config
class HospitalConfig:
    def __init__(self, name, capacity, occupied_beds, ICU, Ward, Emergency):
        self.name = name
        self.capacity = capacity
        self.occupied_beds = occupied_beds # add no futuro, a=sem função no momento/ camas ocupadas
        self.ICU = ICU # add no futuro, a=sem função no momento/ camas de UTI
        self.Ward = Ward # add no futuro, a=sem função no momento/ camas
        self.Emergency = Emergency # add no futuro, a=sem função no momento/ camas de emergência
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
    def __init__(self, config: HospitalConfig):
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
            _, _, patient = heapq.heappop(queue)

            for condition in patient.conditions[:]:
                    
                if condition.treated == False:
                    # Simula o tratamento (aqui você pode adicionar lógica de tratamento real)
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
            self.config.discharge_patient(patient.patient_id)
            return True

        # Piora as condições existentes
        for cond in patient.conditions:
            cond.severity += 1.0

        return False

class SimulationTime:
    # Atributo de classe (compartilhado)
    simulated_data = datetime(2026, 1, 1) 

    @staticmethod
    def next_day():
        # Acessamos o atributo via NomeDaClasse.variavel
        print(f"\n📅 current date: {SimulationTime.simulated_data.strftime('%m/%d/%Y (%A)')}")
        
        # add day to simulated_data
        SimulationTime.simulated_data += timedelta(days=1)