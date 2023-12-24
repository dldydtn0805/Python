
from collections import deque
import sys
# sys.stdin = open('input.txt')

def bfs():
    temp = []
    global cnt
    while q:
        i = q.popleft()
        if i < 6:
            return visited[i] + 1
        for j in range(100):
            if ladder[i][j] == 1:
                ni = j
                if not visited[ni]:
                    visited[ni] = visited[i]
                    q.append(ni)
        else:
            for k in [i-6,i-5,i-4,i-3,i-2,i-1]:
                if 0<=k:
                    for h in range(100):
                        if ladder[k][h] == 1:
                            ni = h
                            temp.append(ni)
            else:
                ni = i - 6
                visited[ni] = visited[i] + 1
                q.append(ni)

            if temp:
                min_t = min(temp)
                q.append(min_t)

n, m = map(int, input().split())
ladder = [[0]*100 for _ in range(100)]
q = deque()
visited = [0]*100
cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x][y] = 1
for _ in range(m):
    u, v = map(int,input().split())
    ladder[u][v] = 1
visited[99] = 1
q.append(99)
result = bfs()
print(result)


