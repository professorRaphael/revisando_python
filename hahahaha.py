class Sorvete:
    def __init__(self, sabor, preco):
        self.sabor = sabor
        self.preco = preco

    def __str__(self):
        return f"{self.sabor} - R${self.preco:.2f}"


class Sorveteria:
    def __init__(self):
        self.sorvetes = [
            Sorvete("Chocolate", 7.50),
            Sorvete("Morango", 6.00),
            Sorvete("Vanilla", 5.50),
            Sorvete("Menta", 6.80),
            Sorvete("Napolitano", 8.00)
        ]
        self.pedido = []

    def exibir_menu(self):
        print("\nMenu de Sorvetes:")
        for idx, sorvete in enumerate(self.sorvetes, 1):
            print(f"{idx}. {sorvete}")

    def fazer_pedido(self):
        while True:
            try:
                self.exibir_menu()
                opcao = int(input("\nEscolha o número do sabor (0 para finalizar): "))
                if opcao == 0:
                    break
                if 1 <= opcao <= len(self.sorvetes):
                    self.pedido.append(self.sorvetes[opcao - 1])
                    print(f"Você adicionou: {self.sorvetes[opcao - 1]}")
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")

    def calcular_total(self):
        return sum(sorvete.preco for sorvete in self.pedido)

    def exibir_resumo(self):
        if not self.pedido:
            print("\nVocê não fez nenhum pedido.")
        else:
            print("\nResumo do Pedido:")
            for sorvete in self.pedido:
                print(f"- {sorvete}")
            print(f"\nTotal a pagar: R${self.calcular_total():.2f}")


def main():
    sorveteria = Sorveteria()

    while True:
        print("\n--- Sorveteria ---")
        print("1. Fazer pedido")
        print("2. Exibir resumo do pedido")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            sorveteria.fazer_pedido()
        elif opcao == '2':
            sorveteria.exibir_resumo()
        elif opcao == '3':
            print("Obrigado pela visita! Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
