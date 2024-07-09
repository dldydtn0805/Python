import sys, heapq
sys.stdin = open('input.txt')
def djk(start):
    heap = []
    # heapq.heappush(heap, (0, start))
    heap.append((0,start))
    visited[start] = 0 # 빼먹음
    while heap:
        # dist, now = heapq.heappop(heap)
        heap = sorted(heap)
        dist, now = heap.pop(0)
        if visited[now] < dist: # 빼먹음
            continue
        for next in graph[now]:
            to = next[0]
            cost = next[1]
            new_cost = dist + cost
            if new_cost >= visited[to]: #visited[to]를 visited[now]로 썼음
                continue
            visited[to] = new_cost
            # heapq.heappush(heap, (new_cost, to))
            heap.append((new_cost, to))
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    visited = [int(1e9)]*(N+1)
    djk(0)
    print(f'#{tc}', visited[len(visited)-1])


