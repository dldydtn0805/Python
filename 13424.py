import sys, heapq
input = sys.stdin.readline

def dijkstra(si):
    heap = []
    heapq.heappush(heap, [0, si])
    distance = [1e9 for _ in range(N)]
    distance[si] = 0
    while heap:
        cw, ci = heapq.heappop(heap)
        if cw > distance[ci]: continue
        for nw, ni in adj_list[ci]:
            next_cost = nw + distance[ci]
            if next_cost < distance[ni]:
                heapq.heappush(heap, [next_cost, ni])
                distance[ni] = next_cost
    return distance

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        adj_list[a].append([c, b])
        adj_list[b].append([c, a])
    K = int(input())
    users = list(map(int, input().split()))
    value = 1e9
    ans = -1
    for i in range(N):
        res = dijkstra(i)
        tmp = 0
        for user in users:
            tmp += res[user-1]
        if value > tmp:
            value = tmp
            ans = i
    print(ans+1)
exit()
