# iteration version

arr = [90, 23, 4, 3342, 348, 1223, 5624, 32, 7, 3, 2, 2, 2, 1432, 3, 24, 646]

def selection_sort(arr):
    for i, value in enumerate(arr):
        aux = value

        for j, content in enumerate(arr[i:]):
            if value < content:
                arr[i] = arr[j]
                arr[j] = aux
