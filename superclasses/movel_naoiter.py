from superclasses.movel import Movel

class MovelNaoIter(Movel):
    def __init__(self, name, message):
        super().__init__(name, message, {})
        self.actions = {'voltar': 'Parar de interagir com %s: ' % self.name}

    def play(self, inventory, inv2):
        # display message
        print(self.message)