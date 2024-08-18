import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(N)]
ans = 1e9
for i in range(N):
    if i == 0:
        prefix[i] = arr[i]
    else:
        prefix[i] = prefix[i-1] + arr[i]

i = 0
j = 0

if prefix[0] >= S:
    ans = min(ans, 1)

if prefix[N-1] >= S:
    ans = min(ans, N)

while i < N:
    if prefix[i] - prefix[j] >= S:
        ans = min(ans, i-j)
        if prefix[i] - prefix[j+1] >= S:
            j += 1
        else:
            i += 1
    else:
        i += 1
print(ans if ans != 1e9 else 0)
