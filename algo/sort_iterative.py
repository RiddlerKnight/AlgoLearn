def sort_from_min_to_max(arr):
    index = 0
    for i in range(index, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if(arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(sort_from_min_to_max([5,12,8,1,3,6,10]))