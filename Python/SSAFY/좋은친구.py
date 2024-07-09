import sys
from collections import defaultdict
# sys.stdin = open('input.txt')

n, k = map(int, input().split())
arr = [len(input()) for i in range(n)]
dict = defaultdict(int)
count = 0
for i, num in enumerate(arr):
    if i > k:
        dict[arr[i-k-1]] -= 1
    count += dict[arr[i]]
    dict[arr[i]] += 1
print(count)