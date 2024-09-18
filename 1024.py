import sys
input = sys.stdin.readline

N, L = map(int, input().split())
num = 0
arr = []
tmp = 0
while num <= 10**9:
    tmp += 1
    num += tmp
    arr.append(num)
arr = [0] + arr
start = L - 1
ans = []
while start < len(arr):
    if N - arr[start] < 0 or start+1 > 100:
        print(-1)
        break
    if (N-arr[start]) % (start + 1)  == 0:
        answer = (N-arr[start]) // (start + 1)
        while start >= 0:
            ans.append(answer)
            answer += 1
            start -= 1
        print(*ans)
        break
    else:
        start += 1
