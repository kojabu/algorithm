def  findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    """
     It is Selection Sort Algorithm
     The time complexity is O(n**2)
     The algorithm repeatedly finds the minimum element in the 
     unsorted part and swaps it with the leftmost element of the unsorted part, 
     thus expanding the sorted part by one element.
    """
    newArr = []
    for i in range(1, len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

lst = [5,3,6,2,10]
print(findSmallest(lst))
print(selectionSort(lst))