import tkinter as tk

botoes_numeros = [(1, 30, 270), (2, 90, 270), (3, 150, 270), (4, 30, 210), (5, 90, 210), (6, 150, 210), (7, 30, 150), (8, 90, 150), (9, 150, 150), (0, 30, 330)]
botoes_operadores = [("/", 210, 150), ("*", 210, 210), ("-", 210, 270), ("+", 210, 330), ("=", 150, 330), ("C", 90, 330)]
calculo = str()

# Funções.
def adicionar_numero(numero: str):
    global calculo
    calculo += numero
    texto_calculo.config(text=calculo)

def adicionar_operador(operador: str):
    global calculo
    calculo += operador
    texto_calculo.config(text=calculo)

def calcular():
    global calculo
    try:
        resultado = round(eval(calculo), 2)
    except Exception:
        resultado = "Erro"
    texto_resultado.config(text=resultado)

def limpar():
    global calculo
    calculo = ""
    texto_calculo.config(text="")
    texto_resultado .config(text="")

# Configuração da Janela.
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("290x410")
janela.resizable(False, False)
janela.configure(background="#292c30")

# Frame da Tela.
tela = tk.Frame(janela, background="#323538", relief="flat")
tela.place(x=30, y=30, width=230, height=100)

# Texto do Calculo.
texto_calculo = tk.Label(tela, text="", font=("Inter", 12, "bold"), foreground="#767b80", background="#323538", anchor="e")
texto_calculo.place(x=20, y=20, width=200)

# Texto do Resultado.
texto_resultado = tk.Label(tela, text="", font=("Inter", 20, "bold"), foreground="#ffffff", background="#323538", anchor="e")
texto_resultado.place(x=20, y=50, width=200)

# Loop Numeros.
for (numero, x, y) in botoes_numeros:
    botao = tk.Button(janela, text=f"{numero}", font=("Inter", 10, "normal"), background="#323538", foreground="#ffffff", relief="flat", highlightthickness=0, command=lambda num=numero: adicionar_numero(f"{num}"))
    botao.place(x=x, y=y, width=50, height=50)

# Loop Operadores.
for (operador, x, y) in botoes_operadores:
    botao = tk.Button(janela, text=f"{operador}", font=("Inter", 10, "normal"), background="#30ad6b", foreground="#ffffff", relief="flat", highlightthickness=0)
    if operador == "=":
        botao.config(command=calcular)
    elif operador == "C":
        botao.config(command=limpar, background="#ee6055")
    else:
        botao.config(command=lambda ope=operador: adicionar_operador(f" {ope} "))
    botao.place(x=x, y=y, width=50, height=50)

# Mainloop.
janela.mainloop()