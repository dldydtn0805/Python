import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}
arr = []
for _ in range(n):
    dict.setdefault(f'{input()}', 0)
for _ in range(m):
    temp = input()
    if temp in dict:
        dict[f'{temp}'] += 1

sum_v = 0
for key, value in dict.items():
    sum_v += value

print(sum_v)