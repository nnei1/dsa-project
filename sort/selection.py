def selection_sort(arr):
    for i, _ in enumerate(arr):
        _min = i
        for j in range(i + 1, len(arr)):
            if arr[_min] > arr[j]:
                _min = j
        arr[i], arr[_min] = arr[_min], arr[i]

    return arr
