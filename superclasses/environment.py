
class Environment:
  """
  Classe de um ambiente cujo jogador pode interagir
  """

  def __init__(self, name, descricao):
    self.name = name
    self.descricao = descricao
    self.moveis = [None, None, None, None, None, None]
    self.nomes_moveis = [None, None, None, None, None, None]

  def add_furniture(self, furniture, place):
    """
        Método que adiciona um móvel ao dado ambiente
        furniture (Object(Movel)): móvel para add
    """
    self.moveis[place] = furniture
    self.nomes_moveis[place] = furniture.name
  
  def olhar(self):
    print(self.descricao)

  def get_furniture(self, nome):
    for i in range(len(self.nomes_moveis)):
      if self.nomes_moveis[i] == nome:
        return self.moveis[i]