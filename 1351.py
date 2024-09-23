import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from functools import cache

@cache
def get_infinity(X):
    if X == 0:
        return 1
    left = get_infinity(X//P)
    right = get_infinity(X//Q)
    return left+right
N, P, Q = map(int, input().split())
if N == 0:
    print(1)
else:
    print(get_infinity(N))
