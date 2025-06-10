from abc import ABC, abstractmethod



def ExtratorDados(ABC):
    
    @classmethod
    @abstractmethod
    def extrair_dados(cls, *args, **kwargs):