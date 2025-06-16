from Jogador import Jogador

def main():
   
    pontos_rony = [2, 1, 0, 1, 2, 3, 1, 2, 0, 1]  
    jogador1 = Jogador("Rony", pontos_rony)
    jogador1.exibir_estatisticas()

    print()

    pontos_gabigol = [2, 3, 2, 3, 2, 3]  
    jogador2 = Jogador("Gabigol", pontos_gabigol)
    jogador2.exibir_estatisticas()

main()
