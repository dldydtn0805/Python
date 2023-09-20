import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(n):
    global m
    visited = [0]*1000001
    queue = deque()
    visited[n] = 0
    queue.append(n)
    while queue:
        x = queue.popleft() # 가장 먼저 넣은 현재 연산 값을 꺼내준다
        if x == m:
            print(f'#{tc}', visited[x])
        a, b, c, d = x+1, x-1, x*2, x-10
        if 0<= x<= 1000000:
            if 0<=a<=1000000 and not visited[a]:
                queue.append(a)
                visited[a] = visited[x] + 1
            if 0<=b<=1000000 and not visited[b]:
                queue.append(b)
                visited[b] = visited[x] + 1
            if 0<=c<=1000000 and not visited[c]:
                queue.append(c)
                visited[c] = visited[x] + 1
            if 0<=d<=1000000 and not visited[d]:
                queue.append(d)
                visited[d] = visited[x] + 1

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    sets = []
    bfs(n)
