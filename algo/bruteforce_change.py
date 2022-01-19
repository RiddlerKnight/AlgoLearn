
# def brut_force_change(money, coin_value_list, coin_typ):
#     smallestNumber = 0
#     pcoin =  [money/c for c in coin_value_list]
#     coin_n_list = []
#     for i in pcoin:
#         just_int = int(i)
#         j_list = [0]
#         for j in range(just_int):
#             j_list.append(j+1)
#         coin_n_list.append(j_list)
#     return
    
# brut_force_change(40, [25, 20, 10, 5, 1], 5)



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

print(RecursiveChange(40,[25,20,10,5,1]))


