# @author: Brunno Ronaldo
# @created: 2026-08-30
# @last updated: 2026-08-30
# @version: 0.7.0

import tkinter as tk

class HelpScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ajuda - MedWatch")
        self.root.geometry("600x400")

        help_text = (
            "Bem-vindo ao MedWatch!\n\n"
            "Este é um simulador de hospital que permite testar diferentes cenários de atendimento.\n\n"
            "Opções disponíveis:\n"
            "- Simulador Automático: Gera pacientes automaticamente e simula o atendimento.\n"
            "- Simulador Manual: Permite inserir pacientes manualmente e simular o atendimento.\n"
            "- Ajuda: Exibe esta tela de ajuda.\n"
            "- Sair: Fecha o programa.\n\n"
            "Para mais informações, consulte a documentação do MedWatch ou visite o nosso GitHub."
        )

        label = tk.Label(self.root, text=help_text, justify='left', padx=10, pady=10)
        label.pack(fill='both', expand=True)

        close_button = tk.Button(self.root, text="Fechar", command=self.root.destroy)
        close_button.pack(pady=10)

    def show(self):
        self.root.mainloop()