def quick_sort(arr, beg=0, end=None):
    if end is None:
        end = len(arr) - 1
    p_beg, p_end = beg, end
    if p_beg < p_end:
        pivot = arr[p_beg]
        pivot_idx = p_beg

        while p_beg < p_end:
            while p_beg <= end and arr[p_beg] <= pivot:
                p_beg += 1
            while pivot < arr[p_end]:
                p_end -= 1

            if p_beg < p_end:
                arr[p_beg], arr[p_end] = arr[p_end], arr[p_beg]

        arr[p_end], arr[pivot_idx] = arr[pivot_idx], arr[p_end]

        quick_sort(arr, beg, p_end - 1)
        quick_sort(arr, p_end + 1, end)

    return arr
