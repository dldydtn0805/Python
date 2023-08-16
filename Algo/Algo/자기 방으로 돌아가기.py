import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    cross = []
    for i in range(n):
        a,b = arr[i]
        for j in range(i+1, n):
            flag = 0
            for k in range(2):
                if a < arr[j][k] < b:
                    flag = 1
            if flag:
                cross += arr[j]

    print(f'#{tc}', len((cross))//2+1)





