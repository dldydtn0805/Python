import sys
# sys.stdin = open('input.txt')

n, m = map(int, input().split())

dict = {}
for _ in range(n+m):
    temp = input()
    dict.setdefault(f'{temp}', 0)
    dict[temp] += 1

arr = []
cnt = 0
for key, value in dict.items():
    if value > 1:
        arr.append(key)
        cnt += 1
arr.sort()

print(cnt)
for a in arr:
    print(a)