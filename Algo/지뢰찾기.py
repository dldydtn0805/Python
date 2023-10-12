import sys
sys.stdin = open('input.txt')

"""
숫자칸의 정보는 인근 8개 칸에 있는 지뢰의 개수를 알려준다

최대 몇개의 지뢰가 있을 수 있는가?

최대한 중복된 위치에 지뢰가 없는 곳을 설정해야할까?

"""

n = int(input())
arr = [list(input()) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        flag = True
        if arr[i][j] == '#':
            for di, dj in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
                if arr[i+di][j+dj] == '0':
                    flag = False
            if flag:
                cnt += 1
print(cnt)
