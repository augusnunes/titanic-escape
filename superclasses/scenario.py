class Scenario:
    """
      Abstract data structure of the game's scenario 
    """

    def __init__(self):
        self.actual = None
        self.envs = {}

    def add_environment(self, env, env_idx):
        """
            Method to add the given environment to the scenario
          Parameters:
            env (Environment): environment to add
        """
        if not self.actual:
            self.actual = env_idx
        self.envs[env_idx] = env


    def esquerda(self):
        
        # check if there is a next environment
        if self.actual == '1':
            print("Você está no primeiro ambiente")
            return

        self.actual = str(int(self.actual)-1)


    def direita(self):

        if int(self.actual) == len(self.envs):
            print("Você está no último ambiente")
            return

        self.actual = str(int(self.actual)+1)


    def get_env_by_name(self, name):
        return {furniture.name: furniture for _, furniture in self.envs[self.actual].moveis.items()}[name]


    def __str__(self):

        # read environment schema
        with open('environment.schema', 'r') as schema:
            schema_str = schema.read()

        # set environment name
        schema_str = schema_str.replace('#'*schema_str.count('#'), self.envs[self.actual].name.center(schema_str.count('#'), ' '))

        # set furniture names
        for placeholder, furniture in self.envs[self.actual].moveis.items():
            schema_str = schema_str.replace(placeholder * schema_str.count(placeholder), furniture.name.center(schema_str.count(placeholder), ' '))

        # clean unused slots
        for i in range(1, 7):
            schema_str= schema_str.replace(str(i) * schema_str.count(str(i)), ' '*schema_str.count(str(i)))

        # replace environments
        if self.actual == '1':
            previous_env = None
            next_env = str(int(self.actual)+1)

        elif self.actual == str(len(self.envs)):
            previous_env = str(int(self.actual)-1)
            next_env = None

        else:
            previous_env = str(int(self.actual)-1)
            next_env = str(int(self.actual)+1)
    
        if previous_env:
            schema_str = schema_str.replace('X'*schema_str.count('X'), self.envs[previous_env].name.center(schema_str.count('X'), ' '))
        else: 
            schema_str = schema_str.replace('X'*schema_str.count('X'), ' '*schema_str.count('X'))


        if next_env:
            schema_str = schema_str.replace('Y'*schema_str.count('Y'), self.envs[next_env].name.center(schema_str.count('Y'), ' '))
        else: 
            schema_str = schema_str.replace('Y'*schema_str.count('Y'), ' '*schema_str.count('Y'))

        return schema_str