import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    pan = [list(input()) for _ in range(n)]
    omok = False
    # 가로줄 오목 탐색
    for i in range(n):
        cnt = 0
        for j in range(n):
            if pan[i][j]=='o':
                cnt+=1
            else:
                cnt=0
            # 5개 이상이기만 하면 되므로
            if cnt ==5:
                omok = True

    # 세로줄 오목 탐색
    for i in range(n):
        cnt = 0
        for j in range(n):
            if pan[j][i]=='o':
                cnt+=1
            else:
                cnt=0
            # 5개 이상이기만 하면 되므로
            if cnt == 5:
                omok = True

    # 대각선 오목 탐색
    for j in range(-n, n, 1):
        cnt = 0
        for i in range(n):
            if 0<=j+i<n:
                # j로 대각선 모양을 위 아래로 조절해준다
                # 원래 형태는 우 상향 대각선
                if pan[j+i][n-1-i] == 'o':
                    cnt+=1
                else:
                    cnt=0
                # 5개 이상이기만 하면 되므로
                if cnt == 5:
                    omok = True

    #반대편 대각선 탐색
    for j in range(-n,n,1):
        cnt = 0
        for i in range(n):
            if 0 <=j+i <n :
                # j로 대각선 모양을 위 아래로 조절해준다
                # 기본 형태는 우 하향 대각선
                if pan[j+i][i] == 'o':
                    cnt += 1
                else:
                    cnt =0
                # 5개 이상이기만 하면 되므로
                if cnt == 5:
                    omok = True

    if omok:
        print(f'#{tc}', 'YES')
    else:
        print(f'#{tc}', 'NO')

