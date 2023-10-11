import sys
from itertools import combinations
# sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
X = list(combinations(arr, 3))
Y = (list(map(sum, X)))
max_v = 0
for y in Y:
    if y <= m and y > max_v:
        max_v = y
print(max_v)
