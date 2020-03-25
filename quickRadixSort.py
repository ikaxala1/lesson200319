import time
import random

def radixSort(a):
    BITS_PER_BYTE = 8
    BITS = 32
    R = 1 << BITS_PER_BYTE
    MASK = R - 1
    w = BITS // BITS_PER_BYTE
    n = len(a)
    aux = n * [0]
    
    for d in range(w):
        count = (R + 1) * [0]
        for i in range(n):
            c = (a[i] >> BITS_PER_BYTE*d) & MASK
            count[c + 1] += 1

        for r in range(R):
            count[r + 1] += count[r]

        if (d == w - 1):
            shift1 = count[R] - count[R//2]
            shift2 = count[R//2]
            for r in range(R//2):
                count[r] += shift1
            for r in range(R//2, R):
                count[r] -= shift2

        for i in range(n):
            c = (a[i] >> BITS_PER_BYTE*d) & MASK
            aux[count[c]] = a[i]
            count[c] += 1

        for i in range(n):
            a[i] = aux[i]


                

#Methods for quicksort
def quickSort(arr):
    random.shuffle(arr)
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

# print(arr)

# for i in range(len(arr)): 
#     print(arr[i])