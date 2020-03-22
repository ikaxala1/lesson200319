import time
import random

def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]//exp1) 
        count[(index)%10] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]//exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i]



# Method to do Radix Sort 
def radixSort(arr): 
  
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10



#Methods for quicksort
def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)

def quickSortHelper(arr, lo, hi):
    if hi <= lo:
        return
    j = partition(arr, lo, hi)
    quickSortHelper(arr, lo, j - 1)
    quickSortHelper(arr, j + 1, hi)

def partition(arr, lo, hi):
    j = hi + 1
    i = lo
    v = arr[lo]
    while True:
        i += 1
        while arr[i] < v:
            i += 1
            if i == hi:
                break
        j -= 1
        while arr[j] > v:
            j -= 1
            if j == lo:
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]    
    arr[lo], arr[j] = arr[j], arr[lo]
    return j

# def partition(arr,low,high): 
#     i = ( low-1 )         # index of smaller element 
#     pivot = arr[high]     # pivot 
  
#     for j in range(low , high): 
  
#         # If current element is smaller than the pivot 
#         if   arr[j] < pivot: 
          
#             # increment index of smaller element 
#             i = i+1 
#             arr[i],arr[j] = arr[j],arr[i] 
  
#     arr[i+1],arr[high] = arr[high],arr[i+1] 
#     return ( i+1 )


# Driver code to test above 
arr = 1000000 * [None]
for i in range (0, 1000000):
    arr[i] = random.randint(0, 1000000)
# print(arr)
start = time.time()
radixSort(arr) 
end = time.time()
print(end - start)

# Eliminate dependence on input.
random.shuffle(arr)

start = time.time()
quickSort(arr) 
end = time.time()
print(end - start)

# print(arr)

# for i in range(len(arr)): 
#     print(arr[i])