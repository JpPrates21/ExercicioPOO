from Engenheira import Engenheira
from Formas import Retangulo, Quadrado

def main():
    # Criação dos terrenos
    terreno1 = Retangulo(largura=10, altura=5)
    terreno2 = Quadrado(lado=7)

    # Criação da engenheira
    engenheira = Engenheira("Ana")

    # Medições do Retângulo
    print("Retângulo:")
    engenheira.medir_area(terreno1)
    engenheira.medir_perimetro(terreno1)

    print("\nQuadrado:")
    engenheira.medir_area(terreno2)
    engenheira.medir_perimetro(terreno2)

main()
