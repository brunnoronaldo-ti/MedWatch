import tkinter as tk

def popup_confirmation():
    popup = tk.Toplevel()
    popup.title("Confirmação")
    popup.geometry("300x100")

    result = {"value": None}

    label = tk.Label(popup, text="Deseja realmente sair?")
    label.pack(pady=10)

    def on_yes():
        result["value"] = True
        popup.destroy()

    def on_no():
        result["value"] = False
        popup.destroy()

    button_yes = tk.Button(popup, text="Sim", command=on_yes)
    button_yes.pack(side=tk.LEFT, padx=20)

    button_no = tk.Button(popup, text="Não", command=on_no)
    button_no.pack(side=tk.RIGHT, padx=20)

    popup.grab_set()
    popup.wait_window()
    return result["value"]

def choose_option_menu(button1, button2, button3):
    if button1.cget("relief") == "sunken":
        print("Simulador Automático selecionado")
        if popup_confirmation(): #Corrigir o retorno aqui!
            return "automatic"
        return choose_option_menu(button1, button2, button3)  # Reopen the menu if the user cancels

    elif button2.cget("relief") == "sunken":
        print("Simulador Manual selecionado")
        if popup_confirmation():
            return "manual"
        return choose_option_menu(button1, button2, button3)  # Reopen the menu if the user cancels

    elif button3.cget("relief") == "sunken":
        print("Sair selecionado")
        if popup_confirmation():
            return "exit"
        return choose_option_menu(button1, button2, button3)  # Reopen the menu if the user cancels

    else:
        print("Nenhuma opção selecionada/Opção inexistente")
        return None

# Window setup
interface_menu = tk.Tk()
interface_menu.title("Menu Principal")
interface_menu.geometry("500x150")

interface_menu.grid_columnconfigure(0, weight=1)
interface_menu.grid_columnconfigure(1, weight=1)
interface_menu.grid_columnconfigure(2, weight=1)

# The argument sticky="nsew" defines that the button should expand in all directions (north, south, east, west) to fill the cell in the grid. This makes the buttons resize with the window.
button1 = tk.Button(interface_menu, text="Simulador Automático")
button1.grid(row=1, column=0, pady=20, padx=5, sticky="nsew")

button2 = tk.Button(interface_menu, text="Simulador Manual")
button2.grid(row=1, column=2, pady=20, padx=5, sticky="nsew")

button3 = tk.Button(interface_menu, text="Sair")
button3.grid(row=2, column=1, pady=20, padx=5, sticky="nsew")

# Execute the main loop (That keeps the window open and responsive to user interactions)
interface_menu.mainloop()# This line should be at the end