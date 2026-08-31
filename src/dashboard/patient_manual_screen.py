# @author: Brunno Ronaldo
# @created: 2026-07-01
# @last updated: 2026-08-09
# @version: 0.6.0

import os  # <-- simple form to clear the screen/terminal
import keyboard  # <-- to capture key presses
import sys  # <-- to exit the program
import time # <-- to simulate time passing

import tkinter as tk

# Import a class from another file in the same directory
from simulator.patient_manual_input import PatientManualInput as pmi

class RecordPatientManual:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Patient Record")
        self.root.geometry("400x300")

        """ Create the input fields """
        
        # Name zone
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        # Age zone
        self.age_label = tk.Label(self.root, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack()

        # CPF zone
        self.cpf_label = tk.Label(self.root, text="CPF:")
        self.cpf_label.pack()
        self.cpf_entry = tk.Entry(self.root)
        self.cpf_entry.pack()

        # Phone zone
        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        # Create the submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        cpf = self.cpf_entry.get()
        phone = self.phone_entry.get()
        patient_input = pmi(name, age, cpf, phone)
        print(f"Patient Input: {patient_input}")

class RecordSymptomsPatient:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Symptoms")
        self.root.geometry("400x300")

        self.sickness_label = tk.Label(self.root, text="Sickness:")
        self.sickness_label.pack()
        self.sickness_entry = tk.Entry(self.root)
        self.sickness_entry.pack()

        # Create the submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        symptom = self.sickness_entry.get()
        print(f"Symptom Input: {symptom}")

class SimulationParameters:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulation Parameters")
        self.root.geometry("400x300")

        # Create the input fields
        self.param_label = tk.Label(self.root, text="Parameter:")
        self.param_label.pack()
        self.param_entry = tk.Entry(self.root)
        self.param_entry.pack()

        # Create the submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        parameter = self.param_entry.get()
        print(f"Simulation Parameter Input: {parameter}")

class PatientManualScreen:
    @staticmethod
    def generate_screen():
        patient_record_screen = RecordPatientManual()
        patient_record_screen.run()

        symptom_record_screen = RecordSymptomsPatient()
        symptom_record_screen.run()

        simulation_parameters_screen = SimulationParameters()
        simulation_parameters_screen.run()