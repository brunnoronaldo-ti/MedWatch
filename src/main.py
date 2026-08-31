# @author: Brunno Ronaldo
# @created: 2026-03-15
# @last updated: 2026-08-09
# @version: 0.6.0

# bin/python3

# Libraries:
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Layouts:
from dashboard.main_menu import main_menu_choice_next_window
from dashboard.panel import panel_layout
from dashboard.patient_manual_screen import PatientManualScreen

# Hospital, Nurse, Doctor, Patient:
from simulator.hospital import HospitalConfig, Hospital
from simulator.nurse import Nurse
from simulator.doctor import DoctorConfig, Doctor

# Tools:
from simulator.tools.patient_generator import generate_patients_batch
from simulator.tools.time_simulator import SimulationTime
from ia_engine.triage_engine import TriageEngine
# ---------------------------------------------

def main(max_iterations=None):

    # Create hospital
    config = HospitalConfig("MedWatch", capacity=100, occupied_beds=0, ICU=0, Ward=0, Emergency=0)
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

    generate_patients_batch(10, config) # Change the number to increase the total patients in the hospital

    print(med_watch.config)

    first_time = True
    iteration = 0

    while True:
        if first_time:
            print(f"Starting simulation...")
            time.sleep(2)

            next_window = main_menu_choice_next_window()

            first_time = False

        if next_window == "automatic":
            while True:
                panel_layout.generate_interface(med_watch)
                SimulationTime.advance_time()
                
                # Do triage for all patients in the hospital
                if hasattr(med_watch, 'patients'):
                    for patient in med_watch.patients:
                        triage_result = TriageEngine.evaluate(patient)
                        # Save the triage result in the patient object
                        patient.triage = triage_result 
                
                med_watch.update_hospital_status()
                
                iteration += 1
                if max_iterations is not None and iteration >= max_iterations:
                    break
                
                med_watch.tick()
                
                time.sleep(1)  # Simulate time passing
        elif next_window == "manual":
            while True:
                PatientManualScreen.generate_screen()
                med_watch.tick()
        else:
            print("Exiting simulation...")
            time.sleep(1)
            print("thank you for using MedWatch!")
            break

if __name__ == "__main__":
    main()