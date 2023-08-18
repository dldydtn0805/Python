import sys
sys.stdin = open('input.txt')
def bfs(s, g, e):
    queue = []
    visited = [0]*(v+1)
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        for i in injup[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    # 도착 노드에 도착할 수 있다면
    if visited[g]:
        return visited[g]-1
    # 도착 노드에 도착할 수 없다면
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    # 정점의 갯수, 간선의 갯수
    v, e = map(int, input().split())
    # 인접 리스트 설정
    injup = [[] for _ in range(v+1)]
    for _ in range(e):
        # 쌍방향으로 노드 삽입
        v1, v2 = map(int, input().split())
        injup[v1].append(v2)
        injup[v2].append(v1)
    # 시작점과 도착점
    s, g = map(int, input().split())
    result = bfs(s, g, e)
    print(f'#{tc}', result)