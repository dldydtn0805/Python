import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    if medicine[0] == routine[0]:
        queue.append([1, len(medicine)-1, 1])
        visited[1][len(medicine)-1] = 1
    if medicine[len(medicine)-1] == routine[0]:
        queue.append([0, len(medicine)-2, 1])
        visited[0][len(medicine)-2] = 1
    while queue:
        front, back, next = queue.popleft()
        if front <= back:
            if medicine[front] == routine[next]:
                if front+1 < len(medicine):
                    if not visited[front+1][back]:
                        visited[front+1][back] = visited[front][back] + 1
                        queue.append([front+1, back, (next+1)%3])
            if medicine[back] == routine[next]:
                if 0<= back-1:
                    if not visited[front][back-1]:
                        visited[front][back-1] = visited[front][back] + 1
                        queue.append([front, back-1, (next+1)%3])


N = int(input())
routine = {0: 'B', 1: 'L', 2:'D'}
medicine = list(input().rstrip())
visited = [[0 for _ in range(len(medicine))] for _ in range(len(medicine))]
bfs()
ans = 0
for item1 in visited:
    for item2 in item1:
        ans = max(ans, item2)
print(ans)
