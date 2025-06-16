from Interface import FormasInterface
from typing import Type

class Engenheira:
    def __init__(self, nome: str):
        self.nome = nome

    def medir_area(self, terreno: FormasInterface):
        print(f"[{self.nome}] A área do terreno é: {terreno.calcular_area()}")

    def medir_perimetro(self, terreno: FormasInterface):
        print(f"[{self.nome}] O perímetro do terreno é: {terreno.calcular_perimetro()}")
