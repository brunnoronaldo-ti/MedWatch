# @author: Brunno Ronaldo
# @created: 2026-07-01
# @last updated: 2026-07-28
# @version: 0.5.0

from rich.layout import Layout
from rich.table import Table
from rich import box
from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console, Group  

import os  # <-- simple form to clear the screen/terminal

from simulator.tools.time_simulator import SimulationTime
from ia_engine.triage_engine import TriageEngine

console = Console()

class panel_layout:
    @staticmethod
    def generate_interface(hospital):
        # The windows use 'cls' and Linux/Mac 'clear'
        os.system('cls' if os.name == 'nt' else 'clear') #`os.system` is used to runs shell terminal commands directly inside python 

        # Define the layout 
        layout = Layout()
        layout.split_row(
            Layout(name="main_menu", ratio=1),
            Layout(name="nerd_stats", ratio=1)
        )

        # The Line bellow don't have any effect, but I will keep it for future use
        group = Group()  # <-- I will create a group to cluster the information in the right side of the panel
        
        # create the tables (patients, doctors, nurses)
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

        # text with hospital information 
        info_hospital_texto = (
            f"Hospital Name: {hospital.config.name}\n"
            f"Capacity (Capacidade): {hospital.config.capacity}\n"
            f"Occupied Beds(Camas Ocupadas): {hospital.config.occupied_beds}\n"
            f"ICU Beds(UTI): {hospital.config.ICU}\n"
            f"Ward Beds(Enfermaria): {hospital.config.Ward}\n"
            f"Emergency Beds(Emergência): {hospital.config.Emergency}"
        )

        # CLUSTER ALL: We group the text and the tables with `group` 
        right_content = Group(
            Panel(info_hospital_texto, title="Hospital Stats", border_style="cyan"),
            table_info_patient,
            table_info_doctor,
            table_info_nurse
        )
        
        # Left side (nerd_stats)
        layout["nerd_stats"].update(Panel(right_content, title="Simulation Data", border_style="blue"))

        # Right Side (Menu)
        layout["main_menu"].update(
            Panel(
                """ Bem vindo ao MedWatch

                Este projeto apresenta o MedWatch, um sistema de simulação hospitalar desenvolvido em linguagem Python para otimizar o fluxo de pronto-socorro, visando reduzir a sobrecarga cognitiva de equipes de enfermagem e humanizar o atendimento.
                A metodologia consistiu na modelagem de um ambiente hospitalar virtual e no desenvolvimento de um sistema especialista baseado em regras. Esse algoritmo analisa os sintomas apresentados pelos pacientes simulados e executa a triagem automatizada utilizando como referência os critérios de gravidade do Protocolo de Manchester (atribuindo cores como vermelho, laranja, amarelo, verde e azul).
                Os resultados parciais demonstram que o simulador é funcional, executa a alocação dinâmica de prioridades de forma automatizada e implementa a lógica de organização de prioridades para os profissionais de saúde. Como perspectivas futuras, o projeto prevê o refinamento das variáveis médicas do simulador e a implementação de uma interface digital de cabeceira com síntese facial e de voz integrada a modelos generativos de IA. Conclui-se que o MedWatch demonstra viabilidade técnica na automação da triagem, servindo como base para ferramentas que otimizem fluxos hospitalares críticos e reduzam o burnout na saúde.            
                
----------------------------------------------------------------------------
                \nMain Menu\n\nAperte Enter para avançar o dia.""",
                title="Menu",
                border_style="blue"
            )
        )

        # Render the layout to the console
        console.print(layout) 
        Prompt.ask(default="")# <-- Pause the simulation until the user presses Enter to advance the day