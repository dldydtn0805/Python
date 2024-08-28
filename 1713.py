import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
arr = list(map(int, input().split()))
candi = {}
for i in range(len(arr)):
    if len(candi) < N:
        if arr[i] not in candi:
            candi[arr[i]] = [1, i]
        else:
            candi[arr[i]][0] += 1
    else:
        if arr[i] in candi:
            candi[arr[i]][0] += 1
        else:
            min_v = 1e9
            min_k = 1e9
            min_idx = 1e9
            for key, value in candi.items():
                if min_v > value[0]:
                    min_v = value[0]
                    min_idx = value[1]
                    min_k = key
                elif min_v == value[0]:
                    if min_idx > value[1]:
                        min_k = key
            candi.pop(min_k)
            candi[arr[i]] = [1, i]
answer = []
for key in candi.keys():
    answer.append(key)
print(*sorted(answer))
