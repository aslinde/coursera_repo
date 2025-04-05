### If you don't define a return you won't get anything back from a function
def my_fun(x,y):
    x+y
print(my_fun(2,2))

def my_fun_r(x,y):
    return x+y
print(my_fun_r(2,2))


####Both Work but the One with the Function is Much more reusable you don't have to copy paste it
bill=175
tax_rate=15
total_tax=bill*tax_rate/100
print('Total Tax is ',total_tax)

def calculate_tax(bill,tax_rate):
    return bill*tax_rate/100
print(calculate_tax(175,15))

