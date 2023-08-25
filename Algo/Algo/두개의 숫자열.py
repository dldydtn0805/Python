import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_v = 0
    # A의 길이가 더 길때
    if n>m:
        i = 0
        while i<n-m+1:
            sum_v = 0
            for j in range(m):
                # A와 B를 B길이만큼 완전 탐색해서
                sum_v += a[j+i]*b[j]
            max_v = max(max_v, sum_v)
            i+=1

    # B의 길이가 더 길때
    if n<m:
        i = 0
        while i<m-n+1:
            sum_v = 0
            for j in range(n):
                # A와 B를 A길이만큼 완전 탐색해서
                sum_v += a[j]*b[j+i]
            max_v = max(max_v, sum_v)
            i+=1

    print(f'#{tc}', max_v)
