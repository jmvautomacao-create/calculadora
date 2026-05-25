import tkinter as tk
from tkinter import messagebox
import math

# =========================
# CONFIGURAÇÃO DA JANELA
# =========================
janela = tk.Tk()
janela.title("Calculadora Do Jean")
janela.geometry("430x690")
janela.resizable(False, False)
janela.configure(bg="#535151")

# =========================
# VARIÁVEIS
# =========================
expressao = ""
memoria = 0

# =========================
# DISPLAY
# =========================
display = tk.Entry(
    janela,
    font=("Consolas", 24),
    bd=10,
    relief=tk.FLAT,
    justify="right",
    bg="#353333",
    fg="white"
)

display.pack(fill="both", padx=10, pady=10, ipady=15)

# =========================
# FUNÇÕES
# =========================
def atualizar_display(valor):
    global expressao
    expressao += str(valor)
    display.delete(0, tk.END)
    display.insert(tk.END, expressao)

def limpar():
    global expressao
    expressao = ""
    display.delete(0, tk.END)

def apagar2():
        global expressao
        expressao = expressao[:-1]
        display.delete(0, tk.END)
        display.insert(0, expressao)

def calcular():
    global expressao

    try:
        expr = expressao.replace(" ", "")

        # =========================
        # TRATAMENTO DE PORCENTAGEM
        # =========================
        if "%" in expr:

            # Soma e subtração
            if "+" in expr:
                partes = expr.split("+")
                base = float(partes[0])
                porcento = float(partes[1].replace("%", ""))

                resultado = base + (base * porcento / 100)

            elif "-" in expr:
                partes = expr.split("-")
                base = float(partes[0])
                porcento = float(partes[1].replace("%", ""))

                resultado = base - (base * porcento / 100)

            # Multiplicação
            elif "*" in expr:
                partes = expr.split("*")
                base = float(partes[0])
                porcento = float(partes[1].replace("%", ""))

                resultado = base * (porcento / 100)

            # Divisão
            elif "/" in expr:
                partes = expr.split("/")
                base = float(partes[0])
                porcento = float(partes[1].replace("%", ""))

                resultado = base / (porcento / 100)

            else:
                resultado = eval(expr.replace("%", "/100"))

        else:
            resultado = eval(expr)

        # Mostrar resultado
        display.delete(0, tk.END)
        display.insert(tk.END, resultado)

        expressao = str(resultado)

    except:
        messagebox.showerror("Erro", "Expressão inválida")
        limpar()
    

# =========================
# FUNÇÕES CIENTÍFICAS
# =========================
def funcao_matematica(func):
    global expressao

    try:
        valor = float(display.get())

        if func == "sqrt":
            resultado = math.sqrt(valor)

        elif func == "sin":
            resultado = math.sin(math.radians(valor))

        elif func == "cos":
            resultado = math.cos(math.radians(valor))

        elif func == "tan":
            resultado = math.tan(math.radians(valor))

        elif func == "log":
            resultado = math.log10(valor)

        elif func == "ln":
            resultado = math.log(valor)

        elif func == "x²":
            resultado = valor ** 2

        elif func == "1/x":
            resultado = 1 / valor

        elif func == "π":
            resultado = 3.141592653589793

        elif func == "e":
            resultado = math.e

        display.delete(0, tk.END)
        display.insert(tk.END, resultado)
        expressao = str(resultado)

        
    except:
        messagebox.showerror("Erro", "Operação inválida")

# =========================
# MEMÓRIA
# =========================
def memoria_salvar():
    global memoria
    try:
        memoria = float(display.get())
    except:
        pass

def memoria_somar():
    global memoria
    try:
        memoria += float(display.get())
    except:
        pass

def memoria_subtrair():
    global memoria
    try:
        memoria -= float(display.get())
    except:
        pass

def memoria_recuperar():
    atualizar_display(memoria)

def memoria_limpar():
    global memoria
    memoria = 0

# =========================
# ESTILO DOS BOTÕES
# =========================
fonte = ("Arial", 16, "bold")

cores = {
    "numero": "#E22911",
    "operador": "#00FF22",
    "cientifica": "#005BBB",
    "memoria": "#9A1B94",
    "controle": "#2C3235"
}

# =========================
# FRAME DOS BOTÕES
# =========================
frame = tk.Frame(janela, bg="#BBB2B2")
frame.pack()

