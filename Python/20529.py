import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    N = int(input())
    arr = list(input().split())
    if N > 32: print(0)
    else:
        min_v = 1e9
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    cnt = 0
                    for l in range(4):
                        if arr[i][l] != arr[j][l]:
                            cnt += 1
                        if arr[j][l] != arr[k][l]:
                            cnt += 1
                        if arr[i][l] != arr[k][l]:
                            cnt += 1
                    if min_v > cnt: min_v = cnt
        print(min_v)
