from collections import deque

N, K = map(int, input().split())

arr = [ i for i in range(1, N+1)]
queue = deque(arr)
ans = []
while len(queue) > 0:
    for _ in range(K-1):
        queue.append(queue.popleft())
    ans.append((queue.popleft()))

print('<', end='')
for i in range(len(ans)):
    print(ans[i], end='')
    if i == N-1:
        break
    print(',', end=' ')
print('>', end='')