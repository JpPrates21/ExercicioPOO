class Jogador:
    def __init__(self, altura, velocidade, passe, chute):
        self.altura = altura
        self.velocidade = velocidade
        self.passe = passe
        self.chute = chute

    def passar(self):
        print("Jogador toca a bola")

    def chutar(self):
        print("Jogador finaliza")

    def defender(self):
        print("Jogador defende")

    def agarrar(self):
        print("Agarra")

class Goleiro(Jogador):
    def __init__(self, altura, velocidade, passe, chute, elaticidade, saida_bola):
        super().__init__(altura, velocidade, passe, chute)

        self.elasticidade = elaticidade
        self.saida_bola = saida_bola
    
    def agarrar(self):
        print("Goleiro agarra a bola")

    def defender(self):
        esta_fora_area = False
        if esta_fora_area:
            print("Usa somente os pés para defender")
        else:
            print("Usa as mãos para defender")

class Jogador_Linha(Jogador):
    def agarrar(self):
        print("Falta e cartão para o jogodor")
        


cassio = Goleiro(190,88,49,10,80,70)
gabigol = Jogador_Linha (175,88,90,95)

cassio.defender()
cassio.agarrar()
gabigol.passar()
gabigol.agarrar()