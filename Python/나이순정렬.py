import sys
# sys.stdin = open('input.txt')

n = int(input())

arr = []
cnt = 0
for _ in range(n):
    age, name = input().split()
    arr.append([int(age), name, cnt])
    cnt += 1

arr.sort(key = lambda x:x[2])
arr.sort(key = lambda x:x[0])

for item in arr:
    print(*item[:2])
