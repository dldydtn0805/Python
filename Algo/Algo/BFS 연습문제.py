"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

"""

import sys
sys.stdin = open('input.txt')

def bfs(s, V):
    visited = [0] * (V+1) # visited 생성
    q = [] # queue 생성
    q.append(s) # 시작점 인큐
    visited[s] = 1 # 시작점 방문 표시
    while q: # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0) # 디큐
        print(t) # 할일
        # 인접한 정점 중 인큐되지 않은 정점이 있으면 w 인큐, 인큐되었음을 표시
        for w in adj_l[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1

V, E = map(int, input().split())
arr = list(map(int, input().split()))

#인접 리스트
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

bfs(1,7)