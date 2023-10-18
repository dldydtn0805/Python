import sys
# sys.stdin = open('input.txt')

n = int(input())

arr = list(map(int, input().split()))

temp = list(set(arr))
dict = {}
for item in arr:
    dict.setdefault(f'{item}', 0)

temp.sort()

for i in range(len(temp)):
    dict[f'{temp[i]}'] = i

for element in arr:
    print(dict[f'{element}'], end=' ')