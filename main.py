from player import Player
import random
from enemy import Enemy
from InquirerPy import prompt


class RPG(Player):
    def __init__(self,nome,classe,level):
        super().__init__(nome,classe,level)

    
    def historia(self):
        pass
    
    def inputs(self,qual_pergunta):
        #Perguntas a se fazer 
        #1 -> batalha
        #2 -> direcao a seguir
        #3 -> acoes relacionada a mochila
    
        match qual_pergunta:
            case 1:
                batalha_Q = [{
                    "type":"list",
                    "message":"Oque voce quer fazer?",
                    "name":"opcoes",
                    "choices":["Enfrentar","Fugir","Falar com o inimigo"]
                },{"type":"list",
                    "message":"Oque voce fala pra ele",
                    "name":"opcoes",
                    "choices":["Voce vai morrer!","Pra que lutar?","vamos uma quebra de braco?"],
                    "when":lambda result: result["opcoes"] == "Falar com o inimigo"
                }]
                self.escolher_acao = prompt(batalha_Q)
                
            case 2:
                direcoes_Q = [{
                    "type":"list",
                    "message":"Qual caminho tomar?",
                    "name":"opcoes",
                    "choices":["NORTE","SUL","LESTE","OESTE"]
                }] 
                self.caminho = prompt(direcoes_Q)
            
            case 3:
                if self.mochila:
                    action = [{
                        "type":"confirm",
                        "message":"Olhar itens mochila?",
                        "name":"proceed",
                        "default":True
                    },{
                        "type":"list",
                        "message":"Qual Item?",
                        "name":"opcoes",
                        "choices":self.mochila
                    }] 
                    self.acao = prompt(action)
                else:
                    print("Sua mochila esta vazia")

        
     
    def itens(self): # Modificar
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


                 
            
def main():
    rpg =RPG("Sandro", "guerreiro",1)
    rpg.inputs(3)
    
if __name__ == "__main__":    
    main()