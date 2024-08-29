import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(si):
    tmp = arr[si]
    for ni in graph[si]:
        prev = dfs(ni)
        tmp += prev
    return tmp if tmp > 0 else 0
N = int(input())
graph = [[] for _ in range(N)]
arr = [0 for _ in range(N)]
for i in range(1, N):
    t, a, p = input().rstrip().split()
    p = int(p) - 1
    a = int(a)
    if t == 'W': # 늑대
        graph[p].append(i)
        arr[i] = -a
    elif t == 'S': # 양
        graph[p].append(i)
        arr[i] = a

visited = [0 for _ in range(N)]
print(dfs(0))
