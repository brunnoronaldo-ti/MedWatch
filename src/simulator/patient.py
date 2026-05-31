# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-04-18
# @version: 0.4.1

class Condition:

    def __init__(self, name, severity, base_recovery_time, contagious=False, treatments=None, symptoms=None):

        self.name = name
        self.severity = severity
        self.base_recovery_time = base_recovery_time
        self.contagious = contagious
        self.treatments = treatments or []
        self.symptoms = symptoms or []
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
    
    def calculate_triage(self):
        condition = self.get_most_severe_condition()

        if condition.severity >= 9:
            self.triage_level = "RED"

        elif condition.severity >= 7:
            self.triage_level = "ORANGE"

        elif condition.severity >= 5:
            self.triage_level = "YELLOW"

        elif condition.severity >= 3:
            self.triage_level = "GREEN"

        else:
            self.triage_level = "BLUE"
    
    def __str__(self):
        return f"Patient {self.patient_id} - {self.name} ({self.age})"