from abc import ABC, abstractmethod
class Pessoa(ABC): 
    def correr(self):
        print("A pessoa esta correndo de manha")

    @abstractmethod 
    def trabalhar(self):
        pass
class Professor(Pessoa):
    def trabalhar(self):
        print("O Professor está dando aula")
    
p1 = Professor() 
p1.correr()
p1.trabalhar()