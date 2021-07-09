class Item:
    def __init__(self, name:str, look:str, usable = None, result=None, f_usable = None):
        """
        :param name: Nome do objeto
        :param look: Perspectiva do personagem acerca do objeto
        :param usable: id da sala que é utilizável
        :param result: (default=None) Tupla de strings para print do use(sala)
            (success, fail)
        """
        self.name = name
        if usable and result:
            self.is_usable = True 
        self.usable = usable
        self.result = result
        self.f_usable = f_usable

    def use(self, sala):
        if not self.is_usable:
            print("O item não pode ser utilizado.")
        elif sala != self.usable:
            print(self.result[1])
        else:
            self.f_usable()
            print(self.result[0])

    

    