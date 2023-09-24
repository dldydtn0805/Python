'''
공평한 선거를 하고자 함

n개의 구역으로 나누어진 백준시는 1번부터 n번까지 번호가 매겨져 있음

각 구역은 선거구중 하나에 포함되어야 한다

한 선거구에 포함된 구역은 모두 연결되어있어야함

'''
import sys
from collections import deque
sys.stdin = open('input.txt')

def backtracking(cnt):
    if cnt == edges:
        return
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            x = graph[i].pop(j)
            backtracking(cnt+1)

    pass

def bfs(start):
    visited[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for to in range(len(graph[cur])):
            next = graph[cur][to]
            if not visited[next]:
                queue.append(next)
                visited[next] = 1

n = int(input())
member = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
edges = 0
for i in range(n):
    inform = list(map(int, input().split()))
    for j in range(1, inform[0]+1):
        t = inform[j]
        if (t-1) not in graph[i]:
            graph[i].append(t-1)
            edges += 1
        if i not in graph[t-1]:
            graph[t-1].append(i)
            edges += 1
print(graph)
visited = [0]*n
print(edges)