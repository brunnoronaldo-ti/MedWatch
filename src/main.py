# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-06-19
# @version: 0.4.1

# bin/python3
# basic bibliotecas
import time
import colorama
from colorama import Fore, Back, Style, init
#--------------------------------------------

# import class from other files
from simulator.patient import Patient, Condition
from simulator.hospital import HospitalConfig, Hospital, SimulationTime
from simulator.nurse import Nurse
from simulator.doctor import DoctorConfig, Doctor
#---------------------------------------------

def main():
    init(autoreset=True)

    # Create hospital
    config = HospitalConfig("MedWatch", capacity=10, occupied_beds=0, ICU=0, Ward=0, Emergency=0)
    med_watch = Hospital(config)

    # Create nurses
    nurse1 = Nurse(1, "Alice", 5)
    nurse2 = Nurse(2, "Bob", 10)
    med_watch.config.assign_nurse(nurse1)
    med_watch.config.assign_nurse(nurse2)

    # Create doctors
    doctor1_config = DoctorConfig("Dr. John", "Cardiology", 1, 10)
    doctor1 = Doctor(doctor1_config)
    doctor2_config = DoctorConfig("Dr. Jane", "Neurology", 2, 8)
    doctor2 = Doctor(doctor2_config)

    med_watch.config.assign_doctor(doctor1)
    med_watch.config.assign_doctor(doctor2)

    # Create patients with conditions
    condition1 = Condition("Flu", base_recovery_time=7, contagious=True, symptoms=["fever", "cough"], triage_color="yellow")
    condition2 = Condition("Fracture", base_recovery_time=30, contagious=False, symptoms=["pain", "swelling"], triage_color="orange")

    patient1 = Patient(1, "John Doe", 30)
    patient1.add_condition(condition1)

    patient2 = Patient(2, "Jane Smith", 25)
    patient2.add_condition(condition2)

    # Admit patients to hospital
    med_watch.config.admit_patient(patient1)
    med_watch.config.admit_patient(patient2)

    # Print hospital status
    print(med_watch.config)

    first_time = True
    while True:

        if first_time:
            print(f"{Fore.GREEN}welcome to MedWatch - Hospital Simulation{Style.RESET_ALL}")
            print(f"{Fore.CYAN}This simulation models a hospital environment with patients, nurses, and doctors.{Style.RESET_ALL}")
            print(f"{Fore.CYAN}You can observe how patients recover over time and interact with medical staff.{Style.RESET_ALL}")
            print(f"{Fore.CYAN}this simulation is designed for educational purposes and is not a real medical tool.{Style.RESET_ALL}")

            first_time = False
        else:
            print(f"{Fore.YELLOW}Day {SimulationTime.simulated_data} - Simulation running...{Style.RESET_ALL}")

        time.sleep(1)  # Simulate time passing

        print(f"{Fore.GREEN}\nCurrent Patients:{Style.RESET_ALL}")
        med_watch.tick()

        time.sleep(1)  # Simulate time passing

        input("\nPress Enter to simulate next time step...")
        print("\n" + "-"*50)
        SimulationTime.next_day()

if __name__ == "__main__":
    main()

