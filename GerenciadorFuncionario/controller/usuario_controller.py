import tkinter as tk
from tkinter import messagebox

class UsuarioController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Inicializa a tela de login
        self.view.mostrar_tela_login(self.realizar_login, self.abrir_formulario_cadastro)

    def realizar_login(self):
        usuario = self.view.entry_usuario.get()
        senha = self.view.entry_senha.get()
        if self.model.autenticar_usuario(usuario, senha):
            messagebox.showinfo("Login", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def abrir_formulario_cadastro(self):
        self.view.mostrar_formulario_cadastro(self.salvar_usuario, self.voltar_para_login)

    def salvar_usuario(self, nome, idade, profissao, cidade, genero, email, senha, aceitou_termos):
        if not aceitou_termos:
            messagebox.showerror("Erro", "Você deve aceitar os Termos de Serviço.")
            return
        usuario = self.model.cadastrar_usuario(nome, idade, profissao, cidade, genero, email, senha)
        messagebox.showinfo("Sucesso", f"Usuário {usuario['nome']} cadastrado com sucesso!")
        self.voltar_para_login()

    def voltar_para_login(self):
        self.view.mostrar_tela_login(self.realizar_login, self.abrir_formulario_cadastro)
