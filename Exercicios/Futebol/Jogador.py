from Interface import EstatisticasInterface

class Jogador(EstatisticasInterface):
    def __init__(self, nome, pontos_partidas):
        self.nome = nome
        self.pontos_partidas = pontos_partidas  

    def total_pontos(self):
        return sum(self.pontos_partidas)

    def media_pontos(self):
        if self.pontos_partidas:
            return sum(self.pontos_partidas) / len(self.pontos_partidas)
        return 0

    def total_partidas(self):
        return len(self.pontos_partidas)

    def exibir_estatisticas(self):
        print(f"--- Estatísticas do jogador {self.nome} ---")
        print(f"Total de partidas: {self.total_partidas()}")
        print(f"Total de pontos: {self.total_pontos()}")
        print(f"Média de pontos por partida: {self.media_pontos():.2f}")
