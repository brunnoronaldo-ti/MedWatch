# @author: Brunno Ronaldo
# @created: 2026-03-22
# @last updated: 2026-05-31
# @version: 0.4.1

import random
from simulator import patient
from simulator import nurse 

class DoctorConfig:
    def __init__(self, name,  specialty, doctor_id, experience_years):
        self.name = name
        self.specialty = specialty
        self.doctor_id = doctor_id
        self.experience_years = experience_years
        
    def __str__(self):
        return f"Doctor {self.doctor_id} - {self.name} - Specialty: {self.specialty} - {self.experience_years} years of experience"
    
class Doctor:
    def __init__(self, config: Doctor_config, burnout_meter=10, working=False, efficacy=1.0):
        self.config = config
        self.burnout_meter = burnout_meter
        self.working = working
        self.efficacy = efficacy
        self.success_rate = int(self.efficacy * 100)

    def doctor_burnout(self):
        if self.working:
            self.burnout_meter += 1

            if self.burnout_meter >= 10:
                self.efficacy -= 0.1
                self.burnout_meter = 0

        personal_problems_chance = random.randint(1, 10)
        if personal_problems_chance == 1:
            self.efficacy -= 0.05

        self.efficacy = max(0, self.efficacy)

    def work(self):
        self.working = True
        self.doctor_burnout()
        self.success_rate = int(self.efficacy * 100)

    def calculate_success_rate(self):
        experience_bonus = (
            self.config.experience_years ** 0.5
        ) * 0.02
        self.success_rate = int((self.efficacy + experience_bonus) * 100)
        return self.success_rate

    def treat_patient(self, patient):

        condition = patient.get_most_severe_condition()
        if not condition:
            return

        condition.severity = max(0, condition.severity)
        if condition.severity == 0:
            patient.conditions.remove(condition)
            return

        success = random.random()

        if success < self.efficacy:
            condition.severity -= 2

        else:
            condition.severity += 1
