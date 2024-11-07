import tkinter as tk
from tkinter import messagebox
import sqlite3
from ttkbootstrap import Style
from PIL import ImageTk, Image

# Função para conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect('database/dados_alunos.db')

# Função para criar a tabela no banco de dados
def criar_tabela():
    conn = conectar_banco()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nota REAL NOT NULL,
            turma TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()

# Função para adicionar um aluno ao banco de dados
def adicionar_aluno():
    nome = entry_nome.get()
    try:
        nota = float(entry_nota.get())
    except ValueError:
        messagebox.showerror("Erro", "Nota inválida!")
        return
    turma = entry_turma.get()

    # Verificando se os dados são válidos
    if nome and 0 <= nota <= 10 and turma:
        conn = conectar_banco()
        c = conn.cursor()
        c.execute("INSERT INTO alunos (nome, nota, turma) VALUES (?, ?, ?)", 
                  (nome, nota, turma))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        # Limpar os campos após o cadastro
        entry_nome.delete(0, tk.END)
        entry_nota.delete(0, tk.END)
        entry_turma.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos corretamente!")

# Função para consultar e mostrar todos os alunos
def consultar_alunos():
    conn = conectar_banco()
    c = conn.cursor()
    c.execute("SELECT id, nome, nota, turma FROM alunos")
    alunos = c.fetchall()
    conn.close()

    # Limpar a lista de alunos
    listbox.delete(0, tk.END)

    if alunos:
        for aluno in alunos:
            listbox.insert(tk.END, f"ID: {aluno[0]} | Nome: {aluno[1]} | Nota: {aluno[2]} | Turma: {aluno[3]}")
    else:
        listbox.insert(tk.END, "Nenhum aluno cadastrado.")

# Função para buscar os dados de um aluno pelo ID
def buscar_aluno():
    aluno_id = entry_id.get()

    if not aluno_id.isdigit():
        messagebox.showerror("Erro", "Por favor, insira um ID válido.")
        return

    conn = conectar_banco()
    c = conn.cursor()
    c.execute("SELECT nome, nota, turma FROM alunos WHERE id=?", (aluno_id,))
    aluno = c.fetchone()
    conn.close()

    if aluno:
        entry_nome.delete(0, tk.END)
        entry_nota.delete(0, tk.END)
        entry_turma.delete(0, tk.END)

        entry_nome.insert(0, aluno[0])
        entry_nota.insert(0, aluno[1])
        entry_turma.insert(0, aluno[2])
    else:
        messagebox.showerror("Erro", f"Aluno com ID {aluno_id} não encontrado.")

# Função para atualizar os dados de um aluno
def atualizar_aluno():
    aluno_id = entry_id.get()
    nome = entry_nome.get()
    try:
        nota = float(entry_nota.get())
    except ValueError:
        messagebox.showerror("Erro", "Nota inválida! Por favor, insira um número entre 0 e 10.")
        return
    turma = entry_turma.get()

    # Verificando se os dados são válidos
    if not aluno_id.isdigit() or not nome or not (0 <= nota <= 10) or not turma:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos corretamente!\nA nota deve estar entre 0 e 10.")
        return

    conn = conectar_banco()
    c = conn.cursor()
    c.execute("UPDATE alunos SET nome=?, nota=?, turma=? WHERE id=?", (nome, nota, turma, aluno_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Cadastro atualizado com sucesso!")
    # Limpar os campos após a atualização
    entry_id.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_nota.delete(0, tk.END)
    entry_turma.delete(0, tk.END)

# Função para excluir um aluno
def excluir_aluno():
    aluno_id = entry_id.get()

    if not aluno_id.isdigit():
        messagebox.showerror("Erro", "Por favor, insira um ID válido.")
        return

    conn = conectar_banco()
    c = conn.cursor()
    c.execute("DELETE FROM alunos WHERE id=?", (aluno_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", f"Aluno com ID {aluno_id} excluído com sucesso!")
    # Limpar o campo ID após a exclusão
    entry_id.delete(0, tk.END)

style = Style(theme="superhero")  # Aplica o tema "superhero" do ttkbootstrap
root = style.master
root.title("Sistema de Gerenciamento de Alunos")
img = ImageTk.PhotoImage(file=r"icon\icon.png") #Adiciona um icone no topo da janela
root.iconphoto(False, img)

#Centralizar a janela no centro do display
x_app = 525
y_app = 515
x_screen = root.winfo_screenwidth()
y_screen = root.winfo_screenheight()
x = (x_screen / 2) - (x_app / 2)
y = (y_screen / 2) - (y_app / 2)
root.geometry(f"{x_app}x{y_app}+{int(x)}+{int(y)}")

#Adiciona uma logo na aplicação
logo = Image.open('icon/logo.png')
logo_img = ImageTk.PhotoImage(logo)
logo_place = tk.Label(root, image=logo_img)
logo_place.image = logo_img
logo_place.grid(row=0, column=1)

# Labels e campos de entrada
label_id = tk.Label(root, text="ID para excluir ou buscar")
label_id.grid(row=2, column=2, padx=10, pady=5)

entry_id = tk.Entry(root)
entry_id.grid(row=3, column=2, padx=10, pady=5)

label_nome = tk.Label(root, text="Nome do aluno:")
label_nome.grid(row=2, column=0, padx=10, pady=5)

entry_nome = tk.Entry(root)  # Usando ttk.Entry ao invés de tk.Entry
entry_nome.grid(row=2, column=1, padx=10, pady=5)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=3, column=0, padx=10, pady=5)

entry_nota = tk.Entry(root)  # Usando ttk.Entry ao invés de tk.Entry
entry_nota.grid(row=3, column=1, padx=10, pady=5)

label_turma = tk.Label(root, text="Turma:")
label_turma.grid(row=4, column=0, padx=10, pady=5)

entry_turma = tk.Entry(root)  # Usando ttk.Entry ao invés de tk.Entry
entry_turma.grid(row=4, column=1, padx=10, pady=5)

# Botões
botao_adicionar = tk.Button(root, text="Cadastrar Aluno", command=adicionar_aluno, width=15)
botao_adicionar.grid(row=5, column=0, padx=10, pady=5)

botao_consultar = tk.Button(root, text="Consultar Alunos", command=consultar_alunos, width=15)
botao_consultar.grid(row=5, column=1, padx=10, pady=5)

botao_buscar = tk.Button(root, text="Buscar Aluno", command=buscar_aluno, width=17)
botao_buscar.grid(row=6, column=2, padx=10, pady=5)

botao_atualizar = tk.Button(root, text="Atualizar Cadastro", command=atualizar_aluno, width=15)
botao_atualizar.grid(row=6, column=0, padx=10, pady=5)

botao_excluir = tk.Button(root, text="Excluir Aluno", command=excluir_aluno, width=17)
botao_excluir.grid(row=5, column=2, padx=10, pady=5)

# Listbox para exibir os alunos cadastrados
listbox = tk.Listbox(root, width=80, height=10)
listbox.grid(row=7, column=0, columnspan=3, padx=10, pady=5)

# Iniciar o loop da aplicação
root.mainloop()
