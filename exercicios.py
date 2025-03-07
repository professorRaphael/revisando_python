class Exercicios:
    def exercicio01():
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        double = [num ** 2 for num in lista]
        print(double)

    def exercicio02():
        alunos = {"Raphael": 8.8, "Carol": 10, "Vanessa": 6}
        aluno_pesquisado = "Raphael"
        if aluno_pesquisado in alunos:
            print(f"Aluno encontrado: {aluno_pesquisado}")
        else:
            print("Aluno desencontrado kkkkk")

    def exercicio03():
        alunos = [
            {"Nome": "Raphael", "Nota": 8.8},
            {"Nome": "Carol", "Nota": 10},
            {"Nome": "Vanessa", "Nota": 6}
        ]
        print(sorted(alunos, key=lambda aluno: aluno["Nota"]))

    def exercicio04():
        pass
        #Classe Carro

    def exercicio05():
        pass
        # Feito

    def exercicio06():
        pass
        # Dataclass Produto
    
    def exercicio07():
        tuplinha = ("vermelho", "azul", "verde")
        # tuplinha.__add__("amarelo")
        print(tuplinha)

    def exercicio08():
        '''Método na classe Produto feito no exercicio06'''

class Carro:
    """Exercicio 04"""
    def __init__(self, marca: str, modelo: str, ano: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __repr__(self):
        return f"\tMarca: {self.marca}\n\tModelo: {self.modelo}\n\tAno: {self.ano}"

from dataclasses import dataclass

@dataclass
class Produto:
    '''Exercicio 05'''
    nome: str
    preco: float
    quantidade: int

    def exibir_informacao(self):
        return f"Nome: {self.nome}\nPreço: R${self.preco}\nQuantidade: {self.quantidade}"
        
if __name__ == "__main__":
    Exercicios.exercicio01()
    Exercicios.exercicio02()
    Exercicios.exercicio03()
    carro = Carro(marca="Fiat", modelo="Palio", ano=2015)
    print(carro.__repr__())
    # Exercicio 05 - Imprimir em uma lista modelo de três carros insatanciados.
    carro1 = Carro("Toyota", "Corola", 2020)
    carro2 = Carro("Hyundai", "Ret", 2021)
    listinha = [carro.modelo, carro1.modelo, carro2.modelo]
    print(listinha)
    produto = Produto(nome="Mount & Blade 2", preco=350.00, quantidade=484)
    print(produto.__repr__())
    Exercicios.exercicio07()
    print(produto.exibir_informacao())