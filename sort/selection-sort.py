# iteration version

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [90, 23, 4, 3342, 348, 1223, 5624, 32, 7, 3, 2, 2, 2, 1432, 3, 24, 646]

selection_sort(arr)

print(arr)
