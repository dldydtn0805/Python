T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = int(input())

    c = [0]*10

    for j in range(N):
        c[number % 10] += 1
        number //= 10

    i = 0
    check = 0
    while i < 10:
        if c[i] >= check:
            check = c[i]
            num = i
        i += 1
    print(f'#{tc}', num, check)

