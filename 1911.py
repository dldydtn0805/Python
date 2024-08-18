import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
cnt = 0
prev = -1
for i in range(N):
    if prev != -1:
        if arr[i][0] < prev < arr[i][1]:
            arr[i][0] = prev
        elif arr[i][1] <= prev:
            continue
    width = arr[i][1] - arr[i][0]
    if width > L:
        if not width % L:
            cnt += width // L
        else:
            cnt += width // L + 1
            prev = arr[i][0] + (width // L + 1) * L
    else:
        cnt += 1
        prev = arr[i][0] + L
print(cnt)
