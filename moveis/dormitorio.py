from superclasses.movel import Movel

import time
from pprint import pprint
from copy import deepcopy

# Interativos
class QuartoInterativo(Movel):
    def __init__(self, name, message, itens):
        super().__init__(name, message, itens)
        self.actions = {
            'ajuda': 'retorna as ações possíveis',
            'procurar': 'Procura por intens no %s' % self.name,
            'voltar': 'Parar de mexer no %s: ' % self.name,
            'pegar': 'Pegar um item específico',
            'pegar_todos': 'Pegar todos os itens'
        }

    def list(self):
        print("\nItens no %s" % self.name)
        for k, _ in self.itens.items():
            print(k)

    def play(self, inventory, inv2):

        # display message
        self.olhar()

        # Entra em um novo loop para interação com aquele móvel
        print('O que deseja fazer no %s: ' % self.name)
        while 1:

            try:
                action = input("\nInsira um comando para interagir com %s:\n" % self.name)

                if action == 'ajuda':
                    for key, value in self.actions.items():
                        print("%s: %s" % (key, value))

                if action == 'pegar_todos':
                    return self.pegar_todos()

                if action == 'pegar':
                    return self.pegar()

                if action == 'procurar':
                    self.list()

                if action == 'voltar':
                    break

            except Exception as exception:
                print('Interação inválida')
                break
