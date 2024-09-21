import sys
input = sys.stdin.readline

S = input().rstrip()
N = len(S)

cur = S[0]
for i in range(1, len(S)):
    if cur[i-1] < S[i]:
        cur = S[i] + cur
    else:
        cur = cur + S[i]
print(cur[::-1])
