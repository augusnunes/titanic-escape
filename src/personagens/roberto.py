from personagem import Personagem
from ambiente import Ambiente

class Robert(Personagem):
    def __init__(self, mapa, ambiente, inventario):
        super().__init__('Robert', inventario, mapa, )
    
    def exitroom(self, id_sala):
        super().exitroom(id_sala)
    
    def goto(self, id_sala):
        super().goto(id_sala)

    def lookatroom(self):
        super().lookatroom()

    def searchitems(self):
        super().searchitems()

    def getitem(self, id):
        super().getitem(id)

    def getall(self, ids):
        super().getall(ids)

    def lookatitem(self, id):
        super().lookatitem(id)

    def listbackpack(self):
        super().listbackpack()

    def use(self, id):
        super().use(id)




# criar cada item
# criar o mapa
# criar o inventario
# 