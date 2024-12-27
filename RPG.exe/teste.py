from InquirerPy import prompt

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