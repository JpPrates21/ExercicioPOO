class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self):
        print("Está correndo")

    def beber(self, bebida):
        if bebida == "cerveja":
            self.__apresentar_documento()
        print("Bebendo...")

    
    def __apresentar_documento(self):
        print(self.__cpf)
        


Camila = Pessoa("Camila", 19, 15186666637)

Camila.correr()

Camila.beber("cerveja")
Camila.beber("coca")