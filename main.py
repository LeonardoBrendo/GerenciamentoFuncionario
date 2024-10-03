# import tkinter as tk
# from tkinter import messagebox, ttk

# pessoas_cadastradas = []

# def mostrar_tabela():
#     janela_tabela = tk.Toplevel()
#     janela_tabela.title("Pessoas Cadastradas")
#     janela_tabela.geometry("600x300")
    
#     colunas = ("Nome", "CPF", "Email","Idade", "Altura", "Profissão", "Salário", "Gênero", "Cidade")
#     tree = ttk.Treeview(janela_tabela, columns=colunas, show="headings")
    
#     for coluna in colunas:
#         tree.heading(coluna, text=coluna)
#         tree.column(coluna, anchor='center', minwidth=100, width=100)
    
#     for pessoa in pessoas_cadastradas:
#         tree.insert("", tk.END, values=pessoa)
    
#     tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# def salvar_pessoa():
#     nome = entry_nome.get()
#     cpf = entry_cpf.get()
#     idade = entry_idade.get()
#     altura = entry_altura.get()
#     profissao = entry_profissao.get()
#     salario = entry_salario.get()
#     email = entry_email.get()

#     genero = genero_var.get()
    
#     cidade = cidade_var.get()
    
#     aceita_termos = check_termos_var.get()
    
#     if nome and idade and altura and profissao and salario and email:
#         print("nome", nome)
#         print("idade", idade)
#         print("altura", altura)
#         print("profissao", profissao)
#         print("salario", salario)
#         print("email", email)
#         try:
#             cpf = int(cpf)
#             idade = int(idade)
#             altura = float(altura)
#             salario = float(salario)

#             if aceita_termos:
#                 pessoa = (nome, cpf, idade, altura, profissao, salario, genero, cidade)
#                 pessoas_cadastradas.append(pessoa)
                
#                 entry_nome.delete(0, tk.END)
#                 entry_cpf.delete(0, tk.END)
#                 entry_idade.delete(0, tk.END)
#                 entry_altura.delete(0, tk.END)
#                 entry_profissao.delete(0, tk.END)
#                 entry_salario.delete(0, tk.END)
#                 entry_email.delete(0, tk.END)
                
#                 messagebox.showinfo("Cadastro Concluído", "Pessoa cadastrada com sucesso!")
                
#                 mostrar_tabela()
                
#             else:
#                 messagebox.showwarning("Erro", "Você deve aceitar os termos para continuar.")
#         except ValueError:
#             messagebox.showerror("Erro", "Idade, altura e salário devem ser valores numéricos!")
#     else:
#         messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

# janela = tk.Tk()
# janela.title("Cadastro de Pessoa")
# janela.geometry("400x450")


# label_nome = tk.Label(janela, text="Nome:")
# label_nome.grid(row=0, column=0, padx=10, pady=5, sticky='e')

# entry_nome = tk.Entry(janela)
# entry_nome.grid(row=0, column=1, padx=10, pady=5)

# label_cpf = tk.Label(janela, text="CPF:")
# label_cpf.grid(row=1, column=0, padx=10, pady=5, sticky='e')

# entry_cpf = tk.Entry(janela)
# entry_cpf.grid(row=1, column=1, padx=10, pady=5)

# label_idade = tk.Label(janela, text="Idade:")
# label_idade.grid(row=2, column=0, padx=10, pady=5, sticky='e')

# entry_idade = tk.Entry(janela)
# entry_idade.grid(row=2, column=1, padx=10, pady=5)

# label_altura = tk.Label(janela, text="Altura (m):")
# label_altura.grid(row=3, column=0, padx=10, pady=5, sticky='e')

# entry_altura = tk.Entry(janela)
# entry_altura.grid(row=3, column=1, padx=10, pady=5)

# label_profissao = tk.Label(janela, text="Profissão:")
# label_profissao.grid(row=4, column=0, padx=10, pady=5, sticky='e')

# entry_profissao = tk.Entry(janela)
# entry_profissao.grid(row=4, column=1, padx=10, pady=5)

# label_salario = tk.Label(janela, text="Salário (R$):")
# label_salario.grid(row=5, column=0, padx=10, pady=5, sticky='e')

# entry_salario = tk.Entry(janela)
# entry_salario.grid(row=5, column=1, padx=10, pady=5)

# label_email = tk.Label(janela, text="Email : ")
# label_email.grid(row=6, column=0, padx=10, pady=5, sticky='e')

# entry_email = tk.Entry(janela)
# entry_email.grid(row=6, column=1, padx=10, pady=5)

# label_genero = tk.Label(janela, text="Gênero:")
# label_genero.grid(row=7, column=0, padx=10, pady=5, sticky='e')

# genero_var = tk.StringVar(value="Masculino")
# radiobutton_masc = tk.Radiobutton(janela, text="Masculino", variable=genero_var, value="Masculino")
# radiobutton_fem = tk.Radiobutton(janela, text="Feminino", variable=genero_var, value="Feminino")

