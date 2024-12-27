from player import Player
from InquirerPy import prompt
from enemy import InimigoComum, SubBoss, Boss
from promptPadrão import opçõesDeEntrada, Batalha, Direção, Inventário, Classes, Habilidades

class RPG(Player):
    def __init__(self,nome):
        super().__init__(nome)
    

#rpg =RPG(str(input("Qual o seu nome novato? ")))

respostaDeEentrada = opçõesDeEntrada()
    

match respostaDeEentrada:

 case "batalha":
  
  Batalha()
    
 case "direcao":
  
  Direção()
        
 case "inventario":
      
  Inventário()

 case "classes":
      
  Classes()

 case "habilidades":

  Habilidades()
        
    