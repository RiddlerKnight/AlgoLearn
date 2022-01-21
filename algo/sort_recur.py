
# int โดยเรียงจาก น้อยไปมาก

def index_of_min(arr, first, arr_len):
    index = first
    for i in range(first + 1, arr_len):
        if (arr[i] < arr[index]):
            index = i
    return index

def recursive_selection_sort(arr_int, first_index, arr_len):
    if(first_index < arr_len):
        index = index_of_min(arr_int, first_index, arr_len)
        arr_int[first_index], arr_int[index] = arr_int[index], arr_int[first_index]
        arr_int = recursive_selection_sort(arr_int, first_index + 1, arr_len)
    return arr_int

print(recursive_selection_sort([5,12,8,1,3,6,10], 0, 7))
print(recursive_selection_sort([12,5,9,1,3,10,6], 0, 7))