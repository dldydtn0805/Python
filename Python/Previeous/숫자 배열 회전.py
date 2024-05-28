import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)
    new_arr90 = []
    new_arr180 = []
    new_arr270 = []
    # 90도 회전
    for j in range(n):
        x = ''
        for i in range(n-1, -1, -1):
                x += str(arr[i][j])
        new_arr90.append(x)

    # 180도 회전
    for i in range(n-1, -1, -1):
        x = ''
        for j in range(n-1, -1, -1):
            x += str(arr[i][j])
        new_arr180.append(x)

    #270도 회전

    for i in range(n-1, -1, -1):
        x = ''
        for j in range(n-1, -1, -1):
            x += str(arr[j][i])
        new_arr270.append(x[::-1])

    print(f'#{tc}')
    for i in range(n):
        print(new_arr90[i], new_arr180[i], new_arr270[i])



