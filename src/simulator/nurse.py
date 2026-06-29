# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-06-19
# @version: 0.2.0

from dataclasses import dataclass, field
from typing import List
from ia_engine.triage_engine import TriageEngine
from simulator import patient

@dataclass
class Nurse:
    nurse_id: int
    name: str
    experience_years: int
    stress_level: int = 0
    patients_attended_today: List[patient.Patient] = field(default_factory=list)
    error_chance: float = 0.05  # Chance base de erro devido ao estresse

    def __str__(self):
        return f"nurse {self.nurse_id} - {self.name} - {self.experience_years} years of experience"
    
    def triage_patient(self, patient):

        result = TriageEngine.evaluate(patient)

        patient.triage_color = result["color"]
        patient.max_wait_time = result["wait_time"]
        patient.triage_reasons = result["reasons"]

    def Burnout_in_nurse(self):

       patients_attended_today = len(self.patients_attended_today)
       if patients_attended_today >= 1:
            self.stress_level += 1
            if self.stress_level >= 5:
                self.error_chance += 0.01
      
@dataclass
class Care_Plan:
    patient: object
    condition: object
    assigned_nurse: Nurse
    assigned_doctor: object
    treatments: List[str] = field(default_factory=list)

    def add_treatment(self, treatment: str):
        self.treatments.append(treatment)