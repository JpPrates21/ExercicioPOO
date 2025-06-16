from abc import ABC, abstractmethod

class Trabalhador(ABC):
    
    @abstractmethod
    def trabalhar(self) -> None: pass

    @abstractmethod
    def ir_para_casa(self) -> None: pass

    @abstractmethod
    def horario_de_almoco(self) -> None: pass


class Cozinheiro(Trabalhador):
    def trabalhar(self):
        print("O Cozinheiro está trabalhando")

    def ir_para_casa(self):
        print("O Cozinheiro está indo pra casa")

    def horario_de_almoco(self):
        print("O Cozinheiro está almocando")

def comunicar_trabalhador(trabalhador: Trabalhador):
    trabalhador.trabalhar()
    print("Comunicar ao trabalhador para ir para casa")
    trabalhador.ir_para_casa()


Jorge = Cozinheiro()
Luiz = Pedreiro()

comunicar_trabalhador(Jorge)
print()
comunicar_trabalhador(Luiz)
