# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-03-24
# @version: 0.1.0

import time
from simulator.patient import Patient, Condition
from simulator.hospital import Hospital, Simulation_time
from simulator.nurse import Nurse
from simulator.doctor import Doctor

def main():
    # Create hospital
    med_watch = Hospital("MedWatch", capacity=100)

    # Create nurses
    nurse1 = Nurse(1, "Alice", 5)
    nurse2 = Nurse(2, "Bob", 10)
    med_watch.assign_nurse(nurse1)
    med_watch.assign_nurse(nurse2)

    # Create doctors
    doctor1 = Doctor(1, "Dr. John", "Cardiology", "11 123456789")
    doctor2 = Doctor(2, "Dr. Jane", "Neurology", "11 987654321")
    med_watch.assign_doctor(doctor1)
    med_watch.assign_doctor(doctor2)

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

    while True:

        time.sleep(1)  # Simulate time passing
        
        print("\nCurrent Patients:")
        med_watch.tick()

        time.sleep(1)  # Simulate time passing

        input("\nPress Enter to simulate next time step...")
        print("\n" + "-"*50)
        Simulation_time.next_day()

if __name__ == "__main__":
    main()

    