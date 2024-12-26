from player import Player
from InquirerPy import prompt
from enemy import InimigoComum, SubBoss, Boss

class RPG(Player):
    def __init__(self,nome):
        super().__init__(nome)
    
    def inputs(self,qual_pergunta:int) :
        """
        Qual tipo de entrada escolher:
        1 -> batalha
        2 -> direcao a seguir
        3 -> acoes relacionada a mochila
        4 -> classes
        5 -> habilidades
        """
        
        match qual_pergunta:
            case "batalha":
                return prompt([{
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
                }])["opcoes"]
                
            case "direcao":
                return prompt([{
                    "type":"list",
                    "message":"Qual caminho tomar?",
                    "name":"opcoes",
                    "choices":["NORTE","SUL","LESTE","OESTE"]
                }])["opcoes"]
            
            case "inventario":
                if self.mochila:
                    return prompt([{
                        "type":"confirm",
                        "message":"Olhar itens mochila?",
                        "name":"proceed",
                        "default":True
                    },{
                        "type":"list",
                        "message":"Qual Item?",
                        "name":"opcoes",
                        "choices":self.mochila
                    }])["opcoes"]
                else:
                    print("Sua mochila esta vazia")
                    
            case "classes":
                return prompt([{
                    "type":"list",
                    "message":"Qual classe você escolherá?",
                    "name":"opcoes",
                    "choices": ["Capoerista","Contrabandista","Pistoleiro","Rezadeira","Tocador de Forro","Barqueiro"]
                }])["opcoes"]
            
            case "habilidades":
                return prompt([{
                    "type":"list",
                    "message":"Habilidades",
                    "name":"opcoes",
                    "choices": self.habilidades_possiveis
                }])["opcoes"]
                
    def batalha(self):
        pass
        
        
    
            
def main():
    rpg =RPG(str(input("Qual o seu nome novato? ")))
    rpg.classes(rpg.inputs("classes"))
    print(*rpg.mochila,sep=" - ")
    
    
if __name__ == "__main__":
    main()