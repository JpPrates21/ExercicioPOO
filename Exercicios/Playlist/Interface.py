from abc import ABC, abstractmethod

class ArtistaInterface(ABC):
    @abstractmethod
    def set_nome(self, nome: str) -> None:
        pass

    @abstractmethod
    def adicionar_musica(self, musica: str) -> None:
        pass

    @abstractmethod
    def set_genero(self, genero: str) -> None:
        pass
