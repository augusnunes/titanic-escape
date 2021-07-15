class Personagem:
    def __init__(self, nome, inventario, mapa, posicao_inicial):
        self.nome = nome
        self.inventario = inventario
        self.mapa = mapa
        self.position = posicao_inicial

    def goto(self, id_sala):
        self.position = self.mapa.vizinhos[id_sala]

    def searchitems(self):
        self.mapa.salas[self.position].procura()

    def exitroom(self, id_sala):
        print("Salas que você pode ir: ")
        self.mapa.printa_vizinhos(self.position)

    def getitem():
        pass 

    def getall():
        pass 
    
    def lookatitem():
        pass 

    def lookatsala():
        pass 

    def listbackpack(self):
        pass 
