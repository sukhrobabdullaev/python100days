class Recipe():
    def __init__(self,dish, items, time) -> None:
        self.dish=dish
        self.items=items
        self.time=time
    def contents(self):
        print('The'+self.dish+' has'+str(self.items)+\
              " and takes "+str(self.time)+"min to prepare")
        
pizza=Recipe("Pizza",["cheese","bread",'tomato'],45)
pasta=Recipe("Pasta",["penne",'sauce'],55)

print(pizza.items)
print(pasta.items)



# Inheritance
class Employees:
    def __init__(self,name,last) -> None:
        self.name=name
        self.last=last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password=password
class Chefs(Employees):
    def leave_request(self,days):
        return "May I take a leave for "+str(days)+"days"
    
