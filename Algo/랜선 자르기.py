import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
'''
가장 작은 숫자를 기준으로 모든 숫자를 빼준다 cnt가 N이 됐다면 clear

만약 실패했다면 

가장 작은 숫자보다 -1 한 수를 기준으로 모든 숫자를 빼준다
'''

K, N = map(int, input().split())
arr = []
for k in range(K):
    arr.append(int(input()))
cnt = 0
temp = max(arr)
start = 0
end = temp * 2
while start <= end:
    mid = (start + end) // 2
    if not mid:
        break
    cnt = 0
    for a in arr:
        cnt += a // mid
    if cnt >= N:
        result = mid
        start = mid + 1
    if cnt < N:
        end =  mid - 1
print(result)