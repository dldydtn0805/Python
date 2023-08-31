import sys
sys.stdin = open('input.txt')
def change(i, cnt):
    global max_v, flag
    if cnt == b:
        # print(a)
        a2 = ''
        for a1 in a:
            a2 += a1
        a2 = int(a2)
        if max_v < a2:
            max_v = a2
        return
    else:
        for j in range(len(a)):
            if i < j and a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
                change(i+1, cnt+1)
                a[i], a[j] = a[j], a[i]
            if i != j and a[i] == a[j]:
                flag = 1
        if flag:
            change(i, cnt + 1)
        else:
            a[len(a)-1], a[len(a)-2] = a[len(a)-2], a[len(a)-1]
            change(i, cnt+1)
            a[len(a) - 1], a[len(a) - 2] = a[len(a) - 2], a[len(a) - 1]

T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    a = list(str(a))
    max_v = 0
    flag = 0
    used= [0]*len(a)
    p = [0]*len(a)
    change(0, 0)
    print(f'#{tc}', max_v)