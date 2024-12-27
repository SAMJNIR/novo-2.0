from InquirerPy import prompt

# função que cria prompt com opções basicas de guia como batalhar, escolher direção, acessar inventário, classes e habilidades
def opçõesDeEntrada():
 
 questões =[{
  
        'type': 'list',
        'name': 'entrada',
        'message': 'O que deseja fazer?',
        'choices': ['batalha', 'direção', 'inventário', 'classes', 'habilidades']

             }]
 
 resposta = prompt(questões)
 return resposta['entrada']


#função que retorna opções de batalha (OBS: PODE SE ADICIONAR MAIS COMPLEXIDADE)
def Batalha():
 
   questões = [{
           
     "type":"list",
    "message":"Oque voce quer fazer?",
    "name":"batalha",
    "choices":["Enfrentar","Fugir","Falar com o inimigo"]

              }]
   resposta = prompt(questões)
   return resposta['batalha']


#função que retorna opções de navegação (OBS: PODE SE ADICIONAR MAIS COMPLEXIDADE)
def Direção():
  
  questões = [{

      "type":"list",
      "message":"Para qual direção deseja seguir?",
      "name":"direção",
      "choices":["NORTE","SUL","LESTE","OESTE"]

              }]
  resposta = prompt(questões)
  return resposta ['direção']


#função que retorna opções de acesso ao inventário
def Inventário():
    
    def quererAcessarInventário(): #função que retorna opção de acesso ao inventário
        questoes = [{
            "type": "confirm",
            "message": "Olhar itens da mochila?",
            "name": "proceed",
            "default": True
        }]
        resposta = prompt(questoes)
        return resposta["proceed"]

    
    def acessarInventario(mochila): #função que acessa o inventário
        questoes = [{
            "type": "list",
            "message": "Qual Item?",
            "name": "itens",
            "choices": mochila
        }]
        resposta = prompt(questoes)
        return resposta["itens"]

    mochila = ["espada", "escudo", "poção"] #inicializar a mochila com alguns itens (EXEMPLO)

    if quererAcessarInventário():
        item_selecionado = acessarInventario(mochila)
        print(f"Você selecionou o item: {item_selecionado}")

#função que retorna opções para escolha de classes (OBS: PODE SE ADICIONAR MAIS COMPLEXIDADE)
def Classes():
 
 questões = [{

    "type":"list",
    "message":"Qual classe você escolherá?",
    "name":"classes",
    "choices": ["Capoerista","Contrabandista","Pistoleiro","Rezadeira","Tocador de Forro","Barqueiro"]

             }]
 
 resposta = prompt(questões)
 resposta = ["classes"]
 return resposta

#função que retorna a opção de ver suas habilidades pré definidas (OBS: PODE SE ADICIONAR MAIS COMPLEXIDADE)
def Habilidades():

 questões = [{ 
  
    "type":"list",
    "message":"Suas habilidades",
    "name":"habilidades",
    "choices": habilidades

              }]
 
 resposta = prompt(questões)
 resposta = questões["habilidades"]

 habilidades = "soco", 'chute', 'esquiva' #exemplo de habilidades iniciais

 return resposta