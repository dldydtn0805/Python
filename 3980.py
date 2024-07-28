import sys
input = sys.stdin.readline
C = int(input())

def backtracking(i, cur_val):
    if i == 11:
        total[0] = max(total[0], cur_val)
        return
    for ni in range(11):
        if not visited[ni] and arr[ni][i] > 0:
                visited[ni] = 1
                backtracking(i + 1, cur_val + arr[ni][i])
                visited[ni] = 0

for _ in range(C):
    arr = [list(map(int, input().split())) for _ in range(11)]
    total = [0]
    visited = [0 for _ in range(11)]
    backtracking(0, 0)
    print(total[0])
