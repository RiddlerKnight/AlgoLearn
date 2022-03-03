
def init_matx(row, col, init_num):
    arr = []
    if init_num == 0:
        arr = [[0] * (len(col)+1) for i in range(len(row)+1)]
    else:
        arr.append(range(0, (len(col) + 1) * init_num, init_num))
    for i in range(1, len(row) + 1):
        arr.append([i * init_num] + [0] * len(col))
    return arr
