import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

def bellman_ford():
    for i in range(N):
        for cur_node in range(1, N+1):
            for next_dist, next_node in graph[cur_node]:
                update_dist = distance[cur_node] + next_dist
                if update_dist < distance[next_node]:
                    distance[next_node] = update_dist
                    if i == N-1:
                        return True
    return False

T = int(input())
flag = [False]*(T)
for tc in range(T):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    # 그래프 그리기
    for _ in range(M):
        s, e, t = map(int, input().split())
        graph[s].append((t, e))
        graph[e].append((t, s))
    for _ in range(W):
        s, e, t = map(int, input().split())
        graph[s].append((-t, e))
    # 최단거리(음의 가중치가 있을때는 벨만포드 알고리즘)
    distance = [1e9] * (N+1)
    if bellman_ford():
        print('YES')
    else:
        print('NO')
