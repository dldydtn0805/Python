import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])
arr.sort(key = lambda x : (x[1], x[0]))
cnt = 1
started, ended = arr[0][0], arr[0][1]
for i in range(1, n):
    if ended <= arr[i][0]:
        started, ended = arr[i][0], arr[i][1]
        cnt += 1
print(cnt)