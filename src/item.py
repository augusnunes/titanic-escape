class Item:
    def __init__(self, name:str, look:str, 
    pegavel=False, sala = None, result=None, f_usable = None, win = True):
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
        self.pegavel = pegavel
        self.win = win

    def use(self, sala):
        if not self.is_usable:
            print("O item não pode ou ainda não está pronto para ser utilizado.")
        elif sala != self.sala:
            print(self.result[1])
        else:
            self.f_usable()
            print(self.result[0])
            return self.win

    def lookat(self):
        print(self.look)
    
    def printa(self):
        print("- ",self.name)

    