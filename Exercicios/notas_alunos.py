class Aluno:
    def __init__(self, nome, serie, nota):
        self.nome = nome
        self.serie = serie
        self.__nota = nota

    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            raise ValueError("A nota deve estar entre 0 e 10.")
        
aluno = Aluno("Maria", "5ª", 8.0)
print(aluno.nome)       # OK
print(aluno.serie)      # OK
