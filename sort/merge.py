def merge_sort(arr):
    _len = len(arr)
    left = right = None
    if _len > 1:
        mid = _len // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

    i = 0
    while True:
        if left and right:
            if left[0] < right[0]:
                arr[i] = left.pop(0)
            else:
                arr[i] = right.pop(0)
        elif left:
            arr[i] = left.pop(0)
        elif right:
            arr[i] = right.pop(0)
        else:
            break
        i += 1

    return arr
