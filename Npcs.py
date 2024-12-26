import random
class Npc:
    def __init__(self):
        self.nomes = ["Fulano","ciclano","Beltrano"]
        self.funcoes = ["Comerciante","Traficante","Mercenario"]
        
    def sorteio(self):
        nome = random.choice(self.nomes)
        funcao = random.choice(self.funcoes)
    
    def missao1(self):
        pass