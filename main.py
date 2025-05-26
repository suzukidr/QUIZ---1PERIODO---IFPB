import json
import os
import random

# abre o json e ler
def openjson(file):
    with open(file, "r") as fp:
      dados = json.load(fp)
    return dados

def update_util(filename):
    # Ler o conteúdo do arquivo JSON
    with open(filename, 'r', encoding='utf-8') as file:
        dados = json.load(file)
    
    # Percorrer cada grupo de perguntas no arquivo
    for lista_perguntas in dados['perguntas']:
        for q in lista_perguntas:
            # Atualizar o atributo 'util' para True se for False
            if q.get('util') == False:
                q['util'] = True

    # Salvar o conteúdo atualizado nk arquivo JSON
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(dados, file, indent=4)

def update(temp_dict, dados):
  temp_dict["util"] = False
  with open("quests.json", "w") as new:
    new.write(json.dumps(dados, indent=4))
# reiniciar o jogo
def restart():
  escolha = " "
  while escolha: #O loop continuará enquanto 'escolha' for uma string não vazia
    escolha = input("Deseja jogar novamente (S/N) ? ").upper()[0]
    if escolha == "S":
      os.system('cls||clear')
      main()
    else:
      os.system('cls||clear')
      print('jogo encerrado.')
      break

def acerto(premio):
  print(f'Parabéns, você acertou! Prêmio atual {premio}')

def main():  
  n = 0 #nivel
  ajuda = 1
  pulos = 3 #pulos
  p = 0 #pergunta
  premio = 0
  dados = openjson("quests.json")
  alt_lista = ['A','B','C','D']
  while True:
    #exibe a pergunta
    temp = dados["perguntas"][n] #nivel da pergunta
    temp_dict = temp[p] #pergunta a ser feita
    print('='*10)
    if temp_dict["util"] == False:
      p+=1
    elif temp_dict["util"] == True:
      print(temp_dict["quest"])
      for i in temp_dict["alternativas"]: #imprimir alternativas
        print(i) 
      print('='*10)
      #menu
      if pulos >=1 and n <4:
        print(f'Para pular insira "P", você tem {pulos} pulos ')
      print('Para desistir digite (DS)')
      if ajuda == 1:
        print('Para pedir ajuda digite [AJ]')

      print('='*10)
      answer = input("Insira a alternativa: ").upper()[0:2]
      print('='*10)
      os.system('cls||clear')

      #validar pergunta
      if answer == temp_dict["correct"]:
        update(temp_dict, dados)
        n+=1
        p = 0 #
        if n == 1:
          premio += 1000
        if n == 2:
          premio += 10000
        elif n == 3:
          premio += 100000
        elif n == 4:
          premio += 500000
        elif n == 5:
          premio += 1000000
          print((f"Você acertou a pergunta de 1 Milhão! \nSeu prêmio total é de {premio}"))
          break
        acerto(premio)

      #ajudas e desistencia  
      elif answer == "DS":
        print(f"Você deistiu! \nSeu prêmio é de {premio}")
        break
      elif answer == "AJ":
        if ajuda >= 1:
          print("==="*2, 'Ajuda', '==='*2)
          print(temp_dict["correct"], end='|')
          ind = alt_lista.index(temp_dict["correct"])
          del alt_lista[ind]
          print(random.choice(alt_lista))
          ajuda -=1
        else:
          print("você não tem mais ajudas") 
      elif answer == "P":
        if pulos >=1:
          pulos -= 1
          p +=1 # achei
        else:
          continue
      elif answer != temp_dict["correct"]:
        print(f"Você errou!\nSeu prêmio é de {premio / 2}")
        break

main()
restart()
update_util('quests.json')