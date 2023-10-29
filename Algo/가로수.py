import sys
# sys.stdin = open('input.txt')
import math
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    if not arr:
        temp = int(input())
        arr.append(0)
    else:
        arr.append(int(input())-temp)
x = (arr[-1] // math.gcd(*arr))
print (x - n + 1)