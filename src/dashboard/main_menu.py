# @author: Brunno Ronaldo
# @created: 2026-08-04
# @last updated: 2026-08-09
# @version: 0.6.0

import tkinter as tk

choice = None

def main_menu_choice_next_window():
    global choice, root
    choice = None

    def automatic():
        global choice
        choice = "automatic"
        root.destroy()

    def manual():
        global choice
        choice = "manual"
        root.destroy()

    def exit_program():
        global choice
        choice = "exit"
        root.destroy()

    root = tk.Tk()
    root.title("MedWatch – Menu Principal")
    root.geometry("500x200")

    tk.Button(
        root,
        text="Simulador Automático",
        command=automatic
    ).pack(pady=10)

    tk.Button(
        root,
        text="Simulador Manual",
        command=manual
    ).pack(pady=10)

    tk.Button(
            root,
            text="Ajuda",
            command=manual
        ).pack(pady=10)

    tk.Button(
        root,
        text="Sair",
        command=exit_program
    ).pack(pady=10)

    root.mainloop()

    return choice