t = int(input())

for tc in range(1, t+1):
#숫자를 입력받는다
    number = int(input())
    c = [0]*12
    for i in range(6):
        c[number % 10] += 1
        number //= 10
    i = 0
    run11 = 0
    tri = 0
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run11 += 1
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run11 += 1
        i += 1
    if run11 == 1 and tri == 1:
        print(f'#{tc}', 1)
    elif tri == 2:
        print(f'#{tc}', 1)
    elif run11 == 2:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)

