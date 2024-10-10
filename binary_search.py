def binary_search(lst, item):
    """
    It is Binary Search Algorithm
    The time complexity is O(log n)
    Binary search is an efficient algorithm for finding an item from a sorted list of items
    """
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high)//2
        guess = lst[mid]
        if guess == item:
            return f'index of {item} is {mid}'
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

mylist=[1,3,5,7,9]

print(binary_search(mylist,3))

    