from Artista import Artista
from typing import List


class Playlist:
    def __init__(self) -> None:
        self.__musicas_playlist: List[str] = []

    def adicionar_da_banda(self, artista: Artista) -> None:
        for musica in artista.get_musicas():
            self.__musicas_playlist.append(f"{musica} - {artista.get_nome()} ({artista.get_genero()})")

    def mostrar_playlist(self) -> None:
        if not self.__musicas_playlist:
            print("A playlist está vazia.")
            return
        print("\n--- Playlist ---")
        for i, faixa in enumerate(self.__musicas_playlist, start=1):
            print(f"{i}. {faixa}")

    def salvar_em_arquivo(self, nome_arquivo: str = "playlist.txt") -> None:
        try:
            with open(nome_arquivo, "w", encoding="utf-8") as file:
                for faixa in self.__musicas_playlist:
                    file.write(faixa + "\n")
            print(f"Playlist salva com sucesso em '{nome_arquivo}'.")
        except IOError as e:
            print(f"Erro ao salvar o arquivo: {e}")
