import sys
input = sys.stdin.readline
from collections import defaultdict
def dfs(depth, ci):
    global rank
    s = ci
    l = adj_list[ci][0]
    r = adj_list[ci][1]
    if l != -1:
        dfs(depth+1, l)
    width[s][0] = depth
    width[s][1] = rank
    rank += 1
    if r != -1:
        dfs(depth+1, r)

def get_root(ci):
    if parent[ci] == -1:
        root[0] = ci
        return
    else:
        get_root(parent[ci])

N = int(input())
adj_list = [[] for _ in range(10001)]
parent = [-1 for _ in range(10001)]
width = [[-1, -1] for _ in range(10001)]
rank = 1
root = [-1]
for _ in range(N):
    s, l, r = map(int, input().split())
    adj_list[s].append(l)
    adj_list[s].append(r)
    if l != -1:
        parent[l] = s
    if r != -1:
        parent[r] = s
get_root(s)
dfs(1, root[0])
depth = defaultdict(list)
for num, rank in width:
    if num != -1:
        depth[num].append(rank)
ans = -1
ans_idx = -1
for key, value in depth.items():
    cur = max(value) - min(value) + 1
    if ans < cur:
        ans = cur
        ans_idx = key
    elif ans == cur:
        ans_idx = min(key, ans_idx)
print(ans_idx, ans)

