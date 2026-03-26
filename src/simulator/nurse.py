# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-03-25
# @version: 0.1.0

class Nurse:

    def __init__(self, nurse_id, name, experience_years):
        self.nurse_id = nurse_id
        self.name = name
        self.experience_years = experience_years

    def __str__(self):
        return f"Nurse {self.nurse_id} - {self.name} ({self.experience_years} years experience)"
    
class care_plan:
    def __init__(self, patient, condition, assigned_nurse, assigned_doctor, treatments=None):
        self.patient = patient
        self.condition = condition
        self.assigned_nurse = assigned_nurse
        self.assigned_doctor = assigned_doctor
        self.treatments = treatments or []
