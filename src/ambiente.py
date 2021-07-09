class Ambiente:
    def __init__(self, id, is_iluminated=False):
        self.itens = None
        self.is_iluminated = is_iluminated 
        self.id = id
    
    def set_itens(self, itens):
        self.itens = itens

    def printa_itens(self):
        print("Itens: ")
        for i in self.itens:
            print('- '+i.name)
        print("~~~~~~~~~~~~~~~~~~~~~~~~\n")

    def procura(self):
        if self.is_iluminated:
            self.printa_itens()
    
    def pega_todos(self):
        return self.itens 
    
    def pega(self, name):
        for i in self.itens:
            if i.name == name:
                return i 
        print("Não foi encontrado!")


