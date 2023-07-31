T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    check = 0
    check22 = 0
    for j in range(n):
        check = 0
        for k in range(j, n):
            if arr[j] > arr[k]:
                check += 1
        if check > check22:
            check22 = check
    print(f'#{i+1}', check22)
