import sys
input = sys.stdin.readline
from collections import defaultdict

def binary_search(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1


M, N = map(int, input().split())
visited = []
space = [list(map(int, input().split())) for _ in range(M)]
ans = defaultdict(int)
answer = 0

for planet in space:
    sorted_planet = sorted(planet)
    rank = [0 for _ in range(len(planet))]
    for p in range(len(planet)):
        res = binary_search(0, len(planet)-1, sorted_planet, planet[p])
        rank[p] = res
    res = tuple(rank)
    answer += ans[res]
    ans[res] += 1
print(answer)
