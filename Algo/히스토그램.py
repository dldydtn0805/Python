N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))
arr = [1e9] + arr + [1e9]

print(arr)
stack = []
result1 = [0 for _ in range(N+2)]
result2 = [0 for _ in range(N+2)]
stack.append((arr[1], 1))

for i in range(1, N+2):
    while stack:
        if stack[-1][0] >= arr[i]:
            stack.pop()
        else:
            result1[i] = stack[-1][1]
            break
    stack.append((arr[i], i))

print(result1)
stack = []
stack.append((arr[N+1], N+1))
for i in range(N+1, 1, -1):
    while stack:
        if stack[-1][0] >= arr[i]:
            stack.pop()
        else:
            result2[i] = stack[-1][1]
            break
    stack.append((arr[i], i))
print(result2)