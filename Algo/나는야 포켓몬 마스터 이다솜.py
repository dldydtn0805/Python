import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline

n , m = map(int, input().rstrip().split())
dap = []
dict = {}
dict2 = {}
for i in range(1, n+1):
    temp = input().rstrip()
    dict.setdefault(f'{temp}', i)
    dict2.setdefault(f'{i}', temp)
for _ in range(m):
    dap.append(input().rstrip())

for d in dap:
    if d.isnumeric():
        print(dict2[d])
    else:
        print(dict[d])