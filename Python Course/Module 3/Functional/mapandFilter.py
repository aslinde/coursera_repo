menu = ["cappucino", "latte", "espresso"]

def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee
coffee_map = map(find_coffee, menu) 
print(coffee_map)  ## Seems like pointers like * work 
for item in coffee_map:
 #   if item != None:
        print(item)
print(list(coffee_map))

print("Works like this too", *coffee_map) ## But not here for some reason 

####### Maps and Filters
numbers = [15, 30, 47, 82, 95]
### The map function returns it as a object but the list allows it to become values as the object now points at a list of values so they can be printed?? But they're not a new list of values 
### BUT the RAW return from the function
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)

def lesser_filter(numbers):
   return numbers < 50

## Still returns as a object
small = filter(lesser, numbers)
print('Object,',small)
## Needs to iterated over
for i in small: print(i)