# radiobutton_masc.grid(row=7, column=1, padx=10, sticky='w')
# radiobutton_fem.grid(row=8, column=1, padx=10, sticky='w')

# label_cidade = tk.Label(janela, text="Cidade:")
# label_cidade.grid(row=9, column=0, padx=10, pady=5, sticky='e')

# cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Brasília"]

# cidade_var = tk.StringVar()
# cidade_var.set(cidades[0])  

# optionmenu_cidades = tk.OptionMenu(janela, cidade_var, *cidades)
# optionmenu_cidades.grid(row=9, column=1, padx=10, pady=5)

# check_termos_var = tk.BooleanVar()
# check_termos = tk.Checkbutton(janela, text="Aceito os Termos de Serviço", variable=check_termos_var)
# check_termos.grid(row=10, columnspan=2, pady=10)

# botao_salvar = tk.Button(janela, text="Salvar", command=salvar_pessoa)
# botao_salvar.grid(row=11, columnspan=2, pady=10)

# janela.mainloop()

# import tkinter as tk
# from tkinter import ttk

# def realizar_login():
#     usuario = entry_usuario.get()
#     senha = entry_senha.get()

#     # Aqui você pode adicionar a lógica de autenticação, por exemplo, verificando o usuário e senha
#     print(f"Usuário: {usuario}")
#     print(f"Senha: {senha}")

# # Criação da janela principal
# janela = tk.Tk()
# janela.title("Tela de Login")
# janela.geometry("600x450")

# # Definindo a fonte para os labels e inputs
# fonte_label = ("Arial", 14, "bold")
# fonte_input = ("Arial", 12)

# # Frame para os campos de login, com borda azul (sem fundo azul)
# frame_login = tk.Frame(janela, bd=2, relief="solid", padx=10, pady=10)
# frame_login.pack(pady=20, padx=20)

# # Label e Entry para o Usuário
# label_usuario = tk.Label(frame_login, text="Usuário:", font=fonte_label)
# label_usuario.grid(row=0, column=0, padx=5, pady=5, sticky='w')

# entry_usuario = tk.Entry(frame_login, font=fonte_input)
# entry_usuario.grid(row=1, column=0, padx=5, pady=5)

# # Label e Entry para a Senha (mascarada com *)
# label_senha = tk.Label(frame_login, text="Senha:", font=fonte_label)
# label_senha.grid(row=2, column=0, padx=5, pady=5, sticky='w')

# entry_senha = tk.Entry(frame_login, show="*", font=fonte_input)
# entry_senha.grid(row=3, column=0, padx=5, pady=5)

# # Botão para realizar login
# botao_login = tk.Button(janela, text="Login", command=realizar_login, font=("Arial", 12))
# botao_login.pack(pady=10)

# # Rodar a janela
# janela.mainloop()

import tkinter as tk
from tkinter import ttk

def realizar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Aqui você pode adicionar a lógica de autenticação, por exemplo, verificando o usuário e senha
    if usuario == 'admin' and senha == 'admin':
        print(f"Usuário: {usuario}")
        print(f"Senha: {senha}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x400")  # Mantendo a altura para centralizar melhor

# Definindo a fonte para os labels, inputs e bem-vindo
fonte_label = ("Arial", 14, "bold")
fonte_input = ("Arial", 12)
fonte_bem_vindo = ("Arial", 16, "bold")

# Mensagem de bem-vindo
label_bem_vindo = tk.Label(janela, text="👋 Bem-vindo!", font=fonte_bem_vindo)
label_bem_vindo.pack(pady=30)  # Espaçamento ajustado acima da mensagem

# Frame para os campos de login, com borda azul (sem fundo azul)
frame_login = tk.Frame(janela, bd=2, relief="solid", padx=10, pady=10)
frame_login.pack(pady=30, padx=20)

# Label e Entry para o Usuário
label_usuario = tk.Label(frame_login, text="Usuário:", font=fonte_label)
label_usuario.grid(row=0, column=0, padx=5, pady=(5, 2), sticky='w')  # Diminui o espaçamento entre label e input

entry_usuario = tk.Entry(frame_login, font=fonte_input)
entry_usuario.grid(row=1, column=0, padx=5, pady=(2, 10))  # Espaço pequeno entre label e input

# Label e Entry para a Senha (mascarada com *)
label_senha = tk.Label(frame_login, text="Senha:", font=fonte_label)
label_senha.grid(row=2, column=0, padx=5, pady=(5, 2), sticky='w')

entry_senha = tk.Entry(frame_login, show="*", font=fonte_input)
entry_senha.grid(row=3, column=0, padx=5, pady=(2, 10))

# Botão para realizar login
botao_login = tk.Button(janela, text="Login", command=realizar_login, font=("Arial", 12))
botao_login.pack(pady=20)

# Rodar a janela
janela.mainloop()
