from functools import lru_cache
import sys
input = sys.stdin.readline

DIV = 1000000007
@lru_cache(maxsize=None)
def fibo(n):
    if n == 0 :
        return 0
    if n == 1 or n == 2:
        return 1
    if n % 2 == 0:
        m = n // 2
        temp1 = fibo(m-1)
        temp2 = fibo(m)
        return ((2 * temp1 + temp2) * temp2) % DIV
    else:
        m = (n+1) // 2
        temp1 = fibo(m)
        temp2 = fibo(m -1 )
        return (temp1 * temp1 + temp2 * temp2) % DIV

n = int(input())
print(fibo(n))
