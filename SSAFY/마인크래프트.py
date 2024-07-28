import sys; sys.stdin = open('input.txt')

N, M, B = map(int, input().split())

blocks = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    blocks.append(a)
    blocks.append(b)
    blocks.append(c)
    blocks.append(d)


print(blocks)

blocks.sort()

print(blocks)
ans = 0
for i in range(len(blocks)-1):
    if B == 0:
        blocks.sort(reverse=True)
        blocks[-1] -= 1
        B += 1
        ans += 2
    while blocks[i] < blocks[i+1] and B > 0:
        blocks.sort()
        blocks[i] += 1
        B -= 1
        ans += 1
        if B == 0:
            blocks.sort(reverse=True)
            blocks[-1] -= 1
            B += 1
            ans += 2
print(ans, max(blocks))