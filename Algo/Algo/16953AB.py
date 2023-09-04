from collections import deque
def bfs(a):
    queue = deque()
    queue.append((a,1))
    while queue:
        n,t = queue.popleft()
        if n>b:
            continue
        if n==b:
            return t
            break
        queue.append((int(str(n)+'1'), t+1))
        queue.append((n*2,t+1))


# import sys
# sys.stdin = open('input.txt')
a, b = map(int, input().split())
result = bfs(a)
if result:
    print(result)
else:
    print(-1)
