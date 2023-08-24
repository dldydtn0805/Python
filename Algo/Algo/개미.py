import sys
sys.stdin = open('input.txt')

def bfs(i):
    queue = []
    queue.append(i)
    # i번째 개미가 굴을 이동할때 각 방에 도착할때 가질수있는 최대 에너지
    visited = [-1e9]*(n+1)
    visited[i] = energy[i]
    while queue:
        t = queue.pop(0)
        for now in range(0, n+1):
            # 만약 갱신할 에너지가 더 클때만 갱신해서 최대 에너지를 유지한다
            if adj[t][now] and visited[t] - adj[t][now] > 0:
                if visited[now] < visited[t] - adj[t][now]:
                    visited[now] = visited[t] - adj[t][now]
                    queue.append(now)
    # print(visited)
    for i in range (len(visited)):
        if visited[i] >= 0:
            return i+1

n = int(input())
energy = []
for i in range(n):
    e = int(input())
    energy.append(e)

adj = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int,input().split())
    adj[a-1][b-1] = c
    adj[b-1][a-1] = c
for i in range(n):
    print(bfs(i))

