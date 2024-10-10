def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)
# countdown(8)
"""
Recursion is breaking a component down into smaller components using the same function. 
This ​function calls itself either directly or indirectly over and over until the base problem 
is identified and solved.
"""
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
print(fact(8))

