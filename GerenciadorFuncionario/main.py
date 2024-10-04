import tkinter as tk
from view.usuario_view import UsuarioView
from controller.usuario_controller import UsuarioController
from tkinter import messagebox


def realizar_login_callback():
    email = usuario_view.entry_usuario.get()
    senha = usuario_view.entry_senha.get()
    if usuario_controller.realizar_login(email, senha):
        # Ações a serem realizadas após o login bem-sucedido
        print("Login bem-sucedido!")
    else:
        # Exibir mensagem de erro
        messagebox.showerror("Erro", "Email ou senha incorretos.")

def main():
    root = tk.Tk()
    usuario_controller = UsuarioController()
    usuario_view = UsuarioView(root, usuario_controller)
    usuario_view.mostrar_tela_login(realizar_login_callback, usuario_view.mostrar_formulario_cadastro)

    root.mainloop()
    usuario_controller.fechar_conexao()  # Fechar a conexão com o banco ao sair

if __name__ == "__main__":
    main()
