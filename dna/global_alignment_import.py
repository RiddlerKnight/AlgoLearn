import numpy as np


def LCS(v, w, match, mismatch, gap):
    v = '0'+v
    w = '0'+w
    n = len(v)
    m = len(w)
    s = np.zeros(shape=(n, m), dtype="int8")
    b = np.zeros(shape=(n, m), dtype="int8")
    for i in range(n):
        s[i, 0] = -i*gap
        b[i, 0] = 1
    for j in range(m):
        s[0, j] = -j*gap
        b[0, j] = 2

    for i in range(1, n, 1):
        for j in range(1, m, 1):
            vertical = s[i-1, j]-gap
            horizontal = s[i, j-1]-gap
            if(v[i] == w[j]):
                diag = s[i-1, j-1]+match
            else:
                diag = s[i-1, j-1]-mismatch
            s[i, j] = max(vertical, horizontal, diag)
            if(s[i, j] == vertical):
                b[i, j] = 1  # keep 1 for vertical
            elif(s[i, j] == horizontal):
                b[i, j] = 2  # keep 2 for horizontal
            elif(s[i, j] == diag):
                b[i, j] = 3  # keep 3 for diag

    return(s[n-1, m-1], b)


def LCS_local(v, w, match, mismatch, gap):
    v = '0'+v
    w = '0'+w
    n = len(v)
    m = len(w)
    s = np.zeros(shape=(n, m), dtype="int8")
    b = np.zeros(shape=(n, m), dtype="int8")
    for i in range(n):
        s[i, 0] = -i*gap
        b[i, 0] = 1
    for j in range(m):
        s[0, j] = -j*gap
        b[0, j] = 2

    for i in range(1, n, 1):
        for j in range(1, m, 1):
            vertical = s[i-1, j]-gap
            horizontal = s[i, j-1]-gap
            if(v[i] == w[j]):
                diag = s[i-1, j-1]+match
            else:
                diag = s[i-1, j-1]-mismatch
            s[i, j] = max(0, vertical, horizontal, diag)
            if(s[i, j] == vertical):
                b[i, j] = 1  # keep 1 for vertical
            elif(s[i, j] == horizontal):
                b[i, j] = 2  # keep 2 for horizontal
            elif(s[i, j] == diag):
                b[i, j] = 3  # keep 3 for diag

    return(s[n-1, m-1], b)


def printLCS(b, v, w, i, j):
    if(i == 0 | j == 0):
        return("", "")
    if(b[i, j] == 3):
        vout, wout = printLCS(b, v, w, i-1, j-1)
        vout = vout+v[i]
        wout = wout+w[j]
    else:
        if(b[i, j] == 1):
            vout, wout = printLCS(b, v, w, i-1, j)
            vout = vout+v[i]
            wout = wout+"-"
        else:
            vout, wout = printLCS(b, v, w, i, j-1)
            vout = vout+"-"
            wout = wout+w[j]
    return(vout, wout)


def globalAlign(v, w, match, mm, gap):
    s, b = LCS(v, w, match, mm, gap)
    v = '0'+v
    w = '0'+w
    vout, wout = printLCS(b, v, w, len(v)-1, len(w)-1)
    print(vout)
    print(wout)


def localAlign(v, w, match, mm, gap):
    s, b = LCS_local(v, w, match, mm, gap)
    v = '0'+v
    w = '0'+w
    vout, wout = printLCS(b, v, w, len(v)-1, len(w)-1)
    print(vout)
    print(wout)


def main(v, w, match, mm, gap):
    globalAlign(v, w, match, mm, gap)
    localAlign(v, w, match, mm, gap)


main("ACTACTAGATTACTTACGGATCAGGTACTTTAGAGGCTTGCAACCA",
     "TACTCACGGATGAGGTACTTTAGAGGC", 1, 1, 2)  # match = 1, mismatch = -1, gap = -2
