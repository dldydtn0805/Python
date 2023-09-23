import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    homework = list(map(int, input().split()))
    # print(homework)
    total = [i for i in range(1, n+1)]
    for i in homework:
        total.remove(i)
    print(f'#{tc}', *total)