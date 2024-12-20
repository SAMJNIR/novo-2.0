from player import Player
from enemy import Enemy
from InquirerPy import prompt


class RPG(Player):
    def __init__(self,nome,level=1):
        super().__init__(nome,level)
    
    def inputs(self,qual_pergunta:int):
        """
        Perguntas a se fazer 
        1 -> batalha
        2 -> direcao a seguir
        3 -> acoes relacionada a mochila"""
    
        match qual_pergunta:
            case 1:
                batalha_Q = [{
                    "type":"list",
                    "message":"Oque voce quer fazer?",
                    "name":"opcoes",
                    "choices":["Enfrentar","Fugir","Falar com o inimigo"]
                },
                {"type":"list",
                    "message":"Oque voce fala pra ele",
                    "name":"fala",
                    "choices":["Voce vai morrer!","Pra que lutar?","vamos uma quebra de braco?"],
                    "when":lambda result: result["opcoes"] == "Falar com o inimigo"
                }]
                return prompt(batalha_Q)["opcoes"]
                
            case 2:
                direcoes_Q = [{
                    "type":"list",
                    "message":"Qual caminho tomar?",
                    "name":"opcoes",
                    "choices":["NORTE","SUL","LESTE","OESTE"]
                }] 
                return prompt(direcoes_Q)["opcoes"]
            
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
                    return prompt(action)["opcoes"]
                else:
                    print("Sua mochila esta vazia")
            case 4:
                classes = [{
                    "type":"list",
                    "message":"Qual classe você escolherá?",
                    "name":"opcoes",
                    "choices":["Capoerista","Traficante","Barqueira","Pescador","Tocador de Forro","Rezadeira","Caboclo"]
                }]
                return prompt(classes)["opcoes"]
        
     
    def batalha(self):
        print("Você encontrou um Inimigo:")
        if res := self.inputs(1) == "Enfrentar":
            
            print("Voce tirou:")
            dadoPlayer = self.D6()
            
            print("O inimigo tirou:")
            dadoInimigo = self.D6()
            
            print(dadoPlayer,dadoInimigo)
            
        elif res == "Fugir":
            pass
            
            
            
                


                 
            
def main():
    rpg =RPG(str(input("Qual o seu nome?")))
    
if __name__ == "__main__":    
    main()