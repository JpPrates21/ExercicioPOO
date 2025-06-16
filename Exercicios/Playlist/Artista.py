from Interface import ArtistaInterface
from typing import List


class Artista(ArtistaInterface):
    def __init__(self) -> None:
        self.__nome: str = ""
        self.__genero: str = ""
        self.__musicas: List[str] = []

    def set_nome(self, nome: str) -> None:
        if not nome:
            raise ValueError("Nome do artista não pode ser vazio.")
        self.__nome = nome.strip()

    def get_nome(self) -> str:
        return self.__nome

    def set_genero(self, genero: str) -> None:
        if not genero:
            raise ValueError("Gênero não pode ser vazio.")
        self.__genero = genero.strip()

    def get_genero(self) -> str:
        return self.__genero

    def adicionar_musica(self, musica: str) -> None:
        if not musica:
            raise ValueError("Nome da música não pode ser vazio.")
        self.__musicas.append(musica.strip())

    def get_musicas(self) -> List[str]:
        return self.__musicas
