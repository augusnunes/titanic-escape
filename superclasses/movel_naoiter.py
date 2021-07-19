from superclasses.movel import Movel

class MovelNaoIter(Movel):
    ''' Classe de móveis não interativos, apenas retorna uma mensagem contendo
    uma breve descrição do móvel
    '''
    def __init__(self, name, message):
        super().__init__(name, message)
        self.actions = {'voltar': 'Parar de interagir com %s: ' % self.name}

    def play(self, inventory, inv2):
        # display message
        print(self.message)