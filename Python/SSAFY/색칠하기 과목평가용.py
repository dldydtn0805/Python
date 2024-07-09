"""
그림과 같이 인덱스가 있는 10X10 격자에 빨간색과 파란색을 칠하려고 한다

N개의 영역에 대해 왼쪽 위와 오른쪽  아래 모서리 인덱스, 칠할 색상이 주어질때

칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오

입력

테스트 케이스에 첫줄에 칠한 영역의 갯수 N이 주어진다

왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2, 색상 정보 color가 주어진다
"""
#
# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 빈 리스트 선언할때, ** [[0]*10]*10 하면 안됨
    blank = [[0]*10 for _ in range(10)]
    for _ in range(N):
        arr = list(map(int, input().split()))
        # 사각형 가로 범위 설정
        for i in range(arr[0], arr[2]+1):
            # 사각형 세로 범위 설정
            for j in range(arr[1], arr[3]+1):
                # 해당 요소가 비어있으면, 색칠한다
                if blank[i][j] == 0:
                    blank[i][j] = arr[4]
                # 해당 요소가 비어있지 않고, 현재 칠할 색과 다르다면, 보라색으로 칠한다
                if blank[i][j] != 0 and blank[i][j] != arr[4]:
                    blank[i][j] = 'purple'
    cnt = 0
    #보라색 갯수 탐색
    for i in range(10):
        for j in range(10):
            if blank[i][j] == 'purple':
                cnt += 1
    print(f'#{tc}', cnt)
