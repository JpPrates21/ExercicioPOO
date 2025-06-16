class Pessoa:  

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dirigir(self, veiculo):
        print("Dirigindo um {}".format(veiculo))

    def cantar(self):
        print("Laalala")

    def apresentar_idade(self):
        return self.idade 