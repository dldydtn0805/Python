import sys
# sys.stdin = open('input.txt')

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

min_cnt = 1e9
for n in range(N-7):
    for m in range(M-7):
        cnt = 0
        case1 = 0
        case2 = 0
        for i in range(n, n+8):
            for j in range(m, m+8):
                # i열이 홀수일때, j열이 홀수일때
                if i % 2 and j % 2:
                    if arr[i][j] == 'W':
                        case1 += 1
                    else:
                        case2 += 1
                # i열이 홀수일때, j열이 짝수일때
                elif i % 2 and j % 2 == 0:
                    if arr[i][j] == 'B':
                        case1 += 1
                    else:
                        case2 += 1
                # i열이 짝수일때, j열이 홀수일때
                elif i % 2 == 0 and j % 2:
                    if arr[i][j] == 'B':
                        case1 += 1
                    else:
                        case2 += 1
                # i열이 짝수일때, j열이 짝수일때
                elif i % 2== 0 and j % 2 == 0:
                    if arr[i][j] == 'W':
                        case1 += 1
                    else:
                        case2 += 1
        min_cnt = min(case1, case2, min_cnt)
print(min_cnt)
