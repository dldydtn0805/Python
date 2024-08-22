import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        cur_idx, cur_value, cur_needs, needs_max = queue.popleft()
        if cur_needs[0] == -1:
            res[cur_idx] = cur_value + needs_max
        else:
            next_needs = []
            for need in cur_needs:
                if need != -1 and res[need-1] != -1:
                    needs_max = max(res[need-1], needs_max)
                else:
                    next_needs.append(need)

            queue.append([cur_idx, cur_value, next_needs, needs_max])

N = int(input())
res = [-1 for _ in range(N)]
queue = deque()
for i in range(N):
    arr = list(map(int, input().split()))
    queue.append([i,arr[0], arr[1:], 0])
bfs()
for ans in res:
    print(ans)
