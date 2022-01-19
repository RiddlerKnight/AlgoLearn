
# n คือจำนวน Level fibo
def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-2) + fibo(n-1)

# 1=0+1 level1
# 2=1+1 level2
# 3=1+2 level3

print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(1000))
