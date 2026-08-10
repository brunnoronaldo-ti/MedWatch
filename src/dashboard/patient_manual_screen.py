# @author: Brunno Ronaldo
# @created: 2026-07-01
# @last updated: 2026-07-28
# @version: 0.6.0

from simulator.patient_manual_input import PatientManualInput

# libraries:
import os
import builtins
import threading
import time
from queue import Queue
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.console import Group, Console

input_queue = Queue()
output_queue = Queue()
console = Console()

class PatientManualScreen:
    @staticmethod
    def generate_screen(hospital):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        
        # Create a layout
        layout = Layout()
        layout.split_row(
            Layout(name="main_menu", ratio=1),
            Layout(name="nerd_stats", ratio=1)
        )

        # Create a group to cluster the information in the right side of the panel
        group = Group()

        # Create a progress bar for the patient input process
        progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            expand=True,
        )

        console.print(Panel("Patient Manual Input Screen", style="bold green"))
        

        
