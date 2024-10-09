from model import Carro, CarroModel
from view import CarroView

class CarroController:
    def __init__(self):
        self.model = CarroModel()
        self.view = CarroView()

    def adicionar_carro(self):
        nome, valor, ano = self.view.solicitar_dados_carro()
        carro = Carro(nome, valor, ano)
        self.model.adicionar_carro(carro)

    def listar_carros(self):
        carros = self.model.listar_carros()
        self.view.listar_carros(carros)
