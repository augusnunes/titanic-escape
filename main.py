#########  UNIAO  #########

# import required libraries
from superclasses.movel_naoiter import MovelNaoIter
from superclasses.invetory import Inventory
from superclasses.scenario import Scenario
from superclasses.environment import Environment
from superclasses.item import Item

from moveis.maquinario import *
from moveis.conves import *
from moveis.saguao import *
from moveis.dormitorio import *

import time
from pprint import pprint
from copy import deepcopy


# initialize scenario object
scenario = Scenario()

# create all environments
maquinario = Environment('Maquinário','O maquinário do navio, contém máquinas pesadas e algumas ferramentas',{})
dormitorio = Environment('Dormitório', 'O dormitório, contém alguns objetos pessoas dos passageiros' ,{})
saguao = Environment('Saguão', 'Locar de lazer do navio' ,{})
conves = Environment('Convés', 'Eu vejo um bote, a unica maneira de sair daqui com vida' ,{})


# create all items
ferramentas = Item('ferramentas','Uma caixa simples com ferramentas')
fusivel13a = Item('fusivel13a','um fusivel de 13 Amperes')
fusivel20a = Item('fusivel20a','um fusivel de 20 Amperes')
fusivel30a = Item('fusivel30a','um fusivel de 30 Amperes')
energia = Item('energia','energia que ngm ve, escondidinha no inventario q ngm ve hehe')
pe_de_cabra = Item('pe_de_cabra', 'um pe de cabra... da pra usar de alavanca, ou ate quebrar algo')
relogio = Item('relogio','Mds, o relogio que meu pai me deu. Nunca que eu sairia desse navio sem isso!!!')
chave = Item('chave','Aaah, a chave do bote: bora sair daquii!')
carta = Item('carta', """Querida Julia,

Sei que muita gente não se importa com você e que quase todo mundo te ignora, mas saiba do teu valor,mulher! Você consegue se sair bem em tudo que faz e além de tudo é rápida. Olha, se o pessoal soubesse que você é bem mais legal que seu pai... Sério, o mundo seria diferente.

Te amo 77815 vezes mais do que qualquer um dos seus parentes (Cenelson, Pai Tom, Tia Mat, Tia Rub, Primo Lisp, ...).
Beijos do Seu Adimirador
-j
""")

## create all furnitures

## Maquinario
# Não Interativos
motor = MovelNaoIter('motor', 'Que motorzão') 
mapa = MovelNaoIter('mapa', 'Um mapa da Bahia... mas nem na Bahia estamos...')
mesa = MovelNaoIter('mesa', 'Esta mesa está meio suja')
# Interativos
armario = ArmarioFerramentas('armario_ferramentas', 'Armário com ferramentas comuns de trabalho', {})
gerador = Gerador('gerador', 'Um gerador... devo conseguir energia com isso aqui',{},[energia])
armario_eletrico = ArmarioEletrico('armario_eletrico', 'O que será que tem aqui dentro?', {},[pe_de_cabra])

##Dormitório
# Não interativos
cabine = MovelNaoIter('cabine','Uau, a cabine do capitão, chique demais!!')
quartob = MovelNaoIter('quarto_b','O quarto do Charles, parece que não tem nada aqui')
quartoc = MovelNaoIter('quarto_c','O quarto do Jeff, eu não tenho como entrar aqui')
# Interativos
quartoa = QuartoInterativo('quarto_a','O quarto do Jesus. Parece que tem algo aqui...',{}) # falta criar
meu_quarto = QuartoInterativo('meu_quarto','Meu quarto: aquilo deve estar aqui...',{})


##Convés
# Não Interativos
bocha = MovelNaoIter('bocha','Pena que o navio está afundado, seria ótimo uma partidinha')
tele_esti = MovelNaoIter('vista_estibordo','Puxa vida mas que vista!!!')
tele_bomb = MovelNaoIter('vista_bombordo','Uma bela visão')
# Interativos
maquina_pesada = MaquinaPesada('maquina_pesada','Posso tentar procurar um fusivel aqui',{},[fusivel30a])
bote = Bote('bote','Esse bote eh minha saida desse navio!!',{})

