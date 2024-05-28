import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dict = {}
arr = []
for i in range(N):
    joy = input().rstrip()
    if len(joy) >= M:
        if joy not in dict.keys():
            dict[joy] = 1
        else:
            dict[joy] += 1

for key, value in dict.items():
     arr.append((value, key))


arr.sort(key = lambda x: (-x[0], -len(x[1]), x[1]))

for item in arr:
    print(item[1])

