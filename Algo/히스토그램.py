import sys
input = sys.stdin.readline
N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))
arr = [1e9] + arr + [1e9]
arr2 = arr[:]
arr2.reverse()
stack = []
stack2 = []
result1 = [0 for _ in range(N+2)]
result2 = [0 for _ in range(N+2)]
stack.append((arr[1], 1))
stack2.append((arr2[1], 1))
# 왼쪽부터 갈때
for i in range(1, N+2): # N번
    while stack:
        if stack[-1][0] >= arr[i]:
            stack.pop()
        else:
            result1[i] = stack[-1][1]
            break
    stack.append((arr[i], i))
# 오른쪽부터 갈때
for i in range(1, N+2):
    while stack2:
        if stack2[-1][0] >= arr2[i]:
            stack2.pop()
        else:
            result2[i] = stack2[-1][1]
            break
    stack2.append((arr2[i], i))

for i in range(len(result2)):
    result2[i] = N - result2[i] - 1

result2.reverse()

result1.pop()
result1.pop(0)
result2.pop()
result2.pop(0)
arr.pop()
arr.pop(0)
ans = [0]*N
for i in range(N):
    ans[i] = abs(result2[i] - result1[i] + 1) * arr[i]

print(max(ans))