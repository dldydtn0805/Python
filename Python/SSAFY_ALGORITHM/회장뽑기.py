import sys
from collections import deque
# sys.stdin = open('input.txt')

'''
각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받는다

회장은 회원들 중에서 점수가 가장 작은 사람이된다

회장의 점수와, 회장이 될수있는 모든 사람을 찾는 프로그램을 작성하라


'''

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1
    while queue:
        cur = queue.popleft()
        for to in range(len(graph[cur])):
            next = graph[cur][to]
            if visited[next]:
                continue
            queue.append(next)
            visited[next] = visited[cur] + 1

n = int(input())
graph = [[] for _ in range(n)]
while True:
    f, t = map(int, input().split())
    if f == -1 and t == -1:
        break
    graph[f-1].append(t-1)
    graph[t-1].append(f-1)

min_v = 1e9
men = []
for i in range(n):
    visited = [0]*n
    bfs(i)
    if min_v > max(visited):
        min_v = max(visited)
        men = [i+1]
    elif min_v == max(visited):
        men.append(i+1)
print(min_v-1, len(men))
print(*men)
