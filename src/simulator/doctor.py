# @author: Brunno Ronaldo
# @created: 2026-03-22
# @last updated: 2026-03-22
# @version: 0.1.0

class Doctor:
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
    
