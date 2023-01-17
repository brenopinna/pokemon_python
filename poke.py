from defs import *
from time import sleep

# Declaração dos pokemons e jogadas

pokemons = [
   {'nome':'charmander',
   'ataque': 20,
   'cura':10,
   'vida':100},
   {'nome':'squirtle',
   'ataque': 20,
   'cura':10,
   'vida':100},
   {'nome':'bulbasauro',
   'ataque': 20,
   'cura':10,
   'vida':100},
]

jogadasUsuario = ['atacar','curar','fugir']

jogadasComputador = []
chances = {
      'atacar':70,
      'curar':29,
      'fugir':1
}
defineChanceJogada(jogadasComputador,chances)
######################################
# Criação dos objetos Pokemon

limpaTerminal()
titulo('BATALHA POKÉMON!')


print('Qual pokémon você deseja?')
listarArray(pokemons, 'nome')
pokemonUsuarioID = validaERetornaInput(pokemons)
pokemonUsuario = Pokemon(
   pokemonUsuarioID['nome'],
   pokemonUsuarioID['ataque'],
   pokemonUsuarioID['cura'],
   pokemonUsuarioID['vida'],
   'Usuário'
)
limpaTerminal()

pokemonUsuario.get_status()
input('Pressione Enter para continuar.')
linha()

pokemonInimigoID = retornaValorAleatorio(pokemons)
pokemonInimigo = Pokemon(
   pokemonInimigoID['nome'],
   pokemonInimigoID['ataque'],
   pokemonInimigoID['cura'],
   pokemonInimigoID['vida'],
   'Inimigo'
)

pokemonInimigo.get_status()
input('Pressione Enter para continuar.')

limpaTerminal()
if(pokemonUsuario.nome == pokemonInimigo.nome):
   pokemonInimigo.nome += '(2)'
titulo(f'{pokemonUsuario.nome} VS. {pokemonInimigo.nome}', bottom=False)
######################################
# Loop do jogo
vencedor = ''
jogadorDaVez = pokemonUsuario
jogadorPassivo = pokemonInimigo
while True:
   if(jogadorDaVez == pokemonUsuario):
      linha()
      sleep(0.7)
      print('O que deseja fazer?')
      listarArray(jogadasUsuario)
      jogada = validaERetornaInput(jogadasUsuario)
   elif(jogadorDaVez == pokemonInimigo):
      jogada = retornaValorAleatorio(jogadasComputador)
      sleep(0.7)
   linha()
   if(jogada == 'atacar'):
         jogadorDaVez.atacar(jogadorPassivo)
         if(jogadorPassivo.vida_atual <= 0):
            vencedor = jogadorDaVez
            break
         jogadorPassivo.atualizaStatus()
   elif(jogada == 'curar'):
      jogadorDaVez.curar()
   elif(jogada == 'fugir'):
      jogadorDaVez.fugir()
      vencedor = jogadorPassivo
      break
   jogadorDaVez, jogadorPassivo = trocaPlayer(jogadorDaVez, jogadorPassivo)
################################
# Fim do Jogo
if(vencedor == pokemonUsuario):
   titulo(f'{vencedor.nome} VENCEU!!')
else:
   titulo('VOCÊ PERDEU!')
titulo('FIM DE JOGO!', False)