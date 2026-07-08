# @author: Brunno Ronaldo
# @created: 2026-07-01
# @last updated: 2026-07-08
# @version: 0.5.0

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box


class Dashboard:
    def __init__(self):
        self.console = Console()

    def display_info(self, hospital):
        self.console.print(f"Hospital Name: {hospital.config.name}")
        self.console.print(f"Capacity: {hospital.config.capacity}")
        self.console.print(f"Occupied Beds: {hospital.config.occupied_beds}")
        self.console.print(f"ICU Beds: {hospital.config.ICU}")
        self.console.print(f"Ward Beds: {hospital.config.Ward}")
        self.console.print(f"Emergency Beds: {hospital.config.Emergency}")
        self.console.print(f"Nurses: {[nurse.name for nurse in hospital.config.nurses]}")
        self.console.print(f"Doctors: {[doctor.name for doctor in hospital.config.doctors]}")
        self.console.print(f"Patients: {[patient.name for patient in hospital.config.patients]}")


class painel_layout:
    @staticmethod
    def gerar_interface(hospital):
        console = Console()

        table_info_patient = Table(title="Patient Information", box=box.ROUNDED, style="green")
        table_info_doctor = Table(title="Doctor Information", box=box.ROUNDED, style="red")
        table_info_nurse = Table(title="Nurse Information", box=box.ROUNDED, style="yellow")

        table_info_patient.add_column("Name", style="bold")
        table_info_patient.add_column("Age", style="bold")
        table_info_patient.add_column("Id", style="bold")
        table_info_patient.add_column("Triage", style="bold")

        for patient in hospital.config.patients:
            triage = getattr(patient, "triage_color", "-")
            table_info_patient.add_row(patient.name, str(patient.age), str(patient.patient_id), str(triage))

        table_info_doctor.add_column("Name", style="bold")
        table_info_doctor.add_column("Specialty", style="bold")
        table_info_doctor.add_column("Id", style="bold")
        table_info_doctor.add_column("Status", style="bold")

        for doctor in hospital.config.doctors:
            table_info_doctor.add_row(doctor.name, doctor.specialty, str(doctor.doctor_id), str(getattr(doctor, "status", "ready")))

        table_info_nurse.add_column("Name", style="bold")
        table_info_nurse.add_column("stress_level", style="bold")
        table_info_nurse.add_column("Id", style="bold")
        table_info_nurse.add_column("Status", style="bold")

        for nurse in hospital.config.nurses:
            table_info_nurse.add_row(nurse.name, str(nurse.stress_level), str(nurse.nurse_id), str(getattr(nurse, "status", "ready")))

        console.print(Panel(table_info_patient, title="Simulation", border_style="green"))
        console.print(Panel(table_info_doctor, title="Doctors", border_style="red"))
        console.print(Panel(table_info_nurse, title="Nurses", border_style="yellow"))