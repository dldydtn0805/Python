t = int(input())
for i in range(1, t+1):
    n = int(input())
    list22 = list(map(int, input().split()))

    for x in range(n-1, 0, -1):
        for y in range(x):
            if list22[y] > list22[y+1]:
                list22[y], list22[y+1] = list22[y+1], list22[y]

    print(f'#{i}', *list22)
