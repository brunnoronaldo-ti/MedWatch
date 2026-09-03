# @author: Brunno Ronaldo
# Tela de Fila / Enfermaria - MedWatch
#
# Onde colocar: dentro da pasta dashboard/, do lado do register_patient_screen.py
# A pasta private/ é irmã de dashboard/ (as duas dentro de src/), então o caminho
# usa __file__ para subir um nível a partir de dashboard/ e achar private/.

import json
import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox

# Se o seu TriageEngine já existir, descomente e ajuste o import abaixo.
# from ia_engine.triage_engine import TriageEngine

class QueueScreen:
    """
    Mostra todos os pacientes cadastrados (lidos da pasta private/*.json),
    com a cor/prioridade da triagem e um status (aguardando / atendido).

    Não herda de RegisterPatientScreen de propósito: essa tela não cadastra
    ninguém, só lê e organiza quem já foi cadastrado.
    """

    STATUS_AGUARDANDO = "aguardando"
    STATUS_ATENDIDO = "atendido"

    def __init__(self, parent=None):
        # Se vier de outra tela Tkinter já aberta, usa Toplevel; senão, cria a raiz.
        self.root = tk.Toplevel(parent) if parent is not None else tk.Tk()
        self.root.title("Fila de Pacientes - MedWatch")
        self.root.geometry("640x420")

        self._build_toolbar()
        self._build_table()
        self.refresh()  # carrega os pacientes assim que a tela abre

    # ------------------------------------------------------------------
    # Localização dos arquivos
    # ------------------------------------------------------------------
    def _private_folder(self) -> Path:
        # dashboard/queue_screen.py -> parent = dashboard/ -> parent.parent = src/
        return Path(__file__).resolve().parent.parent / "private"

    # ------------------------------------------------------------------
    # UI
    # ------------------------------------------------------------------
    def _build_toolbar(self):
        bar = tk.Frame(self.root)
        bar.pack(fill='x', padx=10, pady=(10, 0))

        tk.Button(bar, text="Atualizar", command=self.refresh).pack(side='left')
        tk.Button(bar, text="Marcar como Atendido", command=self._mark_selected_attended).pack(side='left', padx=6)

        self.filtro_var = tk.StringVar(value="todos")
        tk.Label(bar, text="Mostrar:").pack(side='left', padx=(20, 4))
        ttk.Combobox(
            bar, textvariable=self.filtro_var, state='readonly', width=12,
            values=["todos", self.STATUS_AGUARDANDO, self.STATUS_ATENDIDO]
        ).pack(side='left')
        self.filtro_var.trace_add('write', lambda *_: self._populate_table())

    def _build_table(self):
        columns = ("nome", "idade", "condicoes", "triagem", "status")
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')

        headers = {
            "nome": "Nome", "idade": "Idade", "condicoes": "Condições",
            "triagem": "Triagem", "status": "Status",
        }
        widths = {"nome": 140, "idade": 50, "condicoes": 220, "triagem": 90, "status": 90}
        for col in columns:
            self.tree.heading(col, text=headers[col])
            self.tree.column(col, width=widths[col], anchor='w')

        self.tree.pack(fill='both', expand=True, padx=10, pady=10)

    # ------------------------------------------------------------------
    # Dados
    # ------------------------------------------------------------------
    def _load_patients(self):
        """Lê todos os JSONs da pasta private/ e devolve uma lista de dicts."""
        pasta = self._private_folder()
        pacientes = []

        if not pasta.exists():
            print(f"Aviso: pasta não encontrada: {pasta}")
            return pacientes

        for arquivo in sorted(pasta.glob("*.json")):
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
            except Exception as e:
                print(f"Aviso: falha ao ler {arquivo}: {e}")
                continue

            dados.setdefault("status", self.STATUS_AGUARDANDO)
            dados.setdefault("triagem", self._avaliar_triagem(dados))
            dados["_arquivo"] = str(arquivo)  # guarda o caminho pra poder regravar depois
            pacientes.append(dados)

        return pacientes

    def _avaliar_triagem(self, dados: dict) -> str:
        """
        Ponto de integração com o TriageEngine.
        Ajuste esta função para chamar TriageEngine.evaluate(...) de verdade
        assim que souber o formato exato que ele espera receber.
        """
        # Exemplo (ajuste os nomes de campo conforme seu PatientManualInput):
        # try:
        #     resultado = TriageEngine.evaluate(dados)
        #     return resultado.cor  # ou o que o seu evaluate() devolver
        # except Exception as e:
        #     print(f"Aviso: triagem falhou para {dados.get('name')}: {e}")
        #     return "não triado"
        return dados.get("triagem", "não triado")

    def _save_patient(self, dados: dict):
        """Regrava o JSON do paciente (usado ao mudar o status)."""
        arquivo = dados.get("_arquivo")
        if not arquivo:
            return
        to_save = {k: v for k, v in dados.items() if k != "_arquivo"}
        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(to_save, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Aviso: falha ao salvar {arquivo}: {e}")

    # ------------------------------------------------------------------
    # Ações
    # ------------------------------------------------------------------
    def refresh(self):
        self.pacientes = self._load_patients()
        self._populate_table()

    def _populate_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        filtro = self.filtro_var.get()
        for dados in self.pacientes:
            if filtro != "todos" and dados.get("status") != filtro:
                continue

            condicoes = dados.get("conditions", [])
            # conditions pode vir como lista de strings OU lista de dicts com "name"
            if condicoes and isinstance(condicoes[0], dict):
                condicoes_txt = ", ".join(c.get("name", "?") for c in condicoes)
            else:
                condicoes_txt = ", ".join(condicoes)

            self.tree.insert('', 'end', iid=dados["_arquivo"], values=(
                dados.get("name", "?"),
                dados.get("age", "?"),
                condicoes_txt,
                dados.get("triagem", "não triado"),
                dados.get("status", self.STATUS_AGUARDANDO),
            ))

    def _mark_selected_attended(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showinfo("Fila", "Selecione um paciente na tabela primeiro.")
            return

        arquivo = selecionado[0]
        dados = next((p for p in self.pacientes if p["_arquivo"] == arquivo), None)
        if dados is None:
            return

        dados["status"] = self.STATUS_ATENDIDO
        self._save_patient(dados)
        self._populate_table()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    QueueScreen().run()