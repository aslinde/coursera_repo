my_list = [1,2,3,4]

### This is a Traditional Function
def add_to_list(item):
    return my_list.append(item)

add_to_list(0)
print(my_list)

## The fact that the Pure function has this extra 5 proves that it is a Traditional Function
def still_add_to_list(lst, item):
    lst.append(item)
    return lst
print(still_add_to_list(my_list, 5))

### This is a Pure function

def pure_add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl
print(pure_add_to_list(my_list, 5))
## But Here even though I call it again and add a 6 there is no extra 5 from the previous one
def pure_add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl
print(pure_add_to_list(my_list, 6))