from Artista import Artista
from Playlist import Playlist


def main() -> None:
    try:
        artista1 = Artista()
        artista1.set_nome("The Weeknd")
        artista1.set_genero("R&B")
        artista1.adicionar_musica("Blinding Lights")
        artista1.adicionar_musica("Starboy")

        artista2 = Artista()
        artista2.set_nome("Coldplay")
        artista2.set_genero("Rock Alternativo")
        artista2.adicionar_musica("Fix You")
        artista2.adicionar_musica("Paradise")

        minha_playlist = Playlist()
        minha_playlist.adicionar_da_banda(artista1)
        minha_playlist.adicionar_da_banda(artista2)

        minha_playlist.mostrar_playlist()
        minha_playlist.salvar_em_arquivo()

    except Exception as e:
        print(f"Erro: {e}")

main()
