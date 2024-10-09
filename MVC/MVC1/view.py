class CarroView:
    @staticmethod
    def mostrar_carro(carro):
        print(f"Nome: {carro.nome}, Ano: {carro.ano}, Valor: {carro.valor}")

    @staticmethod
    def listar_carros(carros):
        print("Lista de Carros:")
        for carro in carros:
            print(f"- {carro}")
    
    @staticmethod
    def solicitar_dados_carro():
        nome = input("Digite o nome do carro: ")
        valor = float(input("Digite o valor do carro: "))
        ano = int(input("Digite o ano do carro: "))
        return nome, valor, ano
