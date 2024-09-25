import tkinter as tk
from tkinter import messagebox

def salvar_pessoa():
    nome = entry_nome.get()
    idade = entry_idade.get()
    altura = entry_altura.get()
    profissao = entry_profissao.get()
    salario = entry_salario.get()
    
    if nome and idade and altura and profissao and salario:
        try:
            idade = int(idade)
            altura = float(altura)
            salario = float(salario)

            messagebox.showinfo("Cadastro Concluído", 
                                f"Nome: {nome}\nIdade: {idade} anos\nAltura: {altura} m\nProfissão: {profissao}\nSalário: R${salario:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Idade, altura e salário devem ser valores numéricos!")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

janela = tk.Tk()
janela.title("Cadastro de Pessoa")
janela.geometry("300x300")

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

botao_salvar = tk.Button(janela, text="Salvar", command=salvar_pessoa)
botao_salvar.grid(row=5, columnspan=2, pady=10)

janela.mainloop()
