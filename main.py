from player import Player
import random
from enemy import Enemy

class RPG(Player):
    def __init__(self,nome,classe,level):
        super().__init__(nome,classe,level)

            
    def bau(self):
        return random.choice([
            ["Espada Curta","D10","W"],# W -> Weapons
            ["Espada Longa","D10","W"],
            ["Machado Curto","D10","W"],
            ["Machado Grande","D10","W"],
            ["Adaga","D10","W"],
            ["Arco","D10","W"],
            ["Massa","D10","W"],
            ["Katana","D10","W"],
            
            ["cura P","U"], #U -> UTILITARIOS
            ["cura M","U"],
            ["cura G","U"]
            ])
    
    def emboscada(self,escolha):
        match escolha:
            case "RUN": #Se escolher correr
                print("frangote")
                self.status = False
            case "LT": #se escolhe batalhar
                self.enfrentar_inimigo()
                
                
            
    def enfrentar_inimigo(self):
        inimigo = Enemy(self.nivel)
        if inimigo.velocidade > self.percepcao:
            dano_inimigo = inimigo.rolar_dano()
            self.dano_tomado(dano_inimigo)
        else:
            dano_no_inimigo = self.d20()
            if inimigo.status == "MORTO":
                loot = inimigo.dano_tomado(dano_no_inimigo)
                self.barraXP.append(loot)
            
            
def main():
    rpg =RPG("Sandro", "guerreiro",1)
    while rpg.status:
        rpg.emboscada(str(input("Escolha (RUN/LT:lutar): ")))  
    
    
if __name__ == "__main__":    
    main()