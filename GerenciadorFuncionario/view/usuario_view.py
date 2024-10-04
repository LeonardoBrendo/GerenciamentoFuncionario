import tkinter as tk
from tkinter import messagebox

class UsuarioView:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela de Login")
        self.master.geometry(f"{self.master.winfo_screenwidth()}x{self.master.winfo_screenheight()}+0+0")
        
        self.entry_usuario = None
        self.entry_senha = None
        
    def mostrar_tela_login(self, realizar_login_callback, abrir_formulario_cadastro_callback):
        for widget in self.master.winfo_children():
            widget.destroy()
        
        # Recriação da tela de login
        label_bem_vindo = tk.Label(self.master, text="👋 Bem-vindo!", font=("Arial", 16, "bold"))
        label_bem_vindo.pack(pady=30)

        frame_login = tk.Frame(self.master, bd=2, relief="solid", padx=10, pady=10)
        frame_login.pack(pady=20, padx=20)

        # Entrada de usuário
        tk.Label(frame_login, text="Usuário:", font=("Arial", 13, "bold")).grid(row=0, column=0, padx=5, pady=(5, 2), sticky='w')
        self.entry_usuario = tk.Entry(frame_login, font=("Arial", 12))
        self.entry_usuario.grid(row=1, column=0, padx=5, pady=(2, 10))

        # Entrada de senha
        tk.Label(frame_login, text="Senha:", font=("Arial", 13, "bold")).grid(row=2, column=0, padx=5, pady=(5, 2), sticky='w')
        self.entry_senha = tk.Entry(frame_login, show="*", font=("Arial", 12))
        self.entry_senha.grid(row=3, column=0, padx=5, pady=(2, 10))

        # Botão de login
        botao_login = tk.Button(self.master, text="Login", command=realizar_login_callback, font=("Arial", 12))
        botao_login.pack(pady=20)

        # Link para criar nova conta
        link_cadastrar = tk.Button(self.master, text="Criar uma nova conta", command=abrir_formulario_cadastro_callback, font=("Arial", 10))
        link_cadastrar.pack(pady=10)

    def mostrar_formulario_cadastro(self, salvar_usuario_callback, voltar_login_callback):
        for widget in self.master.winfo_children():
            widget.destroy()
        
        label_cadastro = tk.Label(self.master, text="📝 Criar Nova Conta", font=("Arial", 16, "bold"))
        label_cadastro.pack(pady=10)
        
        # Frame para os campos de cadastro
        frame_cadastro = tk.Frame(self.master, bd=2, relief="solid", padx=10, pady=10)
        frame_cadastro.pack(pady=10, padx=20)

        # Campos do formulário
        tk.Label(frame_cadastro, text="Nome:", font=("Arial", 13, "bold")).grid(row=0, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_nome = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_nome.grid(row=1, column=0, padx=5, pady=(2, 5))

        tk.Label(frame_cadastro, text="Idade:", font=("Arial", 13, "bold")).grid(row=2, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_idade = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_idade.grid(row=3, column=0, padx=5, pady=(2, 5))

        tk.Label(frame_cadastro, text="Profissão:", font=("Arial", 13, "bold")).grid(row=4, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_profissao = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_profissao.grid(row=5, column=0, padx=5, pady=(2, 5))

        tk.Label(frame_cadastro, text="Cidade:", font=("Arial", 13, "bold")).grid(row=6, column=0, padx=5, pady=(2, 2), sticky='w')
        cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Brasília"]
        cidade_var = tk.StringVar()
        cidade_var.set(cidades[0])  
        optionmenu_cidades = tk.OptionMenu(frame_cadastro, cidade_var, *cidades)
        optionmenu_cidades.grid(row=7, column=0, padx=(0, 5), pady=(2, 5), sticky='w')

        # Gênero
        tk.Label(frame_cadastro, text="Gênero:", font=("Arial", 13, "bold")).grid(row=8, column=0, padx=5, pady=(2, 2), sticky='w')
        genero_var = tk.StringVar(value="Masculino")
        tk.Radiobutton(frame_cadastro, text="Masculino", variable=genero_var, value="Masculino").grid(row=9, column=0, padx=5, sticky='w')
        tk.Radiobutton(frame_cadastro, text="Feminino", variable=genero_var, value="Feminino").grid(row=10, column=0, padx=5, sticky='w')

        # Email e Senha
        tk.Label(frame_cadastro, text="Email:", font=("Arial", 13, "bold")).grid(row=11, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_email = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_email.grid(row=12, column=0, padx=5, pady=(2, 5))

        tk.Label(frame_cadastro, text="Senha:", font=("Arial", 13, "bold")).grid(row=13, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_senha_cadastro = tk.Entry(frame_cadastro, show="*", font=("Arial", 12))
        entry_senha_cadastro.grid(row=14, column=0, padx=5, pady=(2, 5))

        # CheckBox de termos
        check_termos_var = tk.BooleanVar()
        check_termos = tk.Checkbutton(frame_cadastro, text="Aceito os Termos de Serviço", variable=check_termos_var)
        check_termos.grid(row=15, columnspan=2, pady=5)

        # Botão para salvar usuário
        botao_salvar = tk.Button(frame_cadastro, text="Salvar", command=lambda: salvar_usuario_callback(entry_nome.get(), entry_idade.get(), entry_profissao.get(), cidade_var.get(), genero_var.get(), entry_email.get(), entry_senha_cadastro.get(), check_termos_var.get()), font=("Arial", 12))
        botao_salvar.grid(row=16, columnspan=2, pady=10)

        # Botão para voltar ao login
        botao_voltar = tk.Button(self.master, text="Voltar", command=voltar_login_callback, font=("Arial", 12))
        botao_voltar.pack(pady=10)
