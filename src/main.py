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
from simulator.tools.patient_generator import generate_patients_batch
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

    """
    In this part from the code, we create some sample patients and conditions to demonstrate the simulation.
    In a real-world scenario, patients would be generated dynamically based on various factors. 
    """

    patients = generate_patients_batch(8, config)

    # Admit patients to hospital.
    for patient in patients: 
        med_watch.config.admit_patient(patient)
    
    """
    The end from the patients and conditions creation. Now we will admit the patients to the hospital and start the simulation loop.
    The simulation loop will run indefinitely, simulating the passage of time and allowing the user
    to observe the state of the hospital and its patients. The user can press Enter to advance
    to the next time step, which will simulate a day passing in the hospital.
    The simulation will print the current state of the hospital, including the number of patients, nurses
    """

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