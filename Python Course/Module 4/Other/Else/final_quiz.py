'''
str = 'Pomodoro'
for l in str:
    if l == 'o':
        str = str.split()
        print(str, end=", ")
'''

sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict: ### Returns keys, even though we have seperate method .keys() that does the same why?
    print(x)          ### .items() to get key:value pairs
print(sample_dict.get(1)) 
names = ["Anna", "Natasha", "Mike"]
names.insert(2, "Xi")
print(names) ## Isn't replace but insert value at that specified index moving othhers