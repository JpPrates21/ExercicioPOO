from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def mostrar_dados(self):
        pass
class Aluno(Pessoa):
    def __init__(self, nome, serie, nota):
        super().__init__(nome)
        self.serie = serie
        self._nota = nota   # Atributo privado

    @property
    def nota(self):
        return self._nota   # Getter
    
    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor  #Setter com validação
        else:
            print("A nota deve estar entre 0 e 10")

    def mostrar_dados(self):
        print(self.nome, self.serie, self.nota)
        
class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)

        self.disciplina = disciplina

    def mostrar_dados(self):
        print(f"Professor: {self.nome} : {self.disciplina}")

prof1 = Professor("Rogerio", "Matematica")
prof1.mostrar_dados()

aluno1 = Aluno("Lucas", "8°", 7)
aluno1.mostrar_dados()
aluno1.nota = 9
print(aluno1.nota)
aluno1.nota = 12



