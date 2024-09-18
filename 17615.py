import sys
input = sys.stdin.readline
from collections import deque

def check_right(ball):
    copied_arr = arr[:]
    while copied_arr[-1] != ball:
        copied_arr.pop()
    cnt = len(copied_arr) - copied_arr.count(ball)
    return cnt

def check_left(ball):
    copied_arr = arr[:]
    copied_arr = deque(copied_arr)
    while copied_arr[0] != ball:
        copied_arr.popleft()
    cnt = len(copied_arr) - copied_arr.count(ball)
    return cnt


N = int(input())
arr = list(input().rstrip())
if len(set(arr)) == 1:
    print(0)
else:
    A = (check_right('R'))
    B = (check_right('B'))
    C = (check_left('R'))
    D = (check_left('B'))
    print(min(A, B, C, D))
