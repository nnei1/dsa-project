def insertion_sort(arr):
    for i, key in enumerate(arr):
        for j in range(i - 1, -1, -1):
            if key < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                break
    return arr
