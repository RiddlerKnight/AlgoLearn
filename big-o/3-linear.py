
def binary_search(arr, value):
    keep = []
    loop_count = 0
    for i in range(len(arr)):
        loop_count += 1
        if arr[i] == value:
            keep.append(i)
    return keep


num_arr = [2,5,10,15,29,50,60,70]

num_to_search = 29

print(binary_search(num_arr, num_to_search))
