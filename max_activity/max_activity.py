# arr.sort(key = lambda abc : abc[0])
# print(arr)

def FindMaxActivity(arr):
    selected_act = []
    arr_len = len(arr)
    arr.sort(key = lambda i : i[1])

    ix = 0
    selected_act.append(arr[0])

    for i in range(1,arr_len):
        if arr[i][0] >= arr[ix][1]:
            selected_act.append(arr[i])
            ix = i

    return selected_act


activities = [[0,6],[0,2],[3,4],[4,5],[5,6],[5,9],[6,10],[8,9]]
ok = FindMaxActivity(activities)
print(ok)
