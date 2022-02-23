from numpy import *
# right = 0
# down = 1
# cross = 2


def lcs(row: str, col: str):
    score = zeros((len(row)+1, len(col)+1), dtype="int32")
    direct = zeros((len(row)+1, len(col)+1), dtype="int32")
    for i in range(1, len(row)+1):
        for j in range(1, len(col)+1):

            if (row[i-1] == col[j-1]):
                score[i, j] = max(
                    score[i-1, j], score[i, j-1], score[i-1, j-1] + 1)
            else:
                score[i, j] = max(score[i-1, j], score[i, j-1])

            if (score[i, j] == score[i, j-1]):
                direct[i, j] = 1
            elif (score[i, j] == score[i-1, j]):
                direct[i, j] = 2
            else:
                direct[i, j] = 3
    return (score[i, j], direct)


def print_lcs(direct, row, col, i, j, result=[]):
    if ((i == 0) or (j == 0)):
        print
        st = [a[2] if len(a) >= 3 else "_" for a in result]
        print("w =", " ".join(st))
        st = [b[1] if len(b) >= 2 else " " for b in result]
        print("   ", " ".join(st))
        st = [c[0] if len(c) >= 1 else "_" for c in result]
        print("v =", " ".join(st))
        print
        print("LCS =",)
        return

    if (direct[i, j] == 3):
        result = [(row[i-1], "|", col[j-1])] + result
        print_lcs(direct, row, col, i - 1, j - 1, result)
        print(row[i-1])
    else:
        if (direct[i, j] == 2):
            result = [(row[i-1]), " ", "_"] + result
            print_lcs(direct, row, col, i-1, j, result)
        else:
            result = [("_", " ", col[j-1])] + result
            print_lcs(direct, row, col, i, j - 1, result)


row = "ATGTTAT"
col = "ATCGTAC"

score, direct = lcs(row, col)

print_lcs(direct, row, col, len(row), len(col))
