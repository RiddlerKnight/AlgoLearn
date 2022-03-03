
def init_matx(row, col, init_num):
    arr = []
    if init_num == 0:
        arr = [[0] * (len(col)+1) for i in range(len(row)+1)]
    else:
        arr.append(range(0, (len(col) + 1) * init_num, init_num))
        for i in range(1, len(row) + 1):
            arr.append([i * init_num] + [0] * len(col))
    return arr


def score_p(row, col, row_ix, col_ix, point):
    return point if row[row_ix] == col[col_ix] else -1 * point


def global_alignment(row, col, indent, point):
    matx = init_matx(row, col, indent)
    for r in range(1, len(row)+1):
        for c in range(1, len(col)+1):

            i_a = matx[r - 1][c] + indent
            i_b = matx[r - 1][c - 1] + score_p(row, col, r - 1, c - 1, point)
            i_c = matx[r][c - 1] + indent

            matx[r][c] = max([
                i_a,
                i_b,
                i_c
            ])
    return matx


def local_alignment(row, col, indent, point):
    matx = init_matx(row, col, indent)
    all_max = row_max = col_max = 0
    for r in range(1, len(row) + 1):
        for c in range(1, len(col) + 1):

            i_a = matx[r - 1][c] + indent
            i_b = matx[r - 1][c - 1] + score_p(row, col, r - 1, c - 1, point)
            i_c = matx[r][c - 1] + indent

            matx[r][c] = max([
                0,
                i_a,
                i_b,
                i_c
            ])

            if matx[r][c] > all_max:
                all_max = matx[r][c]
                row_max = r
                col_max = c
    return matx, row_max, col_max


v_row = ["G", "A", "C", "G", "G"]
w_col = ["T", "A", "T", "A", "C", "G", "C", "C", "A"]


check_global_align = global_alignment(v_row, w_col, -1, 1)
check_local_align = local_alignment(v_row, w_col, -1, 1)

print(check_global_align)
print(check_local_align)


range(0, 16, 2)[3]

# 0 -2 -4 -6 -8
# -2
# -4
# -6
# -8
