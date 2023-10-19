import sys
# sys.stdin = open('input.txt')

n = int(input())

arr = []

dict = {}
for _ in range(n):
    temp, temp_inform = input().split()
    dict.setdefault(f'{temp}', 0)
    if temp_inform == 'enter':
        dict[f'{temp}'] += 1
    else:
        dict[f'{temp}'] -= 1


for key, value in dict.items():
    if value:
        arr.append(key)

arr.sort(reverse=True)
for a in arr:
    print(a)