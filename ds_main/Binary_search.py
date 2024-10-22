"""
Binary search is an efficient algorithm for finding an item in a sorted array (or list).
It works by repeatedly dividing the search interval in half, eliminating half of the remaining items at each step,
until the target value is found or the search interval is empty.
"""

#------------------------------------------------------------------------------------------------------#
#-----------------------------------------------code---------------------------------------------------#
#------------------------------------------------------------------------------------------------------#

# first way : Recursive Binary Search
def RecursiveBinarySearch(arr , low , high , key):
    if low > high : return -1 

    mid = (low + high) // 2  

    if arr[mid] == key : return mid

    elif arr[mid] > key :
        return RecursiveBinarySearch(arr , low , mid -1 , key)
    else :
        return RecursiveBinarySearch(arr , mid + 1 , high , key)


if __name__ == "__main__" :
    a = [2,3,10,12,15,20,24,44,63,78,86,94]
    k = 86
    res = RecursiveBinarySearch(a , 0 , len(a) - 1 , k )
    print(res)   

# Worst case : O(logn) / Best case : O(1)


