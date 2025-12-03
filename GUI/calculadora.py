import tkinter as tk
import math
import re

def digitar(valor):
    entrada.insert(tk.END, valor)

def limpar(event=None):
    entrada.delete(0, tk.END)

def calcular(event=None):
    expressao = entrada.get()
    try:
        expressao = (expressao.replace("÷", "/")
                               .replace("×", "*")
                               .replace("^", "**")
                               .replace("π", str(math.pi)))

        expressao = re.sub(r"√(\d+(?:\.\d+)?)", r"math.sqrt(\1)", expressao)
        expressao = re.sub(r"√\(([^)]+)\)", r"math.sqrt(\1)", expressao)

        def percent_addsub(m):
            a, op, b = m.group(1), m.group(2), m.group(3)
            return f"({a}{op}({a}*({b}/100)))"
        expressao = re.sub(r"(\d+(?:\.\d+)?)\s*([+\-])\s*(\d+(?:\.\d+)?)%", percent_addsub, expressao)

        expressao = re.sub(r'(?<=\d|\))%', r'/100', expressao)

        resultado = eval(expressao, {"__builtins__": None}, {"math": math})
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

def teclado(event):
    tecla = event.char
    if tecla.isdigit() or tecla in ".()":
        digitar(tecla)
    elif tecla == "+":
        digitar("+")
    elif tecla == "-":
        digitar("-")
    elif tecla == "*":
        digitar("×")  
    elif tecla == "/":
        digitar("÷")
    elif tecla in ["^", "%"]:
        digitar(tecla)
    elif tecla == "p":  
        digitar("π")
    elif tecla == "r": 
        digitar("√")

root = tk.Tk()
root.title("Calculadora")

root.minsize(300, 400)
root.maxsize(500, 650)

largura_max = 500
altura_max = 650
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

pos_x = (largura_tela // 2) - (largura_max // 2)
pos_y = (altura_tela // 2) - (altura_max // 2)

root.geometry(f"{largura_max}x{altura_max}+{pos_x}+{pos_y}")
root.configure(bg="#1e1e2f") 

entrada = tk.Entry(
    root, font=("Arial", 20),
    borderwidth=5, relief="flat",
    justify="right", bg="#121212", fg="#f8f8f2"
)
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

botoes = [
    ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), ("x²", 5, 1), ("%", 5, 2), ("√", 5, 3),
    (".", 6, 0), ("π", 6, 1), ("=", 6, 2, 2)
]

estilo_num = {"bg": "#3c3f41", "fg": "#f5f3f3"}
estilo_op = {"bg": "#2e3133", "fg": "#f5f3f3"}     
estilo_esp = {"bg": "#44475a", "fg": "#f5f3f3"}   
estilo_calc = {"bg": "#fd6039", "fg": "#F5F3F3"}   

for item in botoes:
    if len(item) == 3:
        texto, linha, coluna = item
        colspan = 1
    else:
        texto, linha, coluna, colspan = item

    if texto == "C":
        cmd = limpar
        style = estilo_esp
    elif texto == "=":
        cmd = calcular
        style = estilo_calc
    elif texto == "x²":
        cmd = lambda: digitar("**2")
        style = estilo_op
    else:
        cmd = lambda t=texto: digitar(t)
        style = estilo_op if texto in ["+", "-", "*", "×", "÷", "^", "%", "√", "(", ")"] else estilo_num

    botao = tk.Button(
        root, text=texto, font=("Arial", 14, "bold"),
        command=cmd, relief="flat", **style
    )
    botao.grid(row=linha, column=coluna, columnspan=colspan,
               padx=3, pady=3, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)

root.bind("<Return>", calcular)   
root.bind("<KP_Enter>", calcular)
root.bind("<Escape>", limpar)     
root.bind("<BackSpace>", lambda e: entrada.delete(len(entrada.get())-1, tk.END)) 
root.bind("<Key>", teclado)      

root.mainloop()