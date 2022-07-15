def heapify(arr, sz, root):
    largest = root
    left, right = 2 * root + 1, 2 * root + 2

    if left < sz and arr[root] < arr[left]:
        largest = left
    if right < sz and arr[largest] < arr[right]:
        largest = right

    if root != largest:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, sz, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
