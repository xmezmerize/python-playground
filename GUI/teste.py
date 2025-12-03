import tkinter as tk

# ======================
# Função de callback
# ======================
def mostrar_nome():
    nome = entrada.get()
    resultado.config(text=f"Parabéns, {nome}!")

# ======================
# Janela principal
# ======================
janela = tk.Tk()
janela.title("Estudo GUI")
janela.geometry("600x500")

# ======================
# Widgets com grid
# ======================
# Label inicial
label = tk.Label(janela, text="Digite seu nome!")
label.grid(row=0, column=0, columnspan=2, pady=10)

# Entrada do nome
entrada = tk.Entry(janela)
entrada.grid(row=1, column=0, columnspan=2, pady=5)

# Resultado
resultado = tk.Label(janela, text="")
resultado.grid(row=2, column=0, columnspan=2, pady=5)

# Campos de login
login = tk.Label(janela, text="Usuário:")
login.grid(row=3, column=0, sticky="e")
login_entrada = tk.Entry(janela)
login_entrada.grid(row=3, column=1, pady=5)

senha = tk.Label(janela, text="Senha:")
senha.grid(row=4, column=0, sticky="e")
senha_entrada = tk.Entry(janela, show="*")
senha_entrada.grid(row=4, column=1, pady=5)

# Botão principal
botao = tk.Button(janela, text="Clique aqui", command=mostrar_nome)
botao.grid(row=5, column=0, columnspan=2, pady=10)

# ======================
# Frame com botões extras
# ======================
frame = tk.Frame(janela, bg="lightgray", padx=10, pady=10)
frame.grid(row=6, column=0, columnspan=2, pady=10)

tk.Button(frame, text="Botão 1").pack(side="left", padx=5)
tk.Button(frame, text="Botão 2").pack(side="left", padx=5)

# ======================
# Menu
# ======================
menu_bar = tk.Menu(janela)
janela.config(menu=menu_bar)

menu_arquivo = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Novo")
menu_arquivo.add_command(label="Sair", command=janela.quit)

# ======================
# Loop principal
# ======================
janela.mainloop()