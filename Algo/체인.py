import sys
from collections import deque
sys.stdin = open('input.txt')
n = int(input())
chain = list(map(int, input().split()))
chain.sort(reverse=True)

rings = 0
print(chain)
cur = chain.pop()
cur_len = len(chain)
print(chain[:n-1])
while True:
    if cur <= cur_len <= cur +1:
        rings += cur
        break
    elif cur < cur_len:
        rings += cur
        chain = chain[:n-1]
        print(chain)
        cur = chain.pop()
    elif cur+1 > cur_len:

