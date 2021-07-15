from ambiente import Ambiente

class Mapa:
    def __init__(self, salas, edges):
        """
        :param edges: lista de listas contendo as conexões das salas
        """
        self.salas = salas
        self.vizinhos = edges

    def ilumine(self):
        for i in self.salas:
            i.is_iluminated = True
    
    def printa_vizinhos(self, id_sala):
        for i in range(len(self.vizinhos[id_sala])):
            print(f"{i} - {self.vizinhos[id_sala][i]}")
            