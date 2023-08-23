import sys
sys.stdin = open('input.txt')

def bfs(n):
    temp = energy[:]
    queue = []
    queue.append(n)
    while queue:
        t = queue.pop(0)
        for now in range(n):
            if temp[now] - adj[t][now]:
                temp[now] = temp[now] - adj[t][now]
                queue.append(now)
        if t == 1:
            return temp


n = int(input())
energy = []
for i in range(n):
    e = int(input())
    energy.append(e)

adj = [[0]*(n) for _ in range(n)]
way = [0]
for _ in range(n-1):
    a, b, c = map(int,input().split())
    adj[a-1][b-1] = c
    adj[b-1][a-1] = c
for i in range(n):
    print(bfs(i))