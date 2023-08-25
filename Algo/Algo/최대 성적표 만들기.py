import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()
    total = 0
    while k>0:
        total += score.pop()
        k -= 1
    print(f'#{tc}', total)