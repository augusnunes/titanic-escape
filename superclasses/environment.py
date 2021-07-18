from pprint import pprint

class Environment:
  """
  ADS of the a environment, an area that the player can interagir with
  """

  def __init__(self, name, descricao, moveis):
    self.name = name
    self.descricao = descricao
    self.moveis = moveis

  def add_furniture(self, furniture, place):
    """
        Method to add the given furniture to the environment
        Parameters:
        furniture (Object(Movel)): furniture to add
    """
    self.moveis[place] = furniture
  
  def olhar(self):
    print(self.descricao)