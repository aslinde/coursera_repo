class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + \
              " and takes " + str(self.time) + " min to prepare")
pizza = Recipe("Pizza", ["Cheese", "Bread"], 45)
pasta = Recipe("Pasta", ["Penne", "Sauce"], 45)
print(pizza.contents())
print(pasta.contents())

print(pasta.dish)
''' 

 def __new__(cls : type[Self]) -> Self:
        pass
'''