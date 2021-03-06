from superclasses.movel import Movel

import time
from copy import deepcopy


# Interativos
class ArmarioFerramentas(Movel):
    def __init__(self, name, message):
        super().__init__(name, message)
        self.actions = {
            'ajuda': 'retorna as ações possíveis',
            'procurar': 'Procura por intens no %s' % self.name,
            'voltar': 'Parar de mexer no %s: ' % self.name,
            'pegar_item x': 'Pegar o item x',
            'pegar_todos': 'Pegar todos os itens'
        }

    def list(self):
        print("\nItens no %s" % self.name)
        for k in self.nomes:
            print('- '+k)

    def play(self, inventory, inv2):

        # display message
        self.olhar()

        # Entra em um novo loop para interação com aquele móvel

        while True:

            action = input("\nInsira um comando para interagir com %s:\n>>>" % self.name)

            if action == 'ajuda':
                for key, value in self.actions.items():
                    print("%s: %s" % (key, value))

            elif action == 'pegar_todos':
                return self.pegar_todos()

            elif 'pegar' in action:
                ver = action.split()
                if len(ver) == 1:
                    print('você não escolheu nenhum item')
                    continue
                return self.pegar(action.split()[1])

            elif action == 'procurar':
                self.list()

            elif action == 'voltar':
                break
            
            else:
                print('Interação inválida')

class Gerador(Movel):
    # itens esconditos é lista de itens que vai pro inventario depois de quebrar
    def __init__(self, name, message, item_invisivel):
        super().__init__(name, message)
        self.item_invisivel = item_invisivel
        self.actions = {
            'ajuda': 'retorna as ações possíveis',
            'voltar': 'Parar de interagir com %s' % self.name,
            'consertar': 'Tentar consertar a maquina'
        }

    def play(self, inventory, inv2):

        # display message
        self.olhar()

        # Entra em um novo loop para interação com aquele Movel
        while True:

            try:

                action = input("\nInsira um comando para interagir com %s:\n>>>" % self.name)

                if action == 'ajuda':
                    for key, value in self.actions.items():
                        print("%s: %s" % (key, value))

                if action == 'consertar':
                  return self.fix(inventory, inv2)


                if action == 'voltar':
                    break

            except Exception:
                print('Interação inválida')
                continue

    def fix(self, inventory, inventory2):

        # CASO O INVENTARIO ESTEJA VAZIO
        if not inventory.itens:
            print("\nEu preciso de um fusivel de 30a para consertar esse gerador...")
            return False

        # caso as ferramentas não estejam no inventario
        elif 'fusivel30a' not in [i.name for i in inventory.itens]:
            print("\nNão tenho o fusivel certo no meu inventário...")
            return False
        elif self.item_invisivel == []:
            print('Voce ja restaurou a energia')
            return False

        print("Consertando gerador...")
        animation = "|/-\\"
        idx = 0
        while True:
            if idx == 30:
                break
            print(animation[idx % len(animation)], end="\r")
            idx += 1
            time.sleep(0.1)
            ########
            itens_a_passar = deepcopy(self.item_invisivel)
            inventory2.add(itens_a_passar)
            self.item_invisivel = []
            
            print('Você restaurou a energia')

            return False

class ArmarioEletrico(Movel):
    # itens esconditos é lista de itens que vai pro inventario depois de quebrar
    def __init__(self, name, message, itens_escondidos):
        super().__init__(name, message)
        self.itens_escondidos = itens_escondidos
        self.actions = {
            'ajuda': 'retorna as ações possíveis',
            'voltar': 'Parar de interagir com %s' % self.name,
            'abrir': 'Tentar abrir o armario'
        }

    def play(self, inventory, inv2):

        # display message
        self.olhar()

        # Entra em um novo loop para interação com aquele Movel
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
        elif 'energia' not in [i.name for i in inventory2.itens]:
            print("\nNão liguei a energia ainda...")
            return False
        elif self.itens_escondidos == []:
            print('Voce ja abriu esse armario')
            return False
        
        print("abrindo armário...")
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
            
            print('Você pegou um pe de cabra')

            return False
          

