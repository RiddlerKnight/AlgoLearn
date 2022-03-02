from turtle import right
from numpy import *


def lcs(row: str, col: str):
    score = zeros((len(row)+1, len(col)+1), dtype="int32")
    direct = zeros((len(row)+1, len(col)+1), dtype="int32")

    row_len = len(row)+1
    col_len = len(col)+1

    score_build = [[0] * col_len for i in range(row_len)]
    direct_build = [[0] * col_len for i in range(row_len)]

    row.insert(0, 0)
    col.insert(0, 0)

    for i in range(1, row_len):
        for j in range(1, col_len):

            up = score_build[i-1][j]  # "↑"
            left = score_build[i][j-1]  # "←"
            up_left = score_build[i-1][j-1]  # "↖"

            if (row[i] == col[j]):
                up_left = up_left + 1
            score_build[i][j] = max(up, left, up_left)

            if (score_build[i][j] == score_build[i][j-1]):
                direct_build[i][j] = "←"
            elif (score_build[i][j] == score_build[i-1][j]):
                direct_build[i][j] = "↑"
            else:
                direct_build[i][j] = "↖"
    return (score_build[i][j], direct_build)


v = ["A", "T", "G", "T", "T", "A", "T"]
w = ["A", "T", "C", "G", "T", "A", "C"]

lcs(v, w)
