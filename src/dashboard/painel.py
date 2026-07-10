# @author: Brunno Ronaldo
# @created: 2026-07-01
# @last updated: 2026-07-09
# @version: 0.5.0

from rich.layout import Layout
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.console import Console

console = Console()

class painel_layout:
    @staticmethod
    def gerar_interface(hospital):
        # 1. Definir o Layout
        layout = Layout()
        layout.split_row(
            Layout(name="nerd_stats", ratio=1), # Lado Esquerdo
            Layout(name="main_menu", ratio=1)   # Lado Direito
        )
        
        # 2. Criar as Tabelas
        table_info_patient = Table(title="Patient Information", box=box.ROUNDED, style="green")
        table_info_doctor = Table(title="Doctor Information", box=box.ROUNDED, style="red")
        table_info_nurse = Table(title="Nurse Information", box=box.ROUNDED, style="yellow")
        
        # Tabela de Pacientes
        table_info_patient.add_column("Name", style="bold")
        table_info_patient.add_column("Age", style="bold")
        table_info_patient.add_column("Id", style="bold")
        table_info_patient.add_column("Triage", style="bold")
        for patient in hospital.config.patients:
            triage = getattr(patient, "triage_color", "-")
            table_info_patient.add_row(patient.name, str(patient.age), str(patient.patient_id), str(triage))

        # Tabela de Médicos
        table_info_doctor.add_column("Name", style="bold")
        table_info_doctor.add_column("Specialty", style="bold")
        table_info_doctor.add_column("Id", style="bold")
        table_info_doctor.add_column("Status", style="bold")
        for doctor in hospital.config.doctors:
            table_info_doctor.add_row(doctor.name, doctor.specialty, str(doctor.doctor_id), str(getattr(doctor, "status", "ready")))

        # Tabela de Enfermeiros
        table_info_nurse.add_column("Name", style="bold")
        table_info_nurse.add_column("stress_level", style="bold")
        table_info_nurse.add_column("Id", style="bold")
        table_info_nurse.add_column("Status", style="bold")
        for nurse in hospital.config.nurses:
            table_info_nurse.add_row(nurse.name, str(nurse.stress_level), str(nurse.nurse_id), str(getattr(nurse, "status", "ready")))

        # 3. Painel da Esquerda (Estatísticas e Tabelas)
        # Agrupando tudo que vai para o lado esquerdo
        nerd_panel_content = Panel(
            f"Hospital Name: {hospital.config.name}\n"
            f"Capacity: {hospital.config.capacity}\n"
            f"Occupied Beds: {hospital.config.occupied_beds}\n"
            f"ICU Beds: {hospital.config.ICU}\n"
            f"Ward Beds: {hospital.config.Ward}\n"
            f"Emergency Beds: {hospital.config.Emergency}",
            title="Simulation Status"
        )

        """
            below is the code that will be used to display the information in the terminal
            using rich library, it will create a layout with two columns, one for
            the nerd stats and another for the main menu, and will display the information
            of patients, doctors and nurses in tables.
        """
        
        # O layout espera um único elemento, então agrupamos tudo em uma lista ou painel maior
        # Aqui, estamos simplesmente atualizando o lado "nerd_stats" com as informações do hospital
        layout["nerd_stats"].update(nerd_panel_content)

        # 4. Painel da Direita (Menu)
        layout["main_menu"].update(Panel("Main Menu\nOpções de controle aqui", title="Menu"))

        # 5. Imprimir o Layout na tela
        console.print(layout)

        # Se quiser exibir as tabelas separadamente embaixo do layout, você pode fazer isso aqui:
        console.print(Panel(table_info_patient, title="Patient Table", border_style="green"))
        console.print(Panel(table_info_doctor, title="Doctor Table", border_style="red"))
        console.print(Panel(table_info_nurse, title="Nurse Table", border_style="yellow"))