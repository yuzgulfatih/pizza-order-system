class Pizza : 
    def __init__(self , description , cost):
        self.description = description
        self.cost = cost

    def get_description(self) : 
        return self.description
    
    def get_cost(self) :
        return self.cost

class ClassicPizza(Pizza):
    def __init__(self ):
        super().__init__ ("Klasik Pizza" , 80)


class Margherita(Pizza) : 
    def __init__(self):
        super().__init__ ("Margarita" , 70)

class TurkPizza(Pizza) :
    def __init__(self):
        super().__init__ ("Türk Pizza" , 83)

class DominosPizza(Pizza):
   def __init__(self):
        super().__init__ ("Sade Pizza" , 74)

