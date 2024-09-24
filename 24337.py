import sys
input = sys.stdin.readline
N, a, b = map(int, input().split())
buildings = []
if a > b:
    buildings.append(a)
    left = [i for i in range(1, a)]
    right = [j for j in range(b-1, 0, -1)]
    fix = [1 for _ in range(N-a-b+1)]
    if b == 1:
        buildings = fix + left + buildings + right
    else:
        buildings = fix + left + buildings + right
else:
    buildings.append(b)
    left = [i for i in range(1, a)]
    right = [j for j in range(b - 1, 0, -1)]
    fix = [1 for _ in range(N - a - b + 1)]
    if a == 1:
        buildings = left + buildings + fix + right
    else:
        buildings = fix + left + buildings + right
if len(buildings) > N:
    print(-1)
else:
    print(*buildings)
