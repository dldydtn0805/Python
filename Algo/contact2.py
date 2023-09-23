# import sys
# sys.stdin = open('input.txt')

def bfs(m):
    visited = [0]*101
    visited[m] = 1
    queue = [m]
    while queue:
        now = queue.pop(0)
        for to in range(len(graph[now])):
            next = graph[now][to]
            if visited[next]:
                continue
            visited[next] = visited[now] + 1
            queue.append(next)
    return(visited)
T = 10
for tc in range(1, T+1):
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, n, 2):
        x = arr[i]
        y = arr[i+1]
        graph[x].append(y)
    result = (bfs(m))
    max_v = 0
    max_i = 0
    for i in range(len(result)):
        if max_v <= result[i]:
            max_v = result[i]
            max_i = i
    print(f'#{tc}', max_i)