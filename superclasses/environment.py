
class Environment:
  """
  ADS of the a environment, an area that the player can interagir with
  """

  def __init__(self, name, descricao):
    self.name = name
    self.descricao = descricao
    self.moveis = [None, None, None, None, None, None]
    self.nomes_moveis = [None, None, None, None, None, None]

  def add_furniture(self, furniture, place):
    """
        Method to add the given furniture to the environment
        Parameters:
        furniture (Object(Movel)): furniture to add
    """
    self.moveis[place] = furniture
    self.nomes_moveis[place] = furniture.name
  
  def olhar(self):
    print(self.descricao)

  def get_furniture(self, nome):
    for i in range(len(self.nomes_moveis)):
      if self.nomes_moveis[i] == nome:
        return self.moveis[i]