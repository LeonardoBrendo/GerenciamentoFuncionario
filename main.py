import tkinter as tk
from tkinter import messagebox

def salvar_pessoa():
    nome = entry_nome.get()
    idade = entry_idade.get()
    altura = entry_altura.get()
    profissao = entry_profissao.get()
    salario = entry_salario.get()

    genero = genero_var.get()
    
    cidade = cidade_var.get()
    
    aceita_termos = check_termos_var.get()
    
    if nome and idade and altura and profissao and salario:
        try:
            idade = int(idade)
            altura = float(altura)
            salario = float(salario)

            if aceita_termos:
                messagebox.showinfo("Cadastro Concluído", 
                                    f"Nome: {nome}\nIdade: {idade} anos\nAltura: {altura} m\nProfissão: {profissao}\nSalário: R${salario:.2f}\n"
                                    f"Gênero: {genero}\nCidade: {cidade}\nTermos aceitos: Sim")
            else:
                messagebox.showwarning("Erro", "Você deve aceitar os termos para continuar.")
        except ValueError:
            messagebox.showerror("Erro", "Idade, altura e salário devem ser valores numéricos!")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

janela = tk.Tk()
janela.title("Cadastro de Pessoa")
janela.geometry("400x450")

label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky='e')

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_idade = tk.Label(janela, text="Idade:")
label_idade.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_idade = tk.Entry(janela)
entry_idade.grid(row=1, column=1, padx=10, pady=5)

label_altura = tk.Label(janela, text="Altura (m):")
label_altura.grid(row=2, column=0, padx=10, pady=5, sticky='e')

entry_altura = tk.Entry(janela)
entry_altura.grid(row=2, column=1, padx=10, pady=5)

label_profissao = tk.Label(janela, text="Profissão:")
label_profissao.grid(row=3, column=0, padx=10, pady=5, sticky='e')

entry_profissao = tk.Entry(janela)
entry_profissao.grid(row=3, column=1, padx=10, pady=5)

label_salario = tk.Label(janela, text="Salário (R$):")
label_salario.grid(row=4, column=0, padx=10, pady=5, sticky='e')

entry_salario = tk.Entry(janela)
entry_salario.grid(row=4, column=1, padx=10, pady=5)

label_genero = tk.Label(janela, text="Gênero:")
label_genero.grid(row=5, column=0, padx=10, pady=5, sticky='e')

genero_var = tk.StringVar(value="Masculino")
radiobutton_masc = tk.Radiobutton(janela, text="Masculino", variable=genero_var, value="Masculino")
radiobutton_fem = tk.Radiobutton(janela, text="Feminino", variable=genero_var, value="Feminino")

radiobutton_masc.grid(row=5, column=1, padx=10, sticky='w')
radiobutton_fem.grid(row=6, column=1, padx=10, sticky='w')

label_cidade = tk.Label(janela, text="Cidade:")
label_cidade.grid(row=7, column=0, padx=10, pady=5, sticky='e')

cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Brasília"]

cidade_var = tk.StringVar()
cidade_var.set(cidades[0]) 

optionmenu_cidades = tk.OptionMenu(janela, cidade_var, *cidades)
optionmenu_cidades.grid(row=7, column=1, padx=10, pady=5)

check_termos_var = tk.BooleanVar()
check_termos = tk.Checkbutton(janela, text="Aceito os Termos de Serviço", variable=check_termos_var)
check_termos.grid(row=8, columnspan=2, pady=10)

botao_salvar = tk.Button(janela, text="Salvar", command=salvar_pessoa)
botao_salvar.grid(row=9, columnspan=2, pady=10)

janela.mainloop()