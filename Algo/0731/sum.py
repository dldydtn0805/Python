T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v = 1*M
    min_v = 10000*M
    for j in range(N-M+1):
        sum_v = 0
        for l in range(j, j+M):
            sum_v += arr[l]
        if max_v < sum_v:
            max_v = sum_v
        if min_v > sum_v:
            min_v = sum_v
    result = max_v-min_v
    print(f'#{i+1}', result)
