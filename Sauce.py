from Pizza import *
class Decorator:
    def __init__(self, component):
        self.component = component
        
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return Pizza.get_description(self) + ' ' + self.component.get_description()
    

class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Zeytinli"
        self.cost = 6
        
class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mantarlı"
        self.cost = 5
        
class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Keçi peynirli"
        self.cost = 7
        
class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Etli"
        self.cost = 10
        
class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Soğanlı"
        self.cost = 2
        
class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mısırlı"
        self.cost = 4
    


