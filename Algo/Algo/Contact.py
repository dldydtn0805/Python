import sys
sys.stdin = open('input.txt')

def bfs(s):
    queue = []
    visited = [0]*(101)
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        for w in range(1, 101):
            if visited[w] == 0 and adj[t][w] == 1:
                queue.append(w)
                visited[w] = visited[t] + 1
    return visited


for tc in range(1, 11):
    e, s = map(int, input().split())
    contact = list(map(int, input().split()))
    adj = [[0]*(101) for _ in range(101)]
    # 인접행렬로 접근해보자
    for i in range(0, e, 2):
        v1, v2 = contact[i], contact[i+1]
        adj[v1][v2] = 1
    result = (bfs(s))
    max_i = 0
    max_index = 0
    for i in range(101):
        if result[i] >= max_i:
            max_i = result[i]
            max_index = i
    print(f'#{tc}', max_index)