import random
import time as tm
class Player:
    def __init__(self,nome,level =1):
        self.nome = nome * level
        self.status = True
        self.classe = None
        self.vida = 100 * level
        self.max_peso = 50 * level
        self.item_na_mao = None
        self.mochila = []
        self.percepcao = random.randint(0,5)
        self.barraXP = []
        self.nivel = level
    
    def verificar_peso(self,peso_item):
        if peso_item < self.max_peso:
            self.max_peso -= peso_item
        else:
            print("Nao e possivel carregar esse item")
    
    def dano_tomado(self,dano):
        if dano <= self.vida:
            self.vida -= dano
        
        elif self.vida == 0:
            self.status = False
            
            
                        
    def pegar_item(self,item):
        if len(item) == 2:
            self.objeto, self.peso_item = item
            
    def d20(self):
        for x in range(6):
            d20 = random.randint(0,20)
            tm.sleep(0.2)
            print(f"\r{d20}",end="")
        print()
        return d20
            
    def D8(self):
        for x in range(6):
            d10 = random.randint(0,8)
            tm.sleep(0.2)
            print(f"\r{d10}",end="")
        print()
        return d10
    
    def D6(self):
        self.D6 = ["""
    +-------+
    |       |
    |   o   |
    |       |
    +-------+""",
    """
    +-------+
    | o     |
    |       |
    |     o |
    +-------+""",
    """
    +-------+
    | o     |
    |   o   |
    |     o |
    +-------+""",
    """
    +-------+
    | o   o |
    |       |
    | o   o |
    +-------+""",
    """
    +-------+
    | o   o |
    |   o   |
    | o   o |
    +-------+""",
    """
    +-------+
    | o   o |
    | o   o |
    | o   o |
    +-------+"""]
        valor = random.randint(0,5)
        print(self.D6[valor])
        return  valor+1
                