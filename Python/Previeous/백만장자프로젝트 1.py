import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = list(map(int, input().split()))
    total = 0
    #역방향
    max_v = arr[n-1]
    for i in range(n-1, -1, -1):
        if max_v < arr[i]:
            max_v = arr[i]
        if max_v > arr[i]:
            total += max_v - arr[i]
    print(f'#{tc}', total)
