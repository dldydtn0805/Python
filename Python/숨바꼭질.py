import sys
# sys.stdin = open('input.txt')
from collections import deque

start, end = map(int, input().split())

graph = [0 for _ in range(100001)]
def bfs():
    q = deque()
    q.append(start)
    graph[start] = 1
    while q:
        cur = q.popleft()
        if cur == end:
            print(graph[cur]-1)
            exit()
        if 0<=cur+1<100001 and graph[cur+1] == 0:
            q.append(cur+1)
            graph[cur+1] = graph[cur]+1
        if 0<=cur-1<100001 and graph[cur-1] == 0:
            q.append(cur-1)
            graph[cur-1] = graph[cur]+1
        if 0<=2*cur<100001 and graph[2*cur] == 0:
            q.append(2*cur)
            graph[2*cur] = graph[cur]+1
bfs()
