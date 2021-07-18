class Personagem:
    def __init__(self, nome, inventario, mapa, posicao_inicial):
        self.nome = nome
        self.inventario = inventario
        self.mapa = mapa
        self.position = posicao_inicial

    def exitroom(self, id_sala):
        print("Salas que você pode ir: ")
        self.mapa.printa_vizinhos(self.position)

    def goto(self, id_sala):
        self.position = self.mapa.vizinhos[id_sala]

    def lookatroom(self):
        self.mapa.salas[self.position].lookat()

    def searchitems(self):
        self.mapa.salas[self.position].procura()

    def getitem(self, id):
        i = self.mapa.salas[self.position].itens[id] 
        if i.pegavel:
            self.inventario.insert(i)
        else:
            print(f"Não foi possível pegar {i.name}!")

    def getall(self, ids):
        for i in ids:
            self.getitem(i)

    def lookatitem(self, id):
        self.mapa.salas[self.position].itens[id].lookat()

    def listbackpack(self):
        self.inventario.list()

    def use(self, id):
        self.win = self.inventario.items[id].use()
