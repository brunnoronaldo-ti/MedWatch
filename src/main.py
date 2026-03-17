# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-03-15
# @version: 0.1.0

import random
from simulator.patient import Patient, Condition
from simulator.hospital import hospital
from simulator.nurse import nurse

def main():
    # Create hospital
    med_watch = hospital("MedWatch", capacity=100)

    # Create nurses
    nurse1 = nurse(1, "Alice", 5)
    nurse2 = nurse(2, "Bob", 10)
    med_watch.assign_nurse(nurse1)
    med_watch.assign_nurse(nurse2)

    # Create patients with conditions
    condition1 = Condition("Flu", severity=2, base_recovery_time=7, contagious=True, symptoms=["fever", "cough"])
    condition2 = Condition("Fracture", severity=4, base_recovery_time=30, contagious=False, symptoms=["pain", "swelling"])
    
    patient1 = Patient(1, "John Doe", 30)
    patient1.add_condition(condition1)
    
    patient2 = Patient(2, "Jane Smith", 25)
    patient2.add_condition(condition2)

    # Admit patients to hospital
    med_watch.admit_patient(patient1)
    med_watch.admit_patient(patient2)

    # Print hospital status
    print(med_watch)

if __name__ == "__main__":
    main()

    