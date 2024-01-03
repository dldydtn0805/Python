import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())
    F = N%H
    if F == 0:
        F = H
        R = N // H
    else:
        R = N//H + 1
    if R < 10:
        print(f'{F}0{R}')
    else:
        print(f'{F}{R}')