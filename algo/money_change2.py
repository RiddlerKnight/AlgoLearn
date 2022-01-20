
# Term 
# The denominations are represented by an array c = (c1, . . . , cd).
# United States Change problem,c = (25, 10, 5, 1), 
# whereas in the European Union Change problem, c = (20, 10, 5, 2, 1).

# Convert some amount of money M into given denominations, using the
# smallest possible number of coins.
# Input: An amount of money M, and an array of d denominations
# c = (c1, c2, . . . , cd), in decreasing order of value (c1 > c2 > · · · > cd).
# Output: Alist of d integers i1, i2, . . . , id such that c1i1+c2i2+ · · · + cdid = M, and i1 + i2 + · · · +id is as small as possible.

def money_change2(money :int, denom :list[int]):
    n_denom = [0] * len(denom)
    m_decrease = 0
    for i in range(len(denom)):
        while((money - m_decrease) >= denom[i]):
            # if n_denom[i] is None: n_denom[i] = 0
            n_denom[i] += 1
            m_decrease += denom[i]
    return n_denom

print(money_change2(77, [25,10,5,1]))
print(money_change2(100, [25,10,5,1]))
print(money_change2(40, [25,10,5,1]))
print(money_change2(47, [25,10,5,1]))
print(money_change2(1000, [25,10,5,1]))
print(money_change2(1713, [20, 10, 5, 2, 1]))
print(money_change2(1713, [ 5, 2, 1]))