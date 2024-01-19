import sys
# sys.stdin = open('input.txt')
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = []
# 분할정복 Devide And Conquer
def DAC(x, y, n):

    # x,y 좌표의 색을 기준으로 한다
    color = arr[x][y]
    # n 범위 만큼 탐색해서 만약 범위에 다른 색이 있다는게 확인되면
    # 분할한다
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                # 분할 다음과 같이 진행한다
                # 좌표를 [x,y] / [x,y+n//2] / [x+n//2, y] / [x+n//2, y+n//2] 네 구역으로 나눈다
                # 범위를 n//2로 좁힌다
                # 그리고 return
                DAC(x, y, n//2)
                DAC(x, y+n//2, n//2)
                DAC(x+n//2, y, n//2)
                DAC(x+n//2, y+n//2, n//2)
                return
    # 만약 분할하지 않았다면 그대로 결과 값에 저장해준다
    if color == 0:
        result.append(0)
    else:
        result.append(1)

DAC(0,0,n)
print(result.count(0))
print(result.count(1))


