import sys
sys.stdin = open('input.txt')
def change(cnt):
    global result

    temp = ''
    for number in a:
        temp += number

    if int(temp) in result[cnt]:
        return
    else:
        result[cnt].append(int(temp))

    if cnt == 0:
        return

    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            a[i], a[j] = a[j], a[i]
            change(cnt - 1)
            a[i], a[j] = a[j], a[i]


T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    a = list(str(a))
    flag = 0
    max_v = 0
    result = [[] for _ in range(int(b)+1)]
    change(b)
    print(f'#{tc}', max(result[0]))