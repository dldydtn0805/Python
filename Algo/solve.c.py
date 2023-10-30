from collections import deque
n = int(input())
temp = round(n * 0.15 + 0.0000001)
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)
arr.sort()
arr = deque(arr)
if n == 0:
    print(0)
    exit()
i = temp
while i:
    arr.pop()
    i -= 1
j = temp
while j:
    arr.popleft()
    j -= 1
print(round(sum(arr)/len(arr) + 0.0000001))