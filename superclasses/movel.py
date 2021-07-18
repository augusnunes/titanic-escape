class Movel:
    """
      Super class to abstract furnitures
    """

    def __init__(self, name, message, itens):
        self.name = name
        self.message = message
        self.itens = itens

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
            all_itens = list(self.itens.values())
            all_itens = [i for i in all_itens]
            self.itens = {}
            print('Você pegou todos os itens')

            return list(all_itens)

        else:
            return []  

    def pegar(self):
        """
            Method that returns to the player the item requested
        """
        try:

            print("Selecione um item:")
            for i in self.itens:
              print(i)

            item = input("Qual item você deseja pegar? ")
            item = self.itens[item]
            self.itens = {k:v for k,v in self.itens.items()}
            print('Você pegou o item')

            return [item]

        except Exception as e:
            ## In case the player inputs nonsense
            print("%s é um item inválido" % item)
            return None

    def store_item(self, item):
        self.itens[item.name] = item