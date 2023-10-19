import sys
# sys.stdin = open('input.txt')

t = int(input())

for tc in range(t):
    K = int(input())
    N = int(input())
    arr = [[0] * (N+1) for _ in range(K+1)]
    for k in range(K+1):
        for n in range(N+1):
            if k == 0:
                arr[k][n] = n+1
            else:
                arr[k][n] = sum(arr[k-1][:n+1])
    print(arr[K][N-1])
