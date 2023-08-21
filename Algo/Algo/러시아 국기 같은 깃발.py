import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    gukgi = [list(input()) for _ in range(n)]
    print(gukgi)