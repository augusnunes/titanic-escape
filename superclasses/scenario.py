class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
    
        # read environment schema
        with open('environment.schema', 'r') as schema:
            schema_str = schema.read()

        # set environment name
        schema_str = schema_str.replace('#'*schema_str.count('#'), 
        self.data.name.center(schema_str.count('#'), ' '))

        # set furniture names
        for placeholder, furniture in self.data.moveis.items():
            schema_str = schema_str.replace(placeholder * schema_str.count(placeholder), furniture.name.center(schema_str.count(placeholder), ' '))

        # clean unused slots
        for i in range(1, 7):
            schema_str= schema_str.replace(str(i) * schema_str.count(str(i)), ' '*schema_str.count(str(i)))

        # replace environments
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

    def get_env_by_name(self, name): # reimplementar
        return {furniture.name: furniture for _, furniture in self.data.moveis.items()}[name]

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
        if self.head is not None:
            self.head.prev = new 
        self.head = new
    

    def get_env_by_name(self, name): # reimplementar
        return {furniture.name: furniture for _, furniture in self.envs[self.actual].moveis.items()}[name]

