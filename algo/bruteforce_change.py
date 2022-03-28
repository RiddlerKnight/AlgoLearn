def RecursiveChange(M, c):
    if (M == 0):
        return [0 for i in range(len(c))]
    smallestNumberOfCoins = M+1
    for i in range(len(c)):
        if (M >= c[i]):
            thisChange = RecursiveChange(M - c[i], c)
            thisChange[i] += 1
            if (sum(thisChange) < smallestNumberOfCoins):
                bestChange = thisChange
                smallestNumberOfCoins = sum(thisChange)
    return bestChange


print(RecursiveChange(40, [25, 20, 10, 5, 1]))