##Saguão##
# Não interativos
bar = MovelNaoIter('bar', 'ai se eu tivesse tempo pra uma bebida')
mesa_pong = MovelNaoIter('tenis_de_mesa', 'na minha terra isso eh ping pong... e eu era o brabo')
sofa = MovelNaoIter('sofa', 'queria mimir! Mas não dá tempo, fiquei com Deus')
# Interativos
radio = Radio('radio', 'Eu posso desmontar para tentar encontrar um fusivel', {}, [fusivel13a])
tv = Tv('tv', 'Aqui deve ter um fusível hein...', {}, [fusivel20a])
cofre = Cofre('cofre', 'Um cofre... preciso de energia e da senha pra abri-lo',{},[chave])

# store all items inside furnitures
armario.store_item(ferramentas)
meu_quarto.store_item(relogio)
quartoa.store_item(carta)

# add environments to the scenario
scenario.add_environment(maquinario, '1')
scenario.add_environment(dormitorio,'2')
scenario.add_environment(saguao,'3')
scenario.add_environment(conves,'4')

# add furnitures to environment
### MOVEIS MAQUINARIO
maquinario.add_furniture(mapa, '2')
maquinario.add_furniture(armario,'1')
maquinario.add_furniture(mesa, '4')
maquinario.add_furniture(motor, '5')
maquinario.add_furniture(gerador, '3')
maquinario.add_furniture(armario_eletrico,'6')


## MOVEIS DORMITORIO
dormitorio.add_furniture(quartoa,'1')
dormitorio.add_furniture(quartob,'2')
dormitorio.add_furniture(cabine,'3')
dormitorio.add_furniture(quartoc,'4')
dormitorio.add_furniture(meu_quarto,'5')


## MOVEIS CONVES
conves.add_furniture(bocha,'1')
conves.add_furniture(tele_bomb,'2')
conves.add_furniture(tele_esti,'5')
conves.add_furniture(maquina_pesada,'4')
conves.add_furniture(bote,'6')


## MOVEIS SAGUÃO
saguao.add_furniture(bar,'2')
saguao.add_furniture(mesa_pong,'3')
saguao.add_furniture(sofa,'5')
saguao.add_furniture(radio,'6')
saguao.add_furniture(tv,'4')
saguao.add_furniture(cofre,'1')


# create player inventory
inventory = Inventory()
inventory2 = Inventory()

# list all available actions
available_actions = {
  'sair': 'Sai do jogo',
  'ajuda': 'Mostra os comandos possíveis',
  'inventario': 'Abre inventario',
  'direita': 'Vai para a sala da direita',
  'esquerda': 'Vai para a sala da esquerda',
  'interagir': 'Interage com moveis da sala',
  'olhar': 'Dá descrição de itens e móveis'
}

        
# main
print(scenario)
while True:
      
    # try:

    # pede ação ao jogador
    action = input("\nInsira uma ação: ").lower()
    
    # sai do jogo
    if action == 'sair':
        break
        
    # mostra a ajuda
    elif action == 'ajuda':
        for key, value in available_actions.items():
            print("%s: %s" % (key, value))
            
    elif action == 'inventario':
        print(inventory)
    #elif action == 'inventario2': 
        #print(inventory2)

    ## Ações de movimentação
        
    elif action == 'direita':

        # faz o que precisa
        scenario.direita()
        print(scenario)
        
    elif action == 'esquerda':

        # faz o que precisa
        scenario.esquerda()
        print(scenario)

        
    # interação com os elementos
    elif 'interagir' in action:
        print(scenario)
        # get the desired furniture
        movel = action.split()[1]
        resp = scenario.get_env_by_name(movel).play(inventory, inventory2)

        if movel == 'bote' and resp:
            print("Parabens, você conseguiu sair do navio!!")
            break

        if resp:

            # add item to the player inventory
            inventory.add(resp)


    # ação de olhar
    elif 'olhar' in action:
        print(scenario)
        objeto_para_olhar = action.split()[1]

        # se o objeto para olhar é o ambiente
        ambiente_atual = scenario.envs[scenario.actual].name.lower()
        if objeto_para_olhar == ambiente_atual:
            print(scenario.envs[scenario.actual].descricao)

        # se o objeto para olhar é um item do inventário
        elif inventory.check(objeto_para_olhar):
                for item in inventory.itens:
                    if item.name == objeto_para_olhar:
                        print(item.message)

        # se o objeto para olhar é um móvel
        else:
            movel = scenario.get_env_by_name(objeto_para_olhar)
            movel.olhar()
    else:
        print('Interação inválida\n')

    # except Exception as exception:
    #     continue