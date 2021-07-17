
# import required libraries
import time
from pprint import pprint
from copy import deepcopy


# Superclasses
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


    def goto_previous(self):
        
        # check if there is a next environment
        if self.actual == '1':
            print("Você está no primeiro ambiente")
            return

        self.actual = str(int(self.actual)-1)


    def goto_next(self):

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

  
    
class Environment:
    """
      ADS of the a environment, an area that the player can interact with
    """

    def __init__(self, name, moveis):
        self.name = name
        self.moveis = moveis

    def add_furniture(self, furniture, place):
        """
            Method to add the given furniture to the environment
          Parameters:
            furniture (Object(Movel)): furniture to add
        """
        self.moveis[place] = furniture



class Móvel:
    """
      Super class to abstract furnitures
    """

    def __init__(self, name, message, itens):
        self.name = name
        self.message = message
        self.itens = itens

    def look(self):
        """
            Method that display the description of the furniture
        """
        print(self.message)

    def take_all(self):
        """
            Method to that returns to the player all the itens in the furniture \
          and clear the itens list
        """
        if len(self.itens):
            all_itens = list(self.itens.values())
            all_itens = deepcopy(all_itens)
            self.itens = {}

            return list(all_itens)

        else:
            return []  

    def take_one(self):
        """
            Method that returns to the player the item requested
        """
        try:

            print("Selecione um item:")
            for i in self.itens:
              print(i)

            item = input("Qual item você deseja pegar? ")
            item = deepcopy(self.itens[item])
            self.itens = {k:v for k,v in self.itens.items()}

            return [item]

        except Exception as e:
            ## In case the player inputs nonsense
            print("%s é um item inválido" % item)
            return None

    def store_item(self, item):
        self.itens[item.name] = item

    
    
class Item:
    """
      Super class to abstract itens
    """

    def __init__(self,name, message):
        self.name = name
        self.message = message

    def look(self):
        """
          Returns a desciption of the item
        """
        print(self.message)

    def __str__(self):
        return self.name
  


# Define all furniture subclasses
class Caldeira(Móvel):

    def __init__(self, name, message, itens):
        super().__init__(name, message, itens)
        self.actions = {'stop': 'Parar de interagir com %s: ' % self.name}

    def play(self, inventory):
        # display message
        self.look()


          
class Armario(Móvel):
  
    def __init__(self, name, message, itens):
        super().__init__(name, message, itens)
        self.actions = {
            'list': 'Listar todos os objetos no %s' % self.name,
            'stop': 'Parar de interagir com %s: ' % self.name,
            'take_one': 'Pegar um item específico',
            'take_all': 'Pegar todos os itens',
        }

    def list(self):
        print("\nItens no %s" % self.name)
        for k, _ in self.itens.items():
            print(k)

    def play(self, inventory):

        # display message
        self.look()

        # Entra em um novo loop para interação com aquele móvel
        while 1:

            try:

                action = input("\nInsira um comando para interagir com %s: " % self.name)

                if action == 'help':
                    for key, value in self.actions.items():
                        print("%s: %s" % (key, value))

                if action == 'take_all':
                    return self.take_all()

                if action == 'take_one':
                    return self.take_one()

                if action == 'list':
                    self.list()

                if action == 'stop':
                    break

            except Exception as exception:
                print('Interação inválida')
                continue

      
class Motor(Móvel):

    def __init__(self, name, message, itens):
        super().__init__(name, message, itens)
        self.actions = {
            'stop': 'Parar de interagir com %s' % self.name,
            'fix': 'Tentar consertar o motor do navio'
        }

    def play(self, inventory):

        # display message
        self.look()

        # Entra em um novo loop para interação com aquele móvel
        while 1:

            try:

                action = input("\nInsira um comando para interagir com %s: " % self.name)

                if action == 'help':
                    for key, value in self.actions.items():
                        print("%s: %s" % (key, value))

                if action == 'fix':
                    return self.fix(inventory)


                if action == 'stop':
                    break

            except Exception:
                print('Interação inválida')
                continue

    def fix(self, inventory):

        if not inventory.itens:
            print("\nEu preciso de algo para consertar esse puta motor...")
            return False

        if 'Toolbox' not in [i.name for i in inventory.itens]:
            print("\nNão tenho uma caixa de ferramentas no meu inventário...")
            return False

        print("Consertando o motor fudido...")
        animation = "|/-\\"
        idx = 0
        while 1:
            if idx == 30:
                break
            print(animation[idx % len(animation)], end="\r")
            idx += 1
            time.sleep(0.1)

        return True



# player inventory
class Inventory:

    def __init__(self):
        self.itens = []

    def add(self, item):
        self.itens += item

    def remove(self, name):
        self.itens = [i for i in self.itens if i.name != name]

    def __str__(self):
        title = "\nSeu inventário contém os seguintes itens:\n"
        return title + "\n".join([i.name for i in self.itens])



# initialize scenario object
scenario = Scenario()

# create all environments
maquinario = Environment('Maquinário', {})
armazem = Environment('Armazém', {})


# create all furnitures
armario = Armario('Armário', 'Armário antigo, pode haver algo nele...', {})
caldeira = Caldeira('Caldeira', 'Caldeira velha, não posso fazer nada com ela', {})
motor = Motor('Motor', 'Que motor fudido', {})
            
# create all items
toolbox = Item('Toolbox','Uma caixa simples com ferramentas')

# store all items inside furnitures
armario.store_item(toolbox)
            
# add environments to the scenario
scenario.add_environment(maquinario, '1')
scenario.add_environment(armazem, '2')


# add furnitures to environment
maquinario.add_furniture(caldeira, '4')
maquinario.add_furniture(motor, '6')
armazem.add_furniture(armario, '1')

# create player inventory
inventory = Inventory()

# list all available actions
available_actions = {
  'goto_next': 'Vai para a sala da direita',
  'goto_previous': 'Vai para a sala da esquerda',
  'interact': 'Interage com objetos da sala',
  'look': 'Dá descrição de itens e móveis'
}

        
# main
print(scenario)
while 1:
      
    try:

        # display player inventory
        # print(inventory)

        # ask the player for a action 
        action = input("\nInsira uma ação: ")

        # display help if required
        if action == 'help':
            for key, value in available_actions.items():
                print("%s: %s" % (key, value))

        # check if the action is valid
        if action.split()[0] not in available_actions:
            continue

        ## identify and perform the required action:
        if action == 'goto_next':

            # faz o que precisa
            scenario.goto_next()
            print(scenario)
            
        elif action == 'goto_previous':

            # faz o que precisa
            scenario.goto_previous()
            print(scenario)

        elif 'interact' in action:

            # get the desired furniture
            movel = action.split()[1]
            resp = scenario.get_env_by_name(movel).play(inventory)

            if movel == 'Motor' and resp:
                print("Você conseguiu salvar o navio!!")
                break

            if resp:

                # add item to the player inventory
                inventory.add(resp)

            print(scenario)

        elif action == 'look':

            # get the desired furniture
            movel = action.split()[1]
            scenario.envs[movel].look()

    except Exception as exception:
        print(exception)
