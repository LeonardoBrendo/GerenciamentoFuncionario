class Carro:
    def __init__(self, nome, valor, ano):
        self.nome = nome
        self.valor = valor
        self.ano = ano

    def __str__(self):
        return f"Carro: {self.nome}, Ano: {self.ano}, Valor: {self.valor}"

class CarroModel:
    def __init__(self):
        self.carros = []

    def adicionar_carro(self, carro):
        self.carros.append(carro)

    def listar_carros(self):
        return self.carros
