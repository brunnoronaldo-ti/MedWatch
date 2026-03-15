class condition:
    def __init__(self, name, severity, base_recovery_time, contagious=False, treatments=[], symptoms=[]):
        self.name = name
        self.severity = severity #ex: 1-5, 5 being the most severe
        self.base_recovery_time = base_recovery_time
        self.contagious = contagious
        self.treatments = treatments
        self.symptoms = symptoms


class patient:
    def __init__(self, patient_id, name, age, conditions=[]):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.conditions = conditions