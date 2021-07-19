from superclasses.movel import Movel

import time
from pprint import pprint
from copy import deepcopy


# Interativos
class Cofre(Movel):
    # itens esconditos é lista de itens que vai pro inventario depois de quebrar
    def __init__(self, name, message, itens_escondidos):
        super().__init__(name, message)
        self.itens_escondidos = itens_escondidos
        self.actions = {
            'ajuda': 'retorna as ações possíveis',
            'voltar': 'Parar de interagir com %s' % self.name,
            'abrir': 'Tentar abrir o cofre'
        }

    def play(self, inventory, inv2):

        # display message
        self.olhar()

        # Entra em um novo loop para interação com aquele móvel
        while True:

            try:

                action = input("\nInsira um comando para interagir com %s:\n>>>" % self.name)

                if action == 'ajuda':
                    for key, value in self.actions.items():
                        print("%s: %s" % (key, value))

                if action == 'abrir':
                  return self.abrir(inventory, inv2)


                if action == 'voltar':
                    break

            except Exception:
                print('Interação inválida')
                continue

    def abrir(self, inventory, inventory2):

        # CASO O INVENTARIO ESTEJA VAZIO
        if not inventory2.itens:
            print("\nEu preciso de energia pra abrir esse armário...")
            return False
        
        # caso as ferramentas não estejam no inventario
        elif self.itens_escondidos == []:
            print('Voce ja abriu esse cofre')
            return False
            
        if 'energia' not in [i.name for i in inventory2.itens]:
            print("\nNão liguei a energia ainda...")
            return False
        senha = str(input('Agora que tem energia, posso por a senha de 5 digitos: '))
        if senha == '77815':
            print("abrindo cofre...")
            animation = "|/-\\"
            idx = 0
            while 1:
                if idx == 30:
                    break
                print(animation[idx % len(animation)], end="\r")
                idx += 1
                time.sleep(0.1)
                ########
                itens_a_passar = deepcopy(self.itens_escondidos)
                inventory.add(itens_a_passar)
                self.itens_escondidos = []

                print('Você pegou a chave do bote')
                return False
        else:
          print('Ih, nao eh essa senha nao...')

          return False

class Tv(Movel):
    # itens esconditos é lista de itens que vai pro inventario depois de quebrar
    def __init__(self, name, message, itens_escondidos):
        super().__init__(name, message)
        self.itens_escondidos = itens_escondidos
        self.actions = {
            'ajuda': 'retorna as ações possíveis',
            'voltar': 'Parar de interagir com %s' % self.name,
            'desmontar': 'Tentar desmontar a Televisão'
        }

    def play(self, inventory, inv2):

        # display message
        self.olhar()

        # Entra em um novo loop para interação com aquele móvel
        while True:

            try:

                action = input("\nInsira um comando para interagir com %s:\n>>>" % self.name)

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
            print("\nEu preciso de algo para abrir essa Tv...")
            return False

        # caso as ferramentas não estejam no inventario
        elif 'ferramentas' not in [i.name for i in inventory.itens]:
            print("\nNão tenho uma caixa de ferramentas no meu inventário...")
            return False

        elif self.itens_escondidos == []:
            print('Voce ja abriu a televisão')
            
        else:
            print("Abrindo a Televisão...")

            animation = "|/-\\"
            idx = 0
            while True:
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

class Radio(Movel):
    # itens esconditos é lista de itens que vai pro inventario depois de quebrar
    def __init__(self, name, message, itens_escondidos):
        super().__init__(name, message)
        self.itens_escondidos = itens_escondidos
        self.actions = {
            'ajuda': 'retorna as ações possíveis',
            'voltar': 'Parar de interagir com %s' % self.name,
            'desmontar': 'Tentar desmontar o radio'
        }

    def play(self, inventory, inv2):

        # display message
        self.olhar()

        # Entra em um novo loop para interação com aquele móvel
        while True:

            try:

                action = input("\nInsira um comando para interagir com %s:\n>>>" % self.name)

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
            print("\nEu preciso de algo para abrir o rádio...")
            return False

        # caso as ferramentas não estejam no inventario
        elif 'ferramentas' not in [i.name for i in inventory.itens]:
            print("\nNão tenho uma caixa de ferramentas no meu inventário...")
            return False

        elif self.itens_escondidos == []:
            print('Voce ja abriu esse aparelho')
            
        else:
            print("Abrindo o radio...")

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