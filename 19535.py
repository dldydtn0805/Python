import sys
input = sys.stdin.readline

N = int(input())
lines = []
degrees = [0 for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    lines.append((u, v))
    degrees[u] += 1
    degrees[v] += 1

D = 0
G = 0

for i in range(N):
    G += degrees[i] * (degrees[i]-1) * (degrees[i]-2) / 6 if degrees[i] >= 3 else 0

for line in lines:
    v1, v2 = line
    D += ((degrees[v1] -1 ) * (degrees[v2]-1))

if D > 3*G:
    print('D')
elif D < 3*G:
    print('G')
else:
    print('DUDUDUNGA')
