import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stacks = [0, 0, 0, 0]
for i in range(N):
    diff = 1e9
    tmp = -1
    for j in range(len(stacks)):
        if diff > A[i] - stacks[j] and A[i] > stacks[j]:
            diff = A[i] - stacks[j]
            tmp = j
    if tmp == -1:
        print('NO')
        exit()
    else:
        stacks[tmp] = A[i]
print('YES')
