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
                    "message":"Qual sua Acao?",
                    "name":"opcoes",
                    "choices":["Jogar Dado","Fugir","Falar com o inimigo"]
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
    def GameOver(self):
        print("Voce morreu")
        
    def battle(self,Roll_player:int,Roll_inimigo:int,inimigo:object):
            while inimigo.status:    
                dano_player = self.d20()
                dano_inimigo = inimigo.rolar_dano()
                if Roll_player > Roll_inimigo:
                    inimigo.vida -= dano_player
                    if inimigo.vida <= 0:
                        inimigo.status = False
                        self.xpDrop += inimigo.dropXp
                else:
                    self.atributo["Const"] -= dano_inimigo
                    if self.atributo["Const"] <= 0:
                        self.status = False
                        self.GameOver()
                        break
    def batalha(self):
        res = self.inputs("batalha")
        inimigo = InimigoComum(self.level)
        if res == "Jogar Dado":
            dado_player = self.D6()
            dado_inimigo = self.D6()
            self.battle(dado_player,dado_inimigo,inimigo)

        
        
    
            
def main():
    rpg =RPG(str(input("Qual o seu nome novato? ")))
    rpg.classes(rpg.inputs("classes"))
    print(*rpg.mochila,sep=" - ")
    rpg.batalha()
    
if __name__ == "__main__":
    main()