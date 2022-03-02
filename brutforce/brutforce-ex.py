
from itertools import chain, product

def bruteforce(charset, repeat_n):
    arr = []
    # check = product(charset, repeat=repeat_n)
    # for i in check:
    #     print(i)
    # print("============================")
    # check = product(charset, repeat=repeat_n)
    # for i in check:
    #     print(i)
    check = product(charset, repeat=repeat_n)
    check2 = chain.from_iterable(check)
    for f in check2:
        print(f)
    return None

# def bruteforce2():


m = [25,10,5,1]
# bruteforce("abcd", 4)

rng = range(101)
bruteforce(rng, 3)