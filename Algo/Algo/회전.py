import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input(). split()))
    for i in range(m):
        arr.append(arr.pop(0))
    print(f'#{tc}', arr.pop(0))
