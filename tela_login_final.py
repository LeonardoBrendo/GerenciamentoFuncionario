import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'postgresql://postgres:77leonardo77@localhost/senac'
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    profissao = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    aceita_termos = Column(Boolean, nullable=False)

Base.metadata.create_all(engine)

class AplicativoLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela de Login")

        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()

        self.master.geometry(f"{largura_tela}x{altura_tela}+0+0")

        self.entry_usuario = None
        self.entry_senha = None

        self.voltar_login()

    def realizar_login(self):
        usuario_email = self.entry_usuario.get()
        senha = self.entry_senha.get()

        usuario = session.query(Usuario).filter_by(email=usuario_email, senha=senha).first()
        if usuario:
            messagebox.showinfo("Login", f"Bem-vindo, {usuario.nome}!")
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos.")

    def abrir_formulario_cadastro(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        label_cadastro = tk.Label(self.master, text="📝 Criar Nova Conta", font=("Arial", 16, "bold"))
        label_cadastro.pack(pady=1)

        frame_cadastro = tk.Frame(self.master, bd=2, relief="solid", padx=10, pady=10)
        frame_cadastro.pack(pady=20, padx=20)

        tk.Label(frame_cadastro, text="Nome:", font=("Arial", 13, "bold")).grid(row=0, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_nome = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_nome.grid(row=1, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_cadastro, text="Idade:", font=("Arial", 13, "bold")).grid(row=2, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_idade = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_idade.grid(row=3, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_cadastro, text="Profissão:", font=("Arial", 13, "bold")).grid(row=4, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_profissao = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_profissao.grid(row=5, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_cadastro, text="Cidade:", font=("Arial", 13, "bold")).grid(row=6, column=0, padx=5, pady=(2, 2), sticky='w')
        cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Brasília"]
        cidade_var = tk.StringVar()
        cidade_var.set(cidades[0])  
        optionmenu_cidades = tk.OptionMenu(frame_cadastro, cidade_var, *cidades)
        optionmenu_cidades.grid(row=7, column=0, padx=(0, 5), pady=(2, 10), sticky='w')

        tk.Label(frame_cadastro, text="Gênero:", font=("Arial", 13, "bold")).grid(row=8, column=0, padx=5, pady=(2, 2), sticky='w')
        genero_var = tk.StringVar(value="Masculino")
        radiobutton_masc = tk.Radiobutton(frame_cadastro, text="Masculino", variable=genero_var, value="Masculino")
        radiobutton_fem = tk.Radiobutton(frame_cadastro, text="Feminino", variable=genero_var, value="Feminino")
        radiobutton_masc.grid(row=9, column=0, padx=5, sticky='w')
        radiobutton_fem.grid(row=10, column=0, padx=5, sticky='w')

        tk.Label(frame_cadastro, text="Email:", font=("Arial", 13, "bold")).grid(row=11, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_email = tk.Entry(frame_cadastro, font=("Arial", 12))
        entry_email.grid(row=12, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_cadastro, text="Senha:", font=("Arial", 13, "bold")).grid(row=13, column=0, padx=5, pady=(2, 2), sticky='w')
        entry_senha_cadastro = tk.Entry(frame_cadastro, show="*", font=("Arial", 12))
        entry_senha_cadastro.grid(row=14, column=0, padx=5, pady=(2, 10))

        check_termos_var = tk.BooleanVar()
        check_termos = tk.Checkbutton(frame_cadastro, text="Aceito os Termos de Serviço", variable=check_termos_var)
        check_termos.grid(row=15, columnspan=2, pady=10)

        botao_salvar = tk.Button(frame_cadastro, text="Salvar", command=lambda: self.salvar_usuario(entry_nome.get(), entry_idade.get(), entry_profissao.get(), cidade_var.get(), genero_var.get(), entry_email.get(), entry_senha_cadastro.get(), check_termos_var.get()), font=("Arial", 12))
        botao_salvar.grid(row=16, columnspan=2, pady=20)

        botao_voltar = tk.Button(frame_cadastro, text="Já tenho uma conta? Voltar para Login", command=self.voltar_login, font=("Arial", 10))
        botao_voltar.grid(row=17, columnspan=2, pady=10)

    def salvar_usuario(self, nome, idade, profissao, cidade, genero, email, senha, aceita_termos):
        if aceita_termos:
            usuario_existente = session.query(Usuario).filter_by(email=email).first()
            if usuario_existente:
                messagebox.showerror("Erro", "Este email já está cadastrado.")
                return

            # Tente converter idade para inteiro
            try:
                idade = int(idade)
            except ValueError:
                messagebox.showerror("Erro", "Idade deve ser um número.")
                return

            novo_usuario = Usuario(nome=nome, idade=idade, profissao=profissao, cidade=cidade, genero=genero, email=email, senha=senha, aceita_termos=aceita_termos)
            session.add(novo_usuario)
            session.commit()
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            self.voltar_login()  
        else:
            messagebox.showwarning("Erro", "Você deve aceitar os termos para continuar.")

    def voltar_login(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        label_bem_vindo = tk.Label(self.master, text="👋 Bem-vindo!", font=("Arial", 16, "bold"))
        label_bem_vindo.pack(pady=30)

        frame_login = tk.Frame(self.master, bd=2, relief="solid", padx=10, pady=10)
        frame_login.pack(pady=20, padx=20)

        tk.Label(frame_login, text="Usuário (Email):", font=("Arial", 13, "bold")).grid(row=0, column=0, padx=5, pady=(2, 2), sticky='w')
        self.entry_usuario = tk.Entry(frame_login, font=("Arial", 12))
        self.entry_usuario.grid(row=1, column=0, padx=5, pady=(2, 10))

        tk.Label(frame_login, text="Senha:", font=("Arial", 13, "bold")).grid(row=2, column=0, padx=5, pady=(2, 2), sticky='w')
        self.entry_senha = tk.Entry(frame_login, show="*", font=("Arial", 12))
        self.entry_senha.grid(row=3, column=0, padx=5, pady=(2, 10))

        botao_login = tk.Button(frame_login, text="Entrar", command=self.realizar_login, font=("Arial", 12))
        botao_login.grid(row=4, columnspan=2, pady=20)

        botao_cadastrar = tk.Button(self.master, text="Criar Nova Conta", command=self.abrir_formulario_cadastro, font=("Arial", 10))
        botao_cadastrar.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoLogin(root)
    root.mainloop()
