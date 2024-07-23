import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

def get_circle(start_node, prev_node, cur_node, tmp):
    for next_node in adj_list[cur_node]:
        if prev_node != next_node:
            if next_node == start_node:
                for temp in tmp:
                    circles[temp] = 1
                return
            else:
                if not visited[next_node]:
                    visited[next_node] = 1
                    get_circle(start_node, cur_node, next_node, tmp+[next_node])

def get_distance(start_node):
    queue = deque()
    queue.append(start_node)
    visited = [0 for _ in range(N)]
    visited[start_node] = 1
    while queue:
        cur = queue.popleft()
        for next_node in adj_list[cur]:
            if circles[next_node]:
                print(visited[cur], end=' ')
                return
            else:
                if not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = visited[cur] + 1

N = int(input())
adj_list = [[] for _ in range(N)]
for _ in range(N):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    adj_list[s].append(e)
    adj_list[e].append(s)

circles = [0 for _ in range(N)]

for i in range(N):
    visited = [0 for _ in range(N)]
    get_circle(i, -1, i, [i])
    if circles[i]:
        break

for i in range(N):
    if not circles[i]:
        get_distance(i)
    else:
        print(0, end=' ')
