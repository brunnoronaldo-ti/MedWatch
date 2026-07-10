# @author: Brunno Ronaldo
# @created: 2026-07-01
# @last updated: 2026-07-09
# @version: 0.5.0

from rich.layout import Layout
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.console import Console, Group  # <-- Importamos o Group aqui
import os  # <-- Importamos para limpar a tela de forma simples

console = Console()

class painel_layout:
    @staticmethod
    def gerar_interface(hospital):
        # 1. Limpa o terminal para evitar a rolagem infinita
        # Usa 'cls' para Windows e 'clear' para Linux/Mac
        os.system('cls' if os.name == 'nt' else 'clear')

        # 2. Definir o Layout
        layout = Layout()
        layout.split_row(
            Layout(name="nerd_stats", ratio=1), 
            Layout(name="main_menu", ratio=1)   
        )
        
        # 3. Criar as Tabelas (Pacientes, Médicos, Enfermeiros)
        table_info_patient = Table(title="Patient Information", box=box.ROUNDED, style="green", expand=True)
        table_info_patient.add_column("Name", style="bold")
        table_info_patient.add_column("Age", style="bold")
        table_info_patient.add_column("Id", style="bold")
        table_info_patient.add_column("Triage", style="bold")
        for patient in hospital.config.patients:
            triage = getattr(patient, "triage_color", "-")
            table_info_patient.add_row(patient.name, str(patient.age), str(patient.patient_id), str(triage))

        table_info_doctor = Table(title="Doctor Information", box=box.ROUNDED, style="red", expand=True)
        table_info_doctor.add_column("Name", style="bold")
        table_info_doctor.add_column("Specialty", style="bold")
        table_info_doctor.add_column("Id", style="bold")
        table_info_doctor.add_column("Status", style="bold")
        for doctor in hospital.config.doctors:
            table_info_doctor.add_row(doctor.name, doctor.specialty, str(doctor.doctor_id), str(getattr(doctor, "status", "ready")))

        table_info_nurse = Table(title="Nurse Information", box=box.ROUNDED, style="yellow", expand=True)
        table_info_nurse.add_column("Name", style="bold")
        table_info_nurse.add_column("stress_level", style="bold")
        table_info_nurse.add_column("Id", style="bold")
        table_info_nurse.add_column("Status", style="bold")
        for nurse in hospital.config.nurses:
            table_info_nurse.add_row(nurse.name, str(nurse.stress_level), str(nurse.nurse_id), str(getattr(nurse, "status", "ready")))

        # 4. Texto com as informações gerais do hospital
        info_hospital_texto = (
            f"Hospital Name: {hospital.config.name}\n"
            f"Capacity: {hospital.config.capacity}\n"
            f"Occupied Beds: {hospital.config.occupied_beds}\n"
            f"ICU Beds: {hospital.config.ICU}\n"
            f"Ward Beds: {hospital.config.Ward}\n"
            f"Emergency Beds: {hospital.config.Emergency}"
        )

        # 5. AGRUPAR TUDO: Juntamos o texto e as tabelas usando o Group
        conteudo_esquerdo = Group(
            Panel(info_hospital_texto, title="Hospital Stats", border_style="cyan"),
            table_info_patient,
            table_info_doctor,
            table_info_nurse
        )
        
        # 6. Jogamos o grupo completo dentro de um grande painel no lado "nerd_stats"
        layout["nerd_stats"].update(Panel(conteudo_esquerdo, title="Simulation Data", border_style="blue"))

        # Lado direito (Menu)
        layout["main_menu"].update(Panel("Main Menu\n\nAperte Enter para avançar o turno...", title="Menu"))

        # 7. Renderiza o layout atualizado na tela
        console.print(layout)