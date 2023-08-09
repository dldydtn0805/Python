import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    # 파스칼의 삼각형 구성
    for i in range(n):
        for j in range(n):
            # 양 끝은 1로 설정
            if j == 0 or j == n-1:
                arr[i][j] = 1
            # 내부 삼각형 연산
            if 0<j<n-1:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    print(f'#{tc}')
    # 모양 대로 출력
    for i in range(n):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()