
# จะลดจำนวน call fucntion ให้น้อยกว่า จำนวน input
def binary_search(arr, value, first, last):
    if last >= first:
        mid = first + (last - first)
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return binary_search(arr, value, first, mid - 1)
        else:
            return binary_search(arr, value, mid + 1, last)
    else:
        return -1

num_arr = [2,5,10,15,29,50,60,70]

num_to_search = 15

print(binary_search(num_arr, num_to_search, len(num_arr) - 1, 0))
