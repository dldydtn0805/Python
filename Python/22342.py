import sys
input = sys.stdin.readline
from copy import deepcopy

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
origin = deepcopy(arr)
max_v = 0
for j in range(len(arr[0])):
    for i in range(len(arr)):
        if 0 <= i-1 < len(arr) and 0 <= j-1 < len(arr[0]) and 0 <= i+1 < len(arr):
            arr[i][j] = max(arr[i-1][j-1], arr[i+1][j-1], arr[i][j-1]) + arr[i][j]
        elif 0 <= i-1 < len(arr) and 0 <= j-1 < len(arr[0]):
            arr[i][j] = max(arr[i-1][j-1], arr[i][j-1]) + arr[i][j]
        elif 0 <= j-1 < len(arr[0]) and 0 <= i+1 < len(arr):
            arr[i][j] = max(arr[i+1][j-1], arr[i][j-1]) + arr[i][j]
        elif 0 <= j-1 < len(arr[0]):
            arr[i][j] = arr[i][j-1] + arr[i][j]
        max_v = max(max_v, arr[i][j]-origin[i][j])
print(max_v)

