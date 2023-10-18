import sys
# sys.stdin = open('input.txt')

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

arr = list(set(arr))

arr.sort()
arr.sort(key = lambda x : len(x))

for item in arr:
    print(item)