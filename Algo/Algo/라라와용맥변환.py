import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = list(input())

print(n, m)

hp = [m]*n

print(hp)

print(arr)

flags = [0]*n
# 해 = 1 바람 = 2 강  = 3
q = []
hps = {}
print(hps)
for i in range(n):
    print(arr[i])
    q.append(arr[i])
    for k, v in hps.items():
        if v == 0:
            hps.pop(k)
            q.remove(k)
    if arr[i] not in hps:
        q.append(arr[i])
        hps = {arr[i]:n}
    else:
        for i in ['S','W','R'] and i != arr[i] and i not in q:
            hps = {i:n}
print(hps)