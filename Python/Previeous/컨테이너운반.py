import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    result = []
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    s = 0
    while trucks and containers:
        if trucks[0] >= containers[0]:
            s += containers.pop(0)
            trucks.pop(0)
        else:
            containers.pop(0)
    print(f'#{tc}', s)