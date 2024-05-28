import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())


cnt = [0]*8002
arr = []
sum_v = 0
for _ in range(n):
    temp = int(input())
    sum_v += temp
    arr.append(temp)
    cnt[temp+4000] += 1
arr.sort()
print(round((sum_v/n)))
print(arr[n//2])

max_v = max(cnt)
flag = 0
flag2 = 0
temp22 =[]
for c in range(len(cnt)):
    if cnt[c] == max_v:
        temp22.append(c)

temp22.sort()

if len(temp22) == 1:
    print(temp22[0]-4000)
else:
    print(temp22[1]-4000)

print(max(arr)-min(arr))