import sys
# sys.stdin = open('input.txt')

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((y,x))

arr.sort()
for item in arr:
    print(*item[::-1])