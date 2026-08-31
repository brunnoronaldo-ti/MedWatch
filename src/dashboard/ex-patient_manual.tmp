# @author: Brunno Ronaldo
# @created: 2026-07-01
# @last updated: 2026-08-09
# @version: 0.6.0

# main.py (Seu Painel de Controle da Simulação)

import os  # <-- simple form to clear the screen/terminal
import keyboard  # <-- to capture key presses
import sys  # <-- to exit the program
import time # <-- to simulate time passing

from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.layout import Layout
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.live import Live

# Importa a sua classe
from simulator.patient_manual_input import PatientManualInput as pmi

console = Console()
class PatientManualScreen:
    @staticmethod
    def generate_layout(passo_atual: str, status: str, detalhes_paciente: str, progresso_componente) -> Layout:
        """Monta o painel visual dividido do hospital."""
        layout = Layout()
        layout.split(
            Layout(name="header", size=3),
            Layout(name="body")
        )
        layout["body"].split_row(
            Layout(name="esquerda", ratio=1),
            Layout(name="direita", ratio=1)
        )
        
        # Topo: Cabeçalho do Hospital
        layout["header"].update(Panel(Align("[bold red]🏥 SISTEMA INTEGRADO DE TRIAGEM E ATENDIMENTO HOSPITALAR[/]", align="center")))
        
        # Esquerda: Ficha do Paciente
        layout["esquerda"].update(Panel(detalhes_paciente, title="📄 Ficha Clínicas do Paciente", border_style="cyan"))
        
        # Direita: O que está acontecendo agora (Status + Animação de Carregamento)
        from rich.console import Group
        layout["direita"].update(Panel(
            Group(
                f"[bold yellow]Etapa atual:[/] {passo_atual}",
                f"[bold white]Status:[/] {status}\n",
                progresso_componente
            ),
            title="⚡ Status da Simulação", 
            border_style="green"
        ))
        return layout

    @staticmethod
    def generate_screen(generate_layout_func=generate_layout):
        """Gera a tela de triagem manual do paciente."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # =========================================================================
        # PASSO 1: CRIAR PACIENTES (Adiciona número de telefone, CPF, Idade, Nome)
        # =========================================================================
        console.print(Panel("[bold green]1. CADASTRO DE NOVO PACIENTE[/]", expand=False))
        
        name = Prompt.ask("[bold]Nome do Paciente[/]").capitalize()
        age = IntPrompt.ask("[bold]Idade do Paciente[/]")
        cpf = Prompt.ask("[bold]CPF do Paciente[/] (xxx.xxx.xxx-xx)")
        phone = Prompt.ask("[bold]Telefone de Contato[/] ((xx) xxxxx-xxxx)")
        
        # Geramos um ID automático misturando o CPF para sua classe não quebrar
        patient_id = f"PAC-{cpf.replace('.', '').replace('-', '')[:4]}"

        # =========================================================================
        # PASSO 2: ADICIONAR OS SINTOMAS (Exibe uma lista de opções e deixa o usuário escolher)
        # =========================================================================
        print("\n")
        biblioteca_doencas = pmi.load_diseases()
        
        tabela_doencas = Table(title="Selecione os Sintomas/Condições na Lista Abaixo", border_style="magenta")
        tabela_doencas.add_column("Opções Disponíveis", style="bold white")
        for cond in biblioteca_doencas:
            tabela_doencas.add_row(cond)
        console.print(tabela_doencas, "\n")

        patient_manual_conditions = []
        while True:
            condition = Prompt.ask("[bold yellow]Escolha uma condição da lista[/] (ou digite 'done'/'feito' para avançar)")
            
            if condition.lower() in ['done', 'feito']:
                if not patient_manual_conditions:
                    console.print("[red]Adicione pelo menos uma condição para triagem![/]")
                    continue
                break
                
            condition_lower = condition.lower()
            if condition_lower in biblioteca_doencas:
                info = biblioteca_doencas[condition_lower]
                patient_manual_conditions.append({
                    "name": condition,
                    "severity": info.get("severity", "moderate"),
                    "duration": info.get("duration", "long-term"),
                    "description": info.get("description", "Sintoma selecionado da biblioteca.")
                })
                console.print(f"[green]✓ '{condition}' adicionada ao prontuário.[/]\n")
            else:
                console.print(f"[bold red]Aviso:[/] '{condition}' não está na biblioteca.")
                confirm = Prompt.ask("Deseja adicionar mesmo assim?", choices=["yes", "no"], default="yes")
                
                if confirm == "no":
                    console.print("[yellow]Condição descartada. Tente novamente.[/]\n")
                    continue
                    
                console.print(f"[bold blue]Adicionando '{condition}'. Por favor, dê mais detalhes:[/]")
                severity = Prompt.ask("Gravidade", choices=["mild", "moderate", "severe"])
                duration = Prompt.ask("Duração", choices=["short-term", "long-term"])
                description = Prompt.ask("Descrição da condição")
                print()


        # Criamos o objeto final com a sua classe do seu arquivo original
        paciente = pmi(name=name, age=age, patient_id=patient_id, conditions=patient_manual_conditions)

        # String formatada que vai alimentar o nosso layout dinâmico nas próximas etapas
        ficha_paciente_texto = (
            f"[bold cyan]Nome:[/] {paciente.name}\n"
            f"[bold cyan]Idade:[/] {paciente.age} anos\n"
            f"[bold cyan]CPF:[/] {cpf}\n"
            f"[bold cyan]Telefone:[/] {phone}\n"
            f"[bold cyan]ID Prontuário:[/] {paciente.patient_id}\n\n"
            f"[bold magenta]Sintomas Relatados:[/]\n" + 
            "\n".join([f" • {c['name'].upper()} ({c['severity']})" for c in paciente.conditions])
        )

        # =========================================================================
        # CONFIGURAÇÃO DO MODO VISUAL EM TEMPO REAL (O "Enrolador Profissional")
        # =========================================================================
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Barra de progresso animada com o "Spinner" (ícone giratório) do Rich
        progresso_visual = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn()
        )
        
        tarefa_id = progresso_visual.add_task("[cyan]Iniciando motores...", total=100)

        # Variáveis de controle para o layout saber o que escrever na tela
        etapa = "Preparando Triagem"
        status_texto = "Aguardando fila de atendimento..."

        # O "with Live" congela a tela do terminal e atualiza o layout 10 vezes por segundo
        with Live(generate_layout_func(etapa, status_texto, ficha_paciente_texto, progresso_visual), refresh_per_second=10, screen=True) as live:
            
            # ---------------------------------------------------------------------
            # PASSO 3: INICIA A TRIAGEM (Triagem automática)
            # ---------------------------------------------------------------------
            etapa = "3. Triagem Automática"
            status_texto = "Analisando dados vitais e sintomas inseridos no sistema..."
            
            # Aqui simulamos o tempo passando enquanto a barra enche de 0 a 30
            for p in range(0, 31):
                progresso_visual.update(tarefa_id, completed=p, description="[bold yellow]Processando algoritmo de Triagem...[/]")
                live.update(generate_layout_func(etapa, status_texto, ficha_paciente_texto, progresso_visual))
                time.sleep(0.08) # Dá a falsa sensação de cálculo pesado
                
            # [AQUI ENCAIXA A FUNÇÃO REAL DE TRIAGEM]
            
            status_texto = "Triagem concluída! Paciente classificado com sucesso."
            time.sleep(1.5)

            # ---------------------------------------------------------------------
            # PASSO 4: O ENFERMEIRO FAZ SEU TRABALHO
            # ---------------------------------------------------------------------
            etapa = "4. Atendimento de Enfermagem"
            status_texto = "Enfermeiro de plantão assumiu o caso. Verificando acessos e medicamentos preliminares..."
            
            # Enche a barra de 30 a 60
            for p in range(30, 61):
                progresso_visual.update(tarefa_id, completed=p, description="[bold blue]Enfermeiro executando procedimentos...[/]")
                live.update(generate_layout_func(etapa, status_texto, ficha_paciente_texto, progresso_visual))
                time.sleep(0.08)
                
            # [AQUIENCAIXA A LOGICA DE ENFERMEIROS REAL]
            # Exemplo: enfermeiro_trabalhar(paciente)
            status_texto = "Procedimentos de enfermagem finalizados. Encaminhando ao consultório médico."
            time.sleep(1.5)

            # ---------------------------------------------------------------------
            # PASSO 5: O MÉDICO FAZ SEU TRABALHO
            # ---------------------------------------------------------------------
            etapa = "5. Consulta Médica e Diagnóstico"
            status_texto = "Médico especialista analisando o prontuário e prescrevendo o tratamento final..."
            
            # Enche a barra de 60 a 95
            for p in range(60, 96):
                progresso_visual.update(tarefa_id, completed=p, description="[bold magenta]Médico prescrevendo tratamento...[/]")
                live.update(generate_layout_func(etapa, status_texto, ficha_paciente_texto, progresso_visual))
                time.sleep(0.1) # Um pouco mais lento porque médico "pensa" mais kkk
                
            # [AQUI ENCAIXA A LÓGICA DE MÉDICOS REAL]
            status_texto = "Diagnóstico concluído! Prescrição médica carimbada."
            time.sleep(1.5)

            # ---------------------------------------------------------------------
            # PASSO 6: USUÁRIO TRATADO. FINALIZA A SIMULAÇÃO
            # ---------------------------------------------------------------------
            etapa = "6. Alta Médica"
            status_texto = "Paciente recuperado, orientado e liberado pelo hospital."
            progresso_visual.update(tarefa_id, completed=100, description="[bold green]Simulação Concluída com Sucesso![/]")
            live.update(generate_layout_func(etapa, status_texto, ficha_paciente_texto, progresso_visual))
            time.sleep(3.0) # Segura a tela cheia por 3 segundos pro professor ver o sucesso

        # Salva o arquivo final usando sua função original
        paciente.save_to_json("registro_simulacao.json")
        
        print("\n")
        console.print(Panel("[bold green]✓ PROCESSO HOSPITALAR CONCLUÍDO![/]\nO prontuário final foi exportado.", expand=False))

        evento = keyboard.read_event()
        while evento.event_type != keyboard.KEY_DOWN or evento.name not in ['enter', 'esc']:
            evento = keyboard.read_event()
        
        if evento.name == 'esc':
            console.print("[red]Fechando o programa...[/red]")
            sys.exit()  # Fecha o programa imediatamente  