from superclasses.movel import Movel

import time
from pprint import pprint
from copy import deepcopy

# Interativos
class Bote(Movel):
    
    def __init__(self, name, message, itens):
        super().__init__(name, message, itens)
        self.actions = {
            'ajuda': 'Retorna as ações possíveis',
            'voltar': 'Parar de interagir com %s' % self.name,
            'soltar': 'Tentar soltar o bote'
        }

    def play(self, inventory, inv2):

        # display message
        self.olhar()

        # Entra em um novo loop para interação com aquele móvel
        while 1:

            try:

                action = input("\nInsira um comando para interagir com %s:\n" % self.name)

                if action == 'ajuda':
                    for key, value in self.actions.items():
                        print("%s: %s" % (key, value))

                if action == 'soltar':
                    return self.soltar(inventory)


                if action == 'voltar':
                    break

            except Exception:
                print('Interação inválida')
                continue

    def soltar(self, inventory):

        # CASO O INVENTARIO ESTEJA VAZIO
        if not inventory.itens:
            print("\nEu preciso de algo para soltar esse bote a chave para liga-lo...")
            return False

        # caso as ferramentas não estejam no inventario
        if 'pe_de_cabra' and 'chave' not in [i.name for i in inventory.itens]:
            print("\nPreciso do pe-de-cabra e da chave para ligar esse bote...")
            return False

        print("libertando o bote...")
        animation = "|/-\\"
        idx = 0
        while 1:
            if idx == 30:
                break
            print(animation[idx % len(animation)], end="\r")
            idx += 1
            time.sleep(0.1)
        print('Aeeeee, bora vazaaaaaar')
        return True
      

class MaquinaPesada(Movel):
    # itens esconditos é lista de itens que vai pro inventario depois de quebrar
    def __init__(self, name, message, itens, itens_escondidos):
        super().__init__(name, message, itens)
        self.itens_escondidos = itens_escondidos
        self.actions = {
            'ajuda': 'retorna as ações possíveis',
            'voltar': 'Parar de interagir com %s' % self.name,
            'desmontar': 'Tentar desmontar a maquina'
        }

    def play(self, inventory, inv2):

        # display message
        self.olhar()

        # Entra em um novo loop para interação com aquele móvel
        while 1:

            try:

                action = input("\nInsira um comando para interagir com %s:\n" % self.name)

                if action == 'ajuda':
                    for key, value in self.actions.items():
                        print("%s: %s" % (key, value))

                if action == 'desmontar':
                  return self.desmontar(inventory)


                if action == 'voltar':
                    break

            except Exception:
                print('Interação inválida')
                continue

    def desmontar(self, inventory):

        # CASO O INVENTARIO ESTEJA VAZIO
        if not inventory.itens:
            print("\nEu preciso de algo para abrir essa maquina...")
            return False

        # caso as ferramentas não estejam no inventario
        elif 'ferramentas' not in [i.name for i in inventory.itens]:
            print("\nNão tenho uma caixa de ferramentas no meu inventário...")
            return False

        elif self.itens_escondidos == []:
            print('Voce ja mexeu nessa maquina')
            
        else:
            print("Abrindo a maquina...")

            animation = "|/-\\"
            idx = 0
            while 1:
                if idx == 30:
                    break
                print(animation[idx % len(animation)], end="\r")
                idx += 1
                time.sleep(0.1)
            itens_a_passar = deepcopy(self.itens_escondidos)
            inventory.add(itens_a_passar)
            self.itens_escondidos = []

            print('Um fusivel foi adicionado ao seu inventário')

            return False