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

from os.path import isfile
from joblib import dump, load

inv1 = './classes/inv1.joblib'
inv2 = './classes/inv2.joblib'
sce = './classes/sce.joblib'

def init():
    if isfile(inv1) and isfile(inv2) and isfile(sce):
        return load(inv1), load(inv2), load(sce)
    else:
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
        ######################################################
        # create all furnitures
        #------------------------------------------------------
        
        ## Maquinario
        # Não Interativos
        motor = MovelNaoIter('motor', 'Que motorzão') 
        mapa = MovelNaoIter('mapa', 'Um mapa da Bahia... mas nem na Bahia estamos...')
        mesa = MovelNaoIter('mesa', 'Esta mesa está meio suja')
        # Interativos
        armario = ArmarioFerramentas('armario_ferramentas', 'Armário com ferramentas comuns de trabalho')
        gerador = Gerador('gerador', 'Um gerador... devo conseguir energia com isso aqui', [energia])
        armario_eletrico = ArmarioEletrico('armario_eletrico', 'O que será que tem aqui dentro?', [pe_de_cabra])

        ##Dormitório
        # Não interativos
        cabine = MovelNaoIter('cabine','Uau, a cabine do capitão, chique demais!!')
        quartob = MovelNaoIter('quarto_b','O quarto do Charles, parece que não tem nada aqui')
        quartoc = MovelNaoIter('quarto_c','O quarto do Jeff, eu não tenho como entrar aqui')
        # Interativos
        quartoa = QuartoInterativo('quarto_a','O quarto do Jesus. Parece que tem algo aqui...') # falta criar
        meu_quarto = QuartoInterativo('meu_quarto','Meu quarto: aquilo deve estar aqui...')


        ##Convés
        # Não Interativos
        bocha = MovelNaoIter('bocha','Pena que o navio está afundado, seria ótimo uma partidinha')
        tele_esti = MovelNaoIter('vista_estibordo','Puxa vida mas que vista!!!')
        tele_bomb = MovelNaoIter('vista_bombordo','Uma bela visão')
        # Interativos
        maquina_pesada = MaquinaPesada('maquina_pesada','Posso tentar procurar um fusivel aqui',[fusivel30a])
        bote = Bote('bote','Esse bote eh minha saida desse navio!!')

        ##Saguão##
        # Não interativos
        bar = MovelNaoIter('bar', 'ai se eu tivesse tempo pra uma bebida')
        mesa_pong = MovelNaoIter('tenis_de_mesa', 'na minha terra isso eh ping pong... e eu era o brabo')
        sofa = MovelNaoIter('sofa', 'queria mimir! Mas não dá tempo, fiquei com Deus')
        # Interativos
        radio = Radio('radio', 'Eu posso desmontar para tentar encontrar um fusivel', [fusivel13a])
        tv = Tv('tv', 'Aqui deve ter um fusível hein...', [fusivel20a])
        cofre = Cofre('cofre', 'Um cofre... preciso de energia e da senha pra abri-lo',[chave])


        # store all items inside furnitures
        armario.store_item(ferramentas)
        meu_quarto.store_item(relogio)
        quartoa.store_item(carta)


        ######################################################
        # create all environments
        #------------------------------------------------------
        
        maquinario = Environment('Maquinário','O maquinário do navio, contém máquinas pesadas e algumas ferramentas')
        dormitorio = Environment('Dormitório', 'O dormitório, contém alguns objetos pessoas dos passageiros' )
        saguao = Environment('Saguão', 'Locar de lazer do navio')
        conves = Environment('Convés', 'Eu vejo um bote, a unica maneira de sair daqui com vida')

        # add furnitures to environment
        ### MOVEIS MAQUINARIO
        maquinario.add_furniture(mapa, 1)
        maquinario.add_furniture(armario,0)
        maquinario.add_furniture(mesa, 3)
        maquinario.add_furniture(motor, 4)
        maquinario.add_furniture(gerador, 2)
        maquinario.add_furniture(armario_eletrico,5)


        ### MOVEIS DORMITORIO
        dormitorio.add_furniture(quartoa, 0)
        dormitorio.add_furniture(quartob,1)
        dormitorio.add_furniture(cabine,2)
        dormitorio.add_furniture(quartoc,3)
        dormitorio.add_furniture(meu_quarto,4)


        ### MOVEIS CONVES
        conves.add_furniture(bocha, 0)
        conves.add_furniture(tele_bomb, 1)
        conves.add_furniture(tele_esti, 4)
        conves.add_furniture(maquina_pesada, 3)
        conves.add_furniture(bote, 5)


        ### MOVEIS SAGUÃO
        saguao.add_furniture(bar, 1)
        saguao.add_furniture(mesa_pong, 2)
        saguao.add_furniture(sofa, 4)
        saguao.add_furniture(radio, 5)
        saguao.add_furniture(tv, 3)
        saguao.add_furniture(cofre, 0)

        # initialize scenario object
        scenario = Scenario() # adicionando ambientes ao contrário
        scenario.add_environment(conves)
        scenario.add_environment(saguao)
        scenario.add_environment(dormitorio)
        scenario.add_environment(maquinario)

        # create player inventory
        inventory = Inventory()
        inventory2 = Inventory()

        dump(inventory, inv1)
        dump(inventory2, inv2)
        dump(scenario, sce)

        return inventory, inventory2, scenario