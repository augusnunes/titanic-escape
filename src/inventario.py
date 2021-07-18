class Inventario:
    def __init__(self):
        self.itens = []

    def list(self):
        for i in self.itens:
            i.printa()

    def insert(self, item):
        """
        :param items: lista de itens a serem guardados
        """
        self.itens.append(item)
