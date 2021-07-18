class Item:
    """
      Super class to abstract itens
    """

    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __str__(self):
        return self.name

    def olhar(self):
      print(self.message)