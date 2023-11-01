N = int(input())
arr = []
stack = []

for i in range(N):
    num = int(input())
    arr.append(num)
arr = [0,0] + arr
result = [[] for _ in range(N)]
stack.append((1,arr[1]))
for i in range(2, N):
    now = (i, arr[i])
    while stack:
        if stack[-1][1] >= now[1]:
            stack.append(now)
        else:
            a, b = stack.pop()
            result[now[0]].append(a)

print(result)
