
# player inventory
class Inventory:

    def __init__(self):
        self.itens = []

    def add(self, item):
        self.itens += item

    def remove(self, name):
        self.itens = [i for i in self.itens if i.name != name]

    def check(self, nome_do_item):
        '''
            Verifica se um item esta no inventario
            nome_do_item: str
        '''
        esta = False
        for item in self.itens:
            if item.name == nome_do_item:
                esta = True
        return esta

    def __str__(self):
        title = "\nSeu inventário contém os seguintes itens:\n"
        return title + "\n".join([i.name for i in self.itens])