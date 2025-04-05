
## Recursion
def factorial(n):
    if n==0: ## It's better to have it be ==1 here, you reduce the recursion by 1 so it's more efficient
        return 1
    else:
        return n*factorial(n-1)
print(factorial(6))
## Loop
def loop_factorial(n):
    if n<=0:
        return 1
    else:
        sum_n = 1  
        for i in range(1,n+1): ## That's righttt... you could specify where the range starts and ends, anyways it was correct
            sum_n *= i
        return sum_n
#for i in range(5): print(i)
print(loop_factorial(6))
            