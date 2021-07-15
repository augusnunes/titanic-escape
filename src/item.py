class Item:
    def __init__(self, name:str, look:str, sala = None, result=None, f_usable = None):
        """
        :param name: Nome do objeto
        :param look: Perspectiva do personagem acerca do objeto
        :param usable: id da sala que é utilizável
        :param result: (default=None) Tupla de strings para print do use(sala)
            (success, fail)
        """
        self.name = name
        if sala and result:
            self.is_usable = True 
        self.sala = sala
        self.result = result
        self.f_usable = f_usable
        self.look = look

    def use(self, sala):
        if not self.is_usable:
            print("O item não pode ser utilizado.")
        elif sala != self.sala:
            print(self.result[1])
        else:
            self.f_usable()
            print(self.result[0])

    def look(self):
        print(self.look)
    
    def printa(self):
        print("- ",self.name)
        
    