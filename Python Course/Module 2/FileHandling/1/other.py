line =[1,2,3,4]
## it's a method with no return though it applies to the original list; therfore,
## You print the original list not the method applied to the list itself
line.reverse()
print("None,",line.reverse())
print("Actual Return,",line)

line[5] = 2
print(line)
line.extend(line)
print(line)