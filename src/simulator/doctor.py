# @author: Brunno Ronaldo
# @created: 2026-03-22
# @last updated: 2026-04-18
# @version: 0.1.0

import random

class Doctor_config:
    def __init__(self, name, specialty, doctor_id, experience_years, capacity):
        self.name = name
        self.specialty = specialty
        self.doctor_id = doctor_id
        self.experience_years = experience_years
        self.capacity = capacity

    def admit_doctor(self, doctor):
        if len(self.doctors) < self.capacity:
            self.doctors.append(doctor)
            return True
        return False
    
    def discharge_doctor(self, doctor_id):
        self.doctors = [d for d in self.doctors if d.doctor_id != doctor_id]
    
    def __str__(self):
        return f"Doctor {self.doctor_id} - {self.name} - Specialty: {self.specialty} - {self.experience_years} years of experience"
    
class Doctor:
    def __init__(self, burnout_meditor=10, working=False, eficacy=1.0, sucesses_rate=100):
        self.burnout_meditor = burnout_meditor
        self.working = working
        self.eficacy = eficacy
        self.sucesses_rate = sucesses_rate

    def doctor_burnout(self):
        #this function will decrease the eficacy of the doctor based on the burnout_meditor and the working hours
        Doctor_config()
        
        for self.doctor_id in self.doctor_id:
            personal_problem = random.randint(1, 10)
            if personal_problem <= 3:
                self.eficacy -= 0.2
        
        while self.working:
            self.burnout_meditor += 1
            if self.burnout_meditor >= 10:
                self.eficacy -= 0.1
                self.burnout_meditor = 0
                while self.eficacy <= 0:
                    self.eficacy = 0
                   
    def work(self):
        self.working = True
        self.doctor_burnout()

        while self.working:
            # Simulate work and update success rate based on efficacy
            self.sucesses_rate = int(self.eficacy * 100)

    #1. fazer a função do burnout
    #2. dar propósito a eficácia de trabalho     