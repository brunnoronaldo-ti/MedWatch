# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-03-30
# @version: 0.1.0

from dataclasses import dataclass, field
from typing import List

@dataclass
class Nurse:
    nurse_id: int
    name: str
    experience_years: int

    def __str__(self):
        return f"nurse {self.nurse_id} - {self.name} - {self.experience_years} years of experience"
       
@dataclass
class Care_Plan:
    patient: object
    condition: object
    assigned_nurse: Nurse
    assigned_doctor: object
    treatments: List[str] = field(default_factory=list)

    def add_treatment(self, treatment: str):
        self.treatments.append(treatment)

   