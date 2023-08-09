import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    # i는 x좌표
    for i in range(-n, n+1):
        # j는 y좌표
        for j in range(-n, n+1):
           if i**2 + j ** 2 <= n**2:
               cnt+=1
    print(f'#{tc}', cnt)
