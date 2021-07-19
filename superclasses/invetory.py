
# player inventory
class Inventory:
    '''Classe que representa o inventário do jogador
    '''

    def __init__(self):
        self.itens = []
        self.nomes = [] ### implementar isso

    def add(self, item):
        if type(item) == list:
            for i in item:
                self.itens.append(i)
                self.nomes.append(i.name)                
        else:
            self.itens.append(item)
            self.nomes.append(item.name)
        

    def remove(self, name):
        for i in range(len(self.itens)):
            if self.nomes[i] == name:
                self.nomes.pop(i)
                self.itens.pop(i)
                return True 
        return False

    def check(self, nome_do_item):
        '''
            Verifica se um item esta no inventario
            nome_do_item: str
        '''
        return nome_do_item in self.nomes

    def __str__(self):
        title = "\nSeu inventário contém os seguintes itens:\n"
        return title + "\n".join(['-'+i for i in self.nomes])