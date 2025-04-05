## Method 1 by Slices
str = "banana"
print(str[::-1])

## Method 2 by iteration apparently not great
lst = []
for index in range(1,len(str)+1):   
    lst.append(str[-index])
print(''.join(lst))

## Method 3 Recursion
def recursive_reversal(str):
    if len(str) == 0:
        return str
    else:
        return recursive_reversal(str[1:]) + str[0]
print(recursive_reversal('potato'))

    