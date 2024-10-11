def quick_sort(arr):
    """
    It is Quick Sort Algorithm
    The  avaerage time complexity is O(n * log n)
    The  worst time complexity is O(n**2)
    
    The Quicksort algorithm takes an array of values, 
    chooses one of the values as the 'pivot' element, 
    and moves the other values so that lower values are 
    on the left of the pivot element, and higher values are on the right of it
    
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
arr4 = [10,5,2,3]
arr5 = [10,5,2,3,31]
arr10 = [10,5,2,3,31,12,123,12345,21,1]
print(quick_sort(arr4))
print(quick_sort(arr5))
print(quick_sort(arr10))