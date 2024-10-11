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
# print(fact(8))

def sumList(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sumList(lst[1:])

lst1 = [4,5,6,12,6,21,12,121,4,1,2,3]
# print(sumList(lst1))

def int_to_str(n, base):
    conver_tString = "0123456789ABCDEF"
    if n < base:
        return conver_tString[n]
    else:
        return int_to_str(n//base, base) + conver_tString[n % base]
    
# print(int_to_str(2835,16))

def countArr(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + countArr(arr[1:])
    
print(f'first{len(lst1)}')
print(countArr(lst1))

def findLargest(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        largest = findLargest(arr[1:])
        return arr[0] if arr[0] > largest else largest
    
print(findLargest(lst1)) 
        

