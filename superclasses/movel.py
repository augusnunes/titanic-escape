class Movel:
    """
      Super class to abstract furnitures
    """

    def __init__(self, name, message):
        self.name = name
        self.message = message
        self.itens = []
        self.nomes = []

    def olhar(self):
        """
            Method that display the description of the furniture
        """
        print(self.message)

    def pegar_todos(self):
        """
            Method to that returns to the player all the itens in the furniture \
          and clear the itens list
        """
        if len(self.itens):
            all_itens = [i for i in self.itens]
            self.itens = []
            self.nomes = []
            print('Você pegou todos os itens')
            return all_itens

        else:
            return []  

    def pegar(self, item):
        """
            Method that returns to the player the item requested
        """
        # try:
        if item in self.nomes:
            for i in range(len(self.nomes)):
                if item == self.nomes[i]:
                    r = self.itens.pop(i)
                    self.nomes.pop(i)
                    print(f'Você pegou o item {item}!')
                    return r
        else:
            print("%s é um item inválido" % item)
        # except Exception as e:
        #     ## In case the player inputs nonsense
        #     print("%s é um item inválido" % item)
        #     return None

    def store_item(self, item):
        self.itens.append(item)
        self.nomes.append(item.name)
    