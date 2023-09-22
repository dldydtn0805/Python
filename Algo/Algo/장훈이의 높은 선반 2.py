from itertools import combinations
T = int(input())

for tc in range(1,T+1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    min_v = 1e9
    for i in range(n):
        set = list(combinations(arr, i+1))
        for i in set:
            if sum(i) >= b:
                x = sum(i)-b
                if min_v > x:
                    min_v = x
    print(f'#{tc}', min_v)