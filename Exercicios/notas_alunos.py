class Aluno:
    def __init__(self, nome, serie, nota):
        self.nome = nome
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

  
        
aluno1 = Aluno("Lucas", "8°", 7)
print(aluno1.nota)

aluno1.nota = 9
print(aluno1.nota)

aluno1.nota = 12



