import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
outlet = []
for i in range(N):
    if len(outlet) < M:
        outlet.append(arr[i])
    else:
        outlet[outlet.index(min(outlet))] += arr[i]
print(max(outlet))
