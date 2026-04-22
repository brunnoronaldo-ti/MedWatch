# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-04-21
# @version: 0.1.0

# bin/python3
# basic bibliotecas
import time
import colorama
from colorama import Fore, Back, Style, init
#--------------------------------------------

# import class from other files
from simulator.patient import Patient, Condition
from simulator.hospital import Hospital_config, Hospital, Simulation_time
from simulator.nurse import Nurse
from simulator.doctor import Doctor_config, Doctor
#---------------------------------------------

first_time = 0

def main(first_time=0):
    init(autoreset=True)

    # Create hospital
    config = Hospital_config("MedWatch", capacity=10)
    med_watch = Hospital(config)
    
    # Create nurses
    nurse1 = Nurse(1, "Alice", 5)
    nurse2 = Nurse(2, "Bob", 10)
    med_watch.config.assign_nurse(nurse1)
    med_watch.config.assign_nurse(nurse2)

    # Create doctors
    doctor1_config = Doctor_config(1, "Dr. John", "Cardiology", "11 123456789")
    doctor1 = Doctor(doctor1_config)
    doctor2_config = Doctor_config(2, "Dr. Jane", "Neurology", "11 987654321")
    doctor2 = Doctor(doctor2_config)
    
    med_watch.config.assign_doctor(doctor1)
    med_watch.config.assign_doctor(doctor2)

    # Create patients with conditions
    condition1 = Condition("Flu", severity=2, base_recovery_time=7, contagious=True, symptoms=["fever", "cough"])
    condition2 = Condition("Fracture", severity=4, base_recovery_time=30, contagious=False, symptoms=["pain", "swelling"])
    
    patient1 = Patient(1, "John Doe", 30)
    patient1.add_condition(condition1)
    
    patient2 = Patient(2, "Jane Smith", 25)
    patient2.add_condition(condition2)

    # Admit patients to hospital
    med_watch.config.admit_patient(patient1)
    med_watch.config.admit_patient(patient2)

    # Print hospital status
    print(med_watch.config)

    while True:

        if first_time == 0:
            print(f"{Fore.GREEN}welcome to MedWatch - Hospital Simulation{Style.RESET_ALL}")
            print(f"{Fore.CYAN}This simulation models a hospital environment with patients, nurses, and doctors.{Style.RESET_ALL}")
            print(f"{Fore.CYAN}You can observe how patients recover over time and interact with medical staff.{Style.RESET_ALL}")
            print(f"{Fore.CYAN}this simulation is designed for educational purposes and is not a real medical tool.{Style.RESET_ALL}")

            first_time = 1
        else:
            print(f"{Fore.YELLOW}Day {Simulation_time.simulated_data} - Simulation running...{Style.RESET_ALL}")

        time.sleep(1)  # Simulate time passing

        print(f"{Fore.GREEN}\nCurrent Patients:{Style.RESET_ALL}")
        med_watch.tick()

        time.sleep(1)  # Simulate time passing

        input("\nPress Enter to simulate next time step...")
        print("\n" + "-"*50)
        Simulation_time.next_day()

if __name__ == "__main__":
    main()