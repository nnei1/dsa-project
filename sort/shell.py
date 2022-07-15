def shell_sort(arr):
    gap = len(arr) // 2
    while gap:
        i = 0
        for j in range(gap, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

            k = i
            while 0 <= k - gap:
                if arr[k] < arr[k - gap]:
                    arr[k - gap], arr[k] = arr[k], arr[k - gap]
                k -= 1

            i, j = i + 1, j + 1
        gap //= 2
    return arr
