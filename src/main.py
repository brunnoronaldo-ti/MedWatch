# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-06-19
# @version: 0.5.0

# bin/python3
# basic bibliotecas
import sys
import time
from pathlib import Path

import colorama
from colorama import Fore, Style, init

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# import class from other files
from dashboard.painel import painel_layout
from simulator.hospital import HospitalConfig, Hospital, SimulationTime
from simulator.nurse import Nurse
from simulator.doctor import DoctorConfig, Doctor
from simulator.tools.patient_generator import generate_patients_batch
# ---------------------------------------------


def main(max_iterations=None):
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

    generate_patients_batch(8, config)

    print(f"{Fore.GREEN}welcome to MedWatch - Hospital Simulation{Style.RESET_ALL}")
    print(f"{Fore.CYAN}This simulation models a hospital environment with patients, nurses, and doctors.{Style.RESET_ALL}")
    print(f"{Fore.CYAN}You can observe how patients recover over time and interact with medical staff.{Style.RESET_ALL}")
    print(med_watch.config)

    first_time = True
    iteration = 0
    while True:
        if first_time:
            print(f"{Fore.YELLOW}Starting simulation...{Style.RESET_ALL}")
            first_time = False

        painel_layout.gerar_interface(med_watch)
        SimulationTime.advance_time()
        med_watch.update_hospital_status()
        print(med_watch.config)

        iteration += 1
        if max_iterations is not None and iteration >= max_iterations:
            break

        time.sleep(0.1)


if __name__ == "__main__":
    main()