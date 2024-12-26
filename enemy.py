import random
class InimigoComum:
    def __init__(self,multiplicador=1):
        self.status:bool = True
        self.vida:int = 15 * multiplicador
        self.velocidade:int = random.randint(0,5)
        self.dropXp:int = random.randint(0,50)
        self.nome:list[str] = []
    
    def rolar_dano(self):
        d10 = random.randint(0,10)
        return d10
    
            
class SubBoss:
    def __init__(self):
        self.status:bool = True
        self.vida:int = 100
        self.velocidade:int = random.randint(0,10)
        self.dropXp:int = random.randint(0,100)
        self.items_dropaveis:list[dict] = []

    def Boto_cor_de_Rosa(self):
        pass

    

class Boss:
    def __init__(self):
        self.status = True 