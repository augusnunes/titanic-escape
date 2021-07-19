from superclasses.movel import Movel

# Interativos
class QuartoInterativo(Movel):
    def __init__(self, name, message):
        super().__init__(name, message)
        self.actions = {
            'ajuda': 'retorna as ações possíveis',
            'procurar': 'Procura por intens no %s' % self.name,
            'voltar': 'Parar de mexer no %s: ' % self.name,
            'pegar': 'Pegar um item específico',
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

            # try:
            action = input("\nInsira um comando para interagir com %s:\n>>>" % self.name)

            if action == 'ajuda':
                for key, value in self.actions.items():
                    print("%s: %s" % (key, value))

            elif action == 'pegar_todos':
                return self.pegar_todos()

            elif 'pegar' in action:
                return self.pegar(action.split()[1])

            elif action == 'procurar':
                self.list()

            elif action == 'voltar':
                break
            
            else:
                print('Interação inválida')

            # except Exception as exception:
            #     print('Interação inválida')
            #     break

