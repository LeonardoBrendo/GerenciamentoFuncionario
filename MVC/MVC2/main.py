from controller import CarroController

if __name__ == "__main__":
    controlador = CarroController()

    while True:
        print("\n1. Adicionar Carro")
        print("2. Listar Carros")
        print("3. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            controlador.adicionar_carro()
        elif opcao == '2':
            controlador.listar_carros()
        elif opcao == '3':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
