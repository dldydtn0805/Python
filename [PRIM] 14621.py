import sys, heapq
input = sys.stdin.readline

def prim(start):
    mst = []
    visited = set()
    visited.add(start)
    heap = []
    for dist, end in graphs[start]:
        heapq.heappush(heap, [dist, start, end])
    while heap:
        cur_w, cur_start, cur_end = heapq.heappop(heap)
        if cur_end not in visited:
            visited.add(cur_end)
            mst.append((cur_start, cur_end, cur_w))
            for next_w, next_end in graphs[cur_end]:
                if next_end not in visited:
                    heapq.heappush(heap, [next_w, cur_end, next_end])
    return mst

N, M = map(int,input().split())
genders = list(input().rstrip().split())

graphs = [[] for _ in range(N)]
for m in range(M):
    u, v, d = map(int,input().split())
    u -= 1
    v -= 1
    if genders[u] != genders[v]:
        graphs[u].append([d, v])
        graphs[v].append([d, u])

res = prim(0)
if len(res) < N-1:
    print(-1)
else:
    ans = 0
    for r in res:
        ans += r[2]
    print(ans)
