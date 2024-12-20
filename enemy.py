import random
class Enemy:
    def __init__(self,multiplicador=1):
        self.vida = 15 * multiplicador
        self.velocidade = random.randint(0,5)
        self.dropXp = random.randint(0,50)
        self.status = "VIVO"
    
    def rolar_dano(self):
        d10 = random.randint(0,10)
        return d10
    
    def dano_tomado(self,dano):
        if dano >= self.vida and self.vida == 0:
            self.status = "MORTO"
            return self.dropXp
        else:
            self.vida -= dano
            
    