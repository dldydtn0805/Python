import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    i, w = map(int, input().split())

for i in range(n):
    if arr[i] != -1:
        graph[arr[i]-1].append(i)