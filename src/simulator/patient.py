# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-06-29
# @version: 0.2.0

class Condition:

    def __init__(self, name, severity, base_recovery_time, contagious=False, treatments=None, 
                 symptoms=None, triage_color=None, max_wait_time=None, triage_reasons=None):

        self.name = name
        self.severity = severity
        self.base_recovery_time = base_recovery_time
        self.contagious = contagious
        self.treatments = treatments or []
        self.symptoms = symptoms or []
        self.triage_color = triage_color
        self.max_wait_time = max_wait_time
        self.triage_reasons = triage_reasons or []
        self.treated = False

class Patient:

    def __init__(self, patient_id, name, age, conditions=None):

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.conditions = conditions or []

        self.vitals = {
            "heart_rate": 80,
            "oxygen": 98,
            "temperature": 36.5
        }

        self.triage_level = None

    def add_condition(self, condition):
        self.conditions.append(condition)

    def get_most_severe_condition(self):
        if not self.conditions:
            return None
        return max(self.conditions, key=lambda c: c.severity)
    
    def __str__(self):
        return f"Patient {self.patient_id} - {self.name} ({self.age})"