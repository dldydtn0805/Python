import sys
# sys.stdin = open('input.txt')

n = int(input())

arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))

cnt = [1]*n
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt[i] += 1

print(*cnt)
