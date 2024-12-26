import random
import time as tm

class Player:
    def __init__(self,nome):
        self.nome = nome 
        self.classe = None
        self.status = True
        self.level = 1
        self.atributo:dict[str:int] = {
            "Const": None,
            "For": None,
            "Dex": None,
            "Car": None,
            "Sab": None
        }
        
        self.habilidades_possiveis:list[str] = []
        
        self.mochila = []
    
    def dano_tomado(self,dano):
        if dano <= self.vida:
            self.vida -= dano
        
        elif self.vida == 0:
            self.status = False
            
            
                        
    def pegar_item(self,item):
        if len(item) == 2:
            self.objeto, self.peso_item = item
    
    
    #["Capoerista","Contrabandista","Pistoleiro","Rezadeira","Tocador de Forro","Barqueiro"]
    
    def classes(self,escolha_de_classe):
        
        match escolha_de_classe:
            case "Capoerista":
                
                #Atributos
                self.atributo["Const"] = 0
                self.atributo["For"] = 0
                self.atributo["Dex"] = 0
                self.atributo["Car"] = 0
                self.atributo["Sab"] = 1
                #habilidades
                self.habilidades_possiveis = ["Ginga", "Roda", "Malícia", "Musicalidade", "Acrobacia"]
                
                #itens iniciais
                self.mochila += ["Cura simples",{"Gold":10},"Berimbau","Cordão","Atabaque"]
                
            case "Contrabandista":
                
                #Atributos
                self.atributo["Const"] = 0
                self.atributo["For"] = 0
                self.atributo["Dex"] = 0
                self.atributo["Car"] = 0
                self.atributo["Sab"] = 1
                #habilidades
                self.habilidades_possiveis = ["Furtividade", "Negociação", "Conhecimento", "Disfarce", " Sobrevivência"]
                
                #itens iniciais
                self.mochila += ["Cura simples",{"Gold":10},"Pistola",{"Balas":10},"Canivete suiço","Kit de Arrombamento"]
                    
            case "Pistoleiro":
                
                #Atributos
                self.atributo["Const"] = 0
                self.atributo["For"] = 0
                self.atributo["Dex"] = 0
                self.atributo["Car"] = 0
                self.atributo["Sab"] = 1
                #habilidades
                self.habilidades_possiveis = ["Músico", "Dança", "Compositor", "Persuasão", "Sobrevivência"]
                
                #itens iniciais
                self.mochila += ["Cura simples",{"Gold":10},"Revolver",{"Balas":16}]
                    
            case "Rezadeira":
                
                #Atributos
                self.atributo["Const"] = 0
                self.atributo["For"] = 0 
                self.atributo["Dex"] = 0
                self.atributo["Car"] = 0
                self.atributo["Sab"] = 1
                #habilidades
                self.habilidades_possiveis = ["Orações","Conhecimento de Ervas", "Rituais", "Persuasão", "Proteção Espiritual"]
                
                #itens iniciais
                self.mochila += ["Cura simples",{"Gold":10},"Terço","Livro de orações","Kit de ervas","Talisman"]
                    
            case "Tocador de Forro":
                
                #Atributos
                self.atributo["Const"] = 0
                self.atributo["For"] = 0
                self.atributo["Dex"] = 0
                self.atributo["Car"] = 0
                self.atributo["Sab"] = 1
                #habilidades
                self.habilidades_possiveis = ["Músico", "Dança", "Compositor", "Persuasão", "Sobrevivência"]
                
                #itens iniciais
                self.mochila += ["Cura simples",{"Gold":20},"Sanfona","Triangulo"]
                    
            case "Barqueiro":
                #Atributos
                self.atributo["Const"] = 0
                self.atributo["For"] = 0
                self.atributo["Dex"] = 0
                self.atributo["Car"] = 0
                self.atributo["Sab"] = 1
                #habilidades
                self.habilidades_possiveis = ["Navegação", "Natação", "Reparo de Embarcações", "Luta com Armas Improvisadas"]
                
                #itens iniciais
                
                self.mochila += ["Cura simples", {"Gold":10}, "Remo", "Rede de Pesca", "Bússola","Mapa Náutico","Kit de reparo"]
                    
            case "Caboclo":
                #Atributos
                self.atributo["Const"] = 0
                self.atributo["For"] = 0
                self.atributo["Dex"] = 0
                self.atributo["Car"] = 0
                self.atributo["Sab"] = 1
                #habilidades
                self.habilidades_possiveis = ["Conhecimento da Floresta", "Medicina Natural", "Comunicação com Animais", "Rituais Espirituais", "Combate com Armas Naturais"]    
                
                #itens iniciais
                self.mochila += [{"Gold":10},"Arco",{"Flecha":20},"Facão","Kit de Sobrevivência","Amuletos e Talismãs","Venenos Naturais"]

        print("-"*20)
        print(f"Sua Constituicao: {self.atributo["Const"]}\nSua Forca: {self.atributo["For"]}\nSua Destreza: {self.atributo["Dex"]}\nSeu Carisma: {self.atributo["Car"]}\nSua Sabedoria: {self.atributo["Sab"]}")
        print("-"*20)
         
    def D6(self):
        D6 = ["""
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
        print(D6[valor])
        return  valor+1
    
    def d20(self):
        for x in range(6):
            d20 = random.randint(0,20)
            tm.sleep(0.2)
            print(f"\r{d20}",end="")
        print()
        return d20