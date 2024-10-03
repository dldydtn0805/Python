import sys
input = sys.stdin.readline
from collections import deque
def plus(X):
    return X+1
def bfs(si):
    queue = deque()
    visited = [0 for _ in range(N)]
    queue.append((si, [si]))
    visited[si] = 1
    while queue:
        ci, path = queue.popleft()
        current = codes[ci]
        for ni in range(N):
            if not visited[ni]:
                next = codes[ni]
                cnt = 0
                flag = True
                for k in range(K):
                    if flag:
                        if current[k] != next[k]:
                            cnt += 1
                            if cnt == 2:
                                flag = False
                                break
                if flag:
                    visited[ni] = 1
                    next = path + [ni]
                    if ni == B:
                        return next
                    else:
                        queue.append((ni, next))


N, K = map(int, input().split())
codes = [list(input().rstrip()) for _ in range(N)]
A, B = map(int, input().split())
A -= 1
B -= 1

res = bfs(A)
if not res:
    print(-1)
else:
    print(*list(map(plus, res)))

