import tkinter as tk
from tkinter import messagebox
import pickle
import os

# Caminho para o arquivo onde os usuários serão armazenados
USER_DATA_FILE = "user_data.pkl"

# Função para carregar usuários do arquivo


def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'rb') as file:
            return pickle.load(file)
    return {}

# Função para salvar usuários no arquivo


def save_users():
    with open(USER_DATA_FILE, 'wb') as file:
        pickle.dump(users, file)


# Dicionário para armazenar usuários e senhas cadastrados
users = load_users()

# Função para registrar um novo usuário


def register_user():
    username = register_entry_username.get()
    password = register_entry_password.get()

    if username in users:
        messagebox.showwarning("Cadastro", "Usuário já existe!")
    else:
        users[username] = password
        save_users()  # Salva os dados após o cadastro
        messagebox.showinfo("Cadastro", "Usuário registrado com sucesso!")

# Função para validar o login


def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Entrando...")
        # Fechar a janela de login e abrir a nova janela (opcional)
        root.destroy()
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos!")

# Função para alternar entre tela de login e cadastro


def switch_to_register():
    login_frame.pack_forget()
    register_frame.pack(pady=20)


def switch_to_login():
    register_frame.pack_forget()
    login_frame.pack(pady=20)


# Criar a janela principal
root = tk.Tk()
root.title("Sistema de Login")

# Frame para login
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

label_username = tk.Label(login_frame, text="Usuário:")
label_username.pack(pady=5)

entry_username = tk.Entry(login_frame)
entry_username.pack(pady=5)

label_password = tk.Label(login_frame, text="Senha:")
label_password.pack(pady=5)

entry_password = tk.Entry(login_frame, show="*")
entry_password.pack(pady=5)

login_button = tk.Button(login_frame, text="Entrar", command=validate_login)
login_button.pack(pady=20)

register_link = tk.Button(login_frame, text="Cadastrar",
                          command=switch_to_register)
register_link.pack(pady=10)

# Frame para cadastro
register_frame = tk.Frame(root)

register_label_username = tk.Label(register_frame, text="Novo Usuário:")
register_label_username.pack(pady=5)

register_entry_username = tk.Entry(register_frame)
register_entry_username.pack(pady=5)

register_label_password = tk.Label(register_frame, text="Nova Senha:")
register_label_password.pack(pady=5)

register_entry_password = tk.Entry(register_frame, show="*")
register_entry_password.pack(pady=5)

register_button = tk.Button(
    register_frame, text="Cadastrar", command=register_user)
register_button.pack(pady=20)

back_to_login_link = tk.Button(
    register_frame, text="Voltar ao Login", command=switch_to_login)
back_to_login_link.pack(pady=10)

# Iniciar com a tela de login
login_frame.pack(pady=20)

# Iniciar o loop principal da interface
root.mainloop()
