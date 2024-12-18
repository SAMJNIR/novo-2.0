import random
import time as tm
class Player:
    def __init__(self,nome, classe, level =1):
        self.nome = nome * level
        self.status = True
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
            
    def d10(self):
        for x in range(6):
            d10 = random.randint(0,10)
            tm.sleep(0.2)
            print(f"\r{d10}",end="")
            print()
        return d10