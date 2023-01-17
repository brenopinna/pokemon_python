from os import system
from time import sleep
from random import randint

class Pokemon:
   def __init__(self, nome, ataque, cura, vida, id):
      self.nome = nome
      self.ataque = int(ataque)
      self.cura = int(cura)
      self.vida_inicial = int(vida)
      self.vida_atual = int(self.vida_inicial)
      self.id = id

   def atacar(self, alvo):
      print(f'{self.nome.upper()} ATACOU {alvo.nome.upper()}')
      print(f'CAUSOU {self.ataque} PONTOS DE DANO!!')
      alvo.vida_atual -= self.ataque

   def curar(self):
      print(f'{self.nome.upper()} USOU A CURA!')
      if(self.vida_atual < self.vida_inicial):
         print(f'RECUPEROU {self.cura} PONTOS DE VIDA!!')
         self.vida_atual += self.cura
         self.atualizaStatus()
         if(self.vida_atual >= self.vida_inicial):
            self.vida_atual = self.vida_inicial
      else:
         print(f'OOPS! OS PONTOS DE VIDA DE {self.nome.upper()} JÁ ESTÃO NO MÁXIMO!')

   def fugir(self):
      titulo(f'{self.nome.upper()} FUGIU!', top=False, bottom=False)

   def get_status(self):
      print(f'STATUS DO {self.id.upper()}:\nNome: {self.nome.upper()}\nAtaque: {self.ataque}\nVida: {self.vida_inicial}\nCura: {self.cura}')

   def atualizaStatus(self):
      print(f'VIDA RESTANTE DE {self.nome.upper()}: {self.vida_atual}')

def linha():
   print('-' * 30)

def titulo(msg, top=True, bottom=True):
   if(top):
      linha()
   print(f'{msg.upper():^30}')
   if(bottom):
      linha()

def defineChanceJogada(jogadasComputador, chances):
   for jogada, chance in chances.items():
      for _ in range(0, chance):
         jogadasComputador.append(jogada)

def msgErro():
   print('OPÇÃO INVÁLIDA!!!')

def listarArray(array, key=None):
   if(key == 'nome'):
      for i,v in enumerate(array):
         print(f'{i + 1}. {v["nome"]}')
   else:
      for i,v in enumerate(array):
         print(f'{i + 1}. {v}')

def validaERetornaInput(array):
   while True:
      try:
         opcao = int(input('>>>> '))
         if(1 <= opcao <= len(array)):
            escolha = array[(opcao - 1)]
            sleep(0.4)
            return escolha
         else:
            msgErro()
      except:
         msgErro()

def limpaTerminal():
   system('cls')

def retornaValorAleatorio(array):
   indice = randint(0, len(array) - 1)
   return array[indice]

def trocaPlayer(player, alvo):
   alvoNovo = player
   playerNovo = alvo
   return playerNovo, alvoNovo
