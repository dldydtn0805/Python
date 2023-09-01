import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(2**n):
        s = 0
        for j in range(n):
            if i & 2**j:
                s += (a[j])
        if s == k:
            cnt += 1
    print(f'#{tc}', cnt)