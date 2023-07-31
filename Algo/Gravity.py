T = int(input())
for i in range(T):
    n = int(input())
    arr22 = list(map(int, input().split()))
    count22 = 0
    for l in arr22:
        count22 += 1
    for j in range(n):
        max22 = 0
        count33 = 0
        for zz in range(count22):
            if max22 <= arr22[zz]:
                max22 = arr22[zz]
                continue
            else:
                count33 += 1
    print(count33)
