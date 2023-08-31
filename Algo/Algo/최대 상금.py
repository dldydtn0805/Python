import sys
sys.stdin = open('input.txt')
def change(i, cnt):
    global max_v, flag
    if cnt == b:
        print(a)
        a2 = ''
        for a1 in a:
            a2 += a1
        a2 = int(a2)
        if max_v < a2:
            max_v = a2
        return

    if max_v == max_a:
        flag = 1

    if flag:
        change(i, cnt + 1)

    else:
        for j in range(len(a)):
            if i < j and int(a[i]) <= int(a[j]):
                a[i], a[j] = a[j], a[i]
                change(i+1, cnt+1)
                a[i], a[j] = a[j], a[i]


T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    a = list(str(a))
    max_a = int(''.join(sorted(a, reverse=True)))
    max_v = 0
    flag = 0
    change(0, 0)
    print(f'#{tc}', max_v)
