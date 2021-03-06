#########  UNIAO  #########

# import required libraries
from init_classes import init

def main():
    ''' Classe principal, que reconhece as ações de movimentação 
    e interação do jogador
    '''
    inventory, inventory2, scenario = init()

    # list all available actions
    available_actions = {
    'sair': 'Sai do jogo',
    'ajuda': 'Mostra os comandos possíveis',
    'inventario ou inv': 'Abre inventario',
    'direita ou dir': 'Vai para a sala da direita',
    'esquerda ou esq': 'Vai para a sala da esquerda',
    'interagir ou int': 'Interage com moveis da sala',
    'olhar': 'Dá descrição de itens e móveis'
    }

    room = scenario.head
    print(room)

    while True:
        # pede ação ao jogador
        action = input("\nInsira uma ação: \n>>>").lower()
        
        # sai do jogo
        if action == 'sair':
            break
            
        # mostra a ajuda
        elif action == 'ajuda':
            for key, value in available_actions.items():
                print("%s: %s" % (key, value))
                
        elif action == 'inventario' or action == "inv":
            print(inventory)
        #elif action == 'inventario2': 
            #print(inventory2)

        ## Ações de movimentação
            
        elif action == 'direita' or action == "dir":
            room = room.gonext()
            
        elif action == 'esquerda' or action == "esq":
            room = room.goprev()

            
        # interação com os elementos
        elif 'interagir' in action or 'int' in action:
            try:
                print(room)
                # get the desired furniture
                movel = action.split()[1]
                resp = room.data.get_furniture(movel).play(inventory, inventory2)
    
                if movel == 'bote' and resp:
                    print("Parabens, você conseguiu sair do navio!!")
                    print('Fim de jogo, muito obrigado por jogar!')
                    break
    
                if resp:
                    # add item to the player inventory
                    inventory.add(resp)
            except:
                print('Comando invalido')


        # ação de olhar
        elif 'olhar' in action:
            print(room)
            objeto_para_olhar = action.split()
            if len(objeto_para_olhar) == 2:
                try:
                    objeto_para_olhar = objeto_para_olhar[1]
                    
                    # se o objeto para olhar é o ambiente
                    ambiente_atual = room.data.name.lower()
                    if objeto_para_olhar == ambiente_atual:
                        print(room.data.descricao)
    
                    # se o objeto para olhar é um item do inventário
                    elif inventory.check(objeto_para_olhar):
                        for item in inventory.itens:
                            if item.name == objeto_para_olhar:
                                print(item.message)
    
                    # se o objeto para olhar é um móvel
                    else:
                        movel = room.data.get_furniture(objeto_para_olhar)
                        movel.olhar()
                except:
                    print('Objeto inválido')
            
            else:
                print("Comando inválido")
        else:
            print('Interação inválida\n')


if __name__=="__main__":
    print("TITANIC SCAPE")
    print('~~~~~~~~~~~~~\n\n')
    historia = './historia.txt'
    print(open(historia).read())
    input('\n\nDigite qualquer coisa para continuar...\n')
    main()