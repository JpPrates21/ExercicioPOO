from abc import ABC, abstractmethod

class EstatisticasInterface(ABC):
    @abstractmethod
    def total_pontos(self):
        pass

    @abstractmethod
    def media_pontos(self):
        pass

    @abstractmethod
    def total_partidas(self):
        pass
