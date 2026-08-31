# @author: Brunno Ronaldo
# @created: 2026-07-01
# @last updated: 2026-08-30
# @version: 0.7.0

import os
try:
    import keyboard
except Exception:
    keyboard = None
import sys
import time

import tkinter as tk
from tkinter import ttk, messagebox

from simulator.patient_manual_input import PatientManualInput


class PatientManualScreen:
    def __init__(self, auto_close=True):
        self.auto_close = auto_close
        self.root = tk.Tk()
        self.root.title("Patient Manual - MedWatch")
        self.root.geometry("480x360")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        self._build_patient_tab()
        self._build_symptoms_tab()
        self._build_simulation_tab()

        # Action buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill='x', padx=10, pady=(0,10))

        self.submit_btn = tk.Button(btn_frame, text="Submit", command=self._on_submit)
        self.submit_btn.pack(side='right')

        self.cancel_btn = tk.Button(btn_frame, text="Cancel", command=self.root.destroy)
        self.cancel_btn.pack(side='right', padx=(0,8))

        # Storage for resulting PatientManualInput
        self.result: PatientManualInput | None = None

    def _build_patient_tab(self):
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text='Patient')

        tk.Label(frame, text='Name').grid(row=0, column=0, sticky='w', padx=6, pady=6)
        self.name_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1, sticky='ew', padx=6, pady=6)

        tk.Label(frame, text='Age').grid(row=1, column=0, sticky='w', padx=6, pady=6)
        self.age_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.age_var).grid(row=1, column=1, sticky='ew', padx=6, pady=6)

        tk.Label(frame, text='CPF').grid(row=2, column=0, sticky='w', padx=6, pady=6)
        self.id_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.id_var).grid(row=2, column=1, sticky='ew', padx=6, pady=6)

        tk.Label(frame, text='Phone').grid(row=3, column=0, sticky='w', padx=6, pady=6)
        self.phone_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.phone_var).grid(row=3, column=1, sticky='ew', padx=6, pady=6)

        frame.columnconfigure(1, weight=1)

    def _build_symptoms_tab(self):
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text='Conditions')

        tk.Label(frame, text='Add condition').grid(row=0, column=0, sticky='w', padx=6, pady=6)
        self.condition_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.condition_var).grid(row=0, column=1, sticky='ew', padx=6, pady=6)
        tk.Button(frame, text='Add', command=self._add_condition).grid(row=0, column=2, padx=6, pady=6)

        self.conditions_listbox = tk.Listbox(frame, height=8)
        self.conditions_listbox.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=6, pady=6)

        tk.Button(frame, text='Remove Selected', command=self._remove_condition).grid(row=2, column=2, sticky='e', padx=6, pady=6)

        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(1, weight=1)

    def _build_simulation_tab(self):
        frame = tk.Frame(self.notebook)
        self.notebook.add(frame, text='Simulation')

        tk.Label(frame, text='Parameter name').grid(row=0, column=0, sticky='w', padx=6, pady=6)
        self.sim_param_name = tk.StringVar()
        tk.Entry(frame, textvariable=self.sim_param_name).grid(row=0, column=1, sticky='ew', padx=6, pady=6)

        tk.Label(frame, text='Parameter value').grid(row=1, column=0, sticky='w', padx=6, pady=6)
        self.sim_param_value = tk.StringVar()
        tk.Entry(frame, textvariable=self.sim_param_value).grid(row=1, column=1, sticky='ew', padx=6, pady=6)

        frame.columnconfigure(1, weight=1)

    def _add_condition(self):
        cond = self.condition_var.get().strip()
        if not cond:
            return
        self.conditions_listbox.insert(tk.END, cond)
        self.condition_var.set('')

    def _remove_condition(self):
        sel = list(self.conditions_listbox.curselection())
        for idx in reversed(sel):
            self.conditions_listbox.delete(idx)

    def _validate(self) -> tuple[bool, str]:
        name = self.name_var.get().strip()
        age = self.age_var.get().strip()
        if not name:
            return False, 'Name is required.'
        if not age:
            return False, 'Age is required.'
        try:
            age_i = int(age)
            if age_i < 0 or age_i > 130:
                return False, 'Age must be between 0 and 130.'
        except ValueError:
            return False, 'Age must be a whole number.'
        return True, ''

    def _on_submit(self):
        ok, msg = self._validate()
        if not ok:
            messagebox.showerror('Validation error', msg)
            return

        name = self.name_var.get().strip()
        age = int(self.age_var.get().strip())
        pid = self.id_var.get().strip() or None
        conditions = [self.conditions_listbox.get(i) for i in range(self.conditions_listbox.size())]

        # Map to PatientManualInput
        self.result = PatientManualInput(name=name, age=age, patient_id=pid, conditions=conditions)
        print('Created patient:', self.result)

        # save to a JSON file in a safe location
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'private')
        try:
            os.makedirs(data_dir, exist_ok=True)
            filename = os.path.join(data_dir, f'patient_{pid or name}.json')
            self.result.save_to_json(filename)
            print('Saved patient file to', filename)
        except Exception as e:
            print('Warning: failed to save patient file:', e)

        if self.auto_close:
            self.root.destroy()

    def run(self):
        self.root.mainloop()

    @staticmethod
    def generate_screen():
        screen = PatientManualScreen()
        screen.run()
        return screen.result


if __name__ == '__main__':
    screen = PatientManualScreen()
    result = screen.generate_screen()
    print('Result:', result)
