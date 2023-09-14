import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))
result = []
temp = 0
for i in range(n-1, -1, -1):
    if arr[:i] and max(arr[:i]) > arr[i]:
        for j in range(i-1, -1, -1):
            if arr[i] < arr[j]:
                temp = j+1
                break
    result.append(temp)
    temp = 0
print(*result[::-1])
