arr = [90, 23, 4, 3342, 348, 1223, 5624, 32, 7, 3, 2, 2, 2, 1432, 3, 24, 646]

def insertion_sort(arr):
    n = len(arr)

    for i in range(n):
        aux = arr[i]
        j = i-1
        
        while j >= 0 and arr[j] > aux:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = aux

insertion_sort(arr)

print(arr)