# =========================
# LISTA DE BOTÕES
# =========================
botoes = [

    # Memória
    ("MC", 0, 0, cores["memoria"], memoria_limpar),
    ("MR", 0, 1, cores["memoria"], memoria_recuperar),
    ("M+", 0, 2, cores["memoria"], memoria_somar),
    ("M-", 0, 3, cores["memoria"], memoria_subtrair),
    ("MS", 0, 4, cores["memoria"], memoria_salvar),

    # Científicos
    ("sin", 1, 0, cores["cientifica"], lambda: funcao_matematica("sin")),
    ("cos", 1, 1, cores["cientifica"], lambda: funcao_matematica("cos")),
    ("tan", 1, 2, cores["cientifica"], lambda: funcao_matematica("tan")),
    ("√",   1, 3, cores["cientifica"], lambda: funcao_matematica("sqrt")),
    ("x²",  1, 4, cores["cientifica"], lambda: funcao_matematica("x²")),

    ("log", 2, 0, cores["cientifica"], lambda: funcao_matematica("log")),
    ("ln",  2, 1, cores["cientifica"], lambda: funcao_matematica("ln")),
    ("π",   2, 2, cores["cientifica"], lambda: funcao_matematica("π")),
    ("e",   2, 3, cores["cientifica"], lambda: funcao_matematica("e")),
    ("1/x", 2, 4, cores["cientifica"], lambda: funcao_matematica("1/x")),

    # Controle
    ("C", 3, 0, cores["controle"], limpar),
    ("(", 3, 1, cores["operador"], lambda: atualizar_display("(")),
    (")", 3, 2, cores["operador"], lambda: atualizar_display(")")),
    ("/", 3, 3, cores["operador"], lambda: atualizar_display("/")),
    ("*", 4, 3, cores["operador"], lambda: atualizar_display("*")),

    # Números
    ("7", 4, 0, cores["numero"], lambda: atualizar_display("7")),
    ("8", 4, 1, cores["numero"], lambda: atualizar_display("8")),
    ("9", 4, 2, cores["numero"], lambda: atualizar_display("9")),
    ("-", 5, 3, cores["operador"], lambda: atualizar_display("-")),
    ("%", 4, 4, cores["operador"], lambda: atualizar_display("%")),

    ("4", 5, 0, cores["numero"], lambda: atualizar_display("4")),
    ("5", 5, 1, cores["numero"], lambda: atualizar_display("5")),
    ("6", 5, 2, cores["numero"], lambda: atualizar_display("6")),
    ("+", 6, 3, cores["operador"], lambda: atualizar_display("+")),

    ("1", 6, 0, cores["numero"], lambda: atualizar_display("1")),
    ("2", 6, 1, cores["numero"], lambda: atualizar_display("2")),
    ("3", 6, 2, cores["numero"], lambda: atualizar_display("3")),
    ("=", 7, 2, cores["operador"], calcular),

    ("0", 7, 0, cores["numero"], lambda: atualizar_display("0")),
    (".", 7, 1, cores["numero"], lambda: atualizar_display(".")),
    ("BACK", 3, 4, cores["controle"],  apagar2),
]

# =========================
# CRIAÇÃO DOS BOTÕES
# =========================
for (texto, linha, coluna, cor, comando) in botoes:

    largura = 5
    altura = 2

    # Botão "=" maior
    if texto == "=":
        largura = 7
        colspan = 1
    else:
        largura = 5
        colspan = 1

    # Botão "0" maior
    if texto == "+":
        largura = 5
        colspan = 1
    
    # Botão "Back" maior
    if texto == "BACK":
        largura = 5
        colspan = 2
    else:
        colspan = 1     

    botao = tk.Button(
        frame,
        text=texto,
        width=largura,
        height=altura,
        font=fonte,
        bg=cor,
        fg="white",
        activebackground="#AAAAAA",
        relief=tk.FLAT,
        command=comando
    )

    botao.grid(
        row=linha,
        column=coluna,
        columnspan=colspan,
        padx=3,
        pady=3,
        sticky="nsew"
    )

# =========================
# TECLADO
# =========================
def teclado(event):
    tecla = event.keysym

    if tecla in "0123456789":
        atualizar_display(tecla)

    elif tecla in ["plus", "KP_Add"]:
        atualizar_display("+")

    elif tecla in ["minus", "KP_Subtract"]:
        atualizar_display("-")

    elif tecla in ["asterisk", "KP_Multiply"]:
        atualizar_display("*")

    elif tecla in ["slash", "KP_Divide"]:
        atualizar_display("/")

    elif tecla == "Return":
        calcular()

    elif tecla == "period":
        atualizar_display(".")

    elif tecla == "BackSpace":
        global expressao
        expressao = expressao[:-1]
        display.delete(0, tk.END)
        display.insert(0, expressao)

    elif tecla == "Escape":
        limpar()

janela.bind("<Key>", teclado)

# =========================
# LOOP
# =========================
janela.mainloop()