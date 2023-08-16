import sys
sys.stdin = open('input.txt')
def min_sunyeol(i, N, arr):
    # 최소 합
    global min_s
    # 순열 응용
    if i == N:
        i = 0
        s = 0
        while i < n:
            for j in A:
                s += arr[i][j]
                i+= 1
        min_s = min(s, min_s)
    # 순열 구하기
    else:
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            min_sunyeol(i+1, N, arr)
            A[j], A[i] = A[i], A[j]
    return min_s

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_s = 10 * n
    # 순열 만들기
    A = [i for i in range(n)]
    print(f'#{tc}', min_sunyeol(0, n, arr))
