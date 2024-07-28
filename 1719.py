import sys
input = sys.stdin.readline
import heapq

def dikstra(si):
    heap = []
    heapq.heappush(heap, (0, si, ''))
    distance = [1e9 for _ in range(N)]
    distance[si] = 0
    ans = ['' for _ in range(N)]
    while heap:
        cw, ci, c_way = heapq.heappop(heap)
        if cw > distance[ci]:
            continue
        for nw, ni in adjacent_list[ci]:
            nd = nw + distance[ci]
            n_way = c_way + str(ni) + '/'
            if distance[ni] > nd:
                distance[ni] = nd
                ans[ni] = n_way
                heapq.heappush(heap, (nd, ni, n_way))

    return ans

N, M = map(int, input().split())
adjacent_list = [[] for _ in range(N)]
for _ in range(M):
    s, e, d = map(int, input().split())
    s -= 1
    e -= 1
    adjacent_list[s].append((d, e))
    adjacent_list[e].append((d, s))

for i in range(N):
    res = (dikstra(i))
    for j in range(len(res)):
        if res[j] == '':
            print('-', end=' ')
        else:
            tmp = ''
            for k in range(len(res[j])):
                if res[j][k] == '/':
                    break
                tmp += res[j][k]
            print(int(tmp)+1, end=' ')
    print()
