class Item:
    """
      Super classe para itens abstratos
    """

    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __str__(self):
        return self.name

    def olhar(self):
      print(self.message)