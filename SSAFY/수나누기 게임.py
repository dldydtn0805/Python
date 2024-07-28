import sys

# sys. stdin = open ( 'input.txt' )

n = int(input())

arr = list(map(int, input().split()))

max_v = max(arr)
card = [-1] * (max_v+1)
for i in range(n):
    card[arr[i]] = i

result = [0] * n
for num in range(len(card)):
    if card[num] != -1:
        idx = card[num]
        for i in range(2*num, max_v+1, num):
            if card[i] != -1:
                result[idx] += 1
                result[card[i]] -= 1
print(*result)

