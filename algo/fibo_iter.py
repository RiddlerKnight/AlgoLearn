
def fibo(n):
    f1, f2 = 0, 1
    fn = 0
    for i in range(0, n):
        fn = f1 + f2
        f1 = f2
        f2 = fn
        #fn, f1, f2 = f1 + f2, f2, fn

    return fn
        
print(fibo(1)) # 1=0+1 level1
print(fibo(2)) # 2=1+1 level2
print(fibo(3)) # 3=1+2 level3
print(fibo(4)) # 5=2+3 level4
print(fibo(5)) # 8=3+5 level5

# print(fibo(3))

# def plus(a,b):
#     return a+b

# f1, f2 = 0, 1
# print(plus(f1,f2))
# f1, f2 = 3, 5
# print(plus(f1,f2))
# f1, f2 = 5, 8
# print(plus(f1,f2))

