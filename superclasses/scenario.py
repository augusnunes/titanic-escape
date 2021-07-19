class Node:
    ''' Classe abstrata que contém uma lista duplamente encadeada, que é
    responsável pela movimentação do jogador, além da função que faz a animação 
    dos ambientes
    '''
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
    
        # Lê o arquivo do cenário
        with open('environment.schema', 'r') as schema:
            schema_str = schema.read()

        # insere o nome dos ambientes
        schema_str = schema_str.replace('#'*schema_str.count('#'), 
        self.data.name.center(schema_str.count('#'), ' '))

        # insere os nomes dos móveis em cada ambiente
        for i in range(6):
            if self.data.nomes_moveis[i]: # se não tiver um None ele faz o replace na string do ambiente
                placeholder = f'{i+1}'
                schema_str = schema_str.replace(placeholder * schema_str.count(placeholder), self.data.nomes_moveis[i].center(schema_str.count(placeholder), ' '))

        # limpa espaços inutilizáveis
        for i in range(6):
            schema_str= schema_str.replace(str(i+1) * schema_str.count(str(i+1)), ' '*schema_str.count(str(i+1)))

        # movimentação
        previous_env = self.prev 
        next_env = self.next 
    
        if previous_env:
            schema_str = schema_str.replace('X'*schema_str.count('X'), previous_env.data.name.center(schema_str.count('X'), ' '))
        else: 
            schema_str = schema_str.replace('X'*schema_str.count('X'), ' '*schema_str.count('X'))

        if next_env:
            schema_str = schema_str.replace('Y'*schema_str.count('Y'), next_env.data.name.center(schema_str.count('Y'), ' '))
        else: 
            schema_str = schema_str.replace('Y'*schema_str.count('Y'), ' '*schema_str.count('Y'))

        return schema_str
    
    def gonext(self):
        if self.next == None:
            print(self)
            print("Você está no último ambiente")
            return self
        else:
            print(self.next)
            return self.next 

    def goprev(self):
        if self.prev == None:
            print(self)
            print("Você está no primeiro ambiente")
            return self 
        else:
            print(self.prev)
            return self.prev


class Scenario:
    """
      Abstract data structure of the game's scenario 
    """

    def __init__(self):
        self.head = None

    def add_environment(self, data):
        """
            Method to add the given environment to the scenario
          Parameters:
            env (Environment): environment to add
        """
        new = Node(data)
        new.next = self.head 
        if self.head != None:
            self.head.prev = new 
        self.head = new
    

