import heapq
from collections import deque

s = list(input())
t = list(input())

flag = 0
while t:
    if s == t:
        flag = 1
        break
    if s != t:
        if t[-1] == 'A':
            t.pop()
        elif t[-1] == 'B':
            t.pop()
            t = list(reversed(t))

if flag:
    print(1)
else:
    print(0)