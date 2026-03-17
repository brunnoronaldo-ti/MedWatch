# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-03-15
# @version: 0.1.0

class hospital:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.nurses = []

    def admit_patient(self, patient):
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            return True
        return False

    def discharge_patient(self, patient_id):
        self.patients = [p for p in self.patients if p.patient_id != patient_id]

    def assign_nurse(self, nurse):
        self.nurses.append(nurse)

    def __str__(self):
        return f"Hospital {self.name} - Capacity: {self.capacity}, Patients: {len(self.patients)}, Nurses: {len(self.nurses)}"