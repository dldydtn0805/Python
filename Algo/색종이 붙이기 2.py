import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)
def isOkay(x, y, arr):
    #x,y 좌표에서 색종이 들어 맞는게 있으면 True를 반환해라
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if x+i >= 10 or y + j >= 10:
                continue
            if paper[x+i][y+j] == 0:
                return False
    return True

def let_Visited(x, y, arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if x + i >= 10 or y + j >= 10:
                continue
            visited[x+i][y+j] = 1
            paper[x+i][y+j] = 0

def return_Visited(x, y, arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if x + i >= 10 or y + j >= 10:
                continue
            visited[x+i][y+j] = 0
            paper[x+i][y+j] = 1

def bruteForce(cur_i, cur_j, cnt1, cnt2, cnt3, cnt4):
    global max_v
    if cnt1 > 5 or cnt2 > 5 or cnt3 > 5 or cnt4 > 5:
        return
    total = 0
    for i in range(10):
        for j in range(10):
            total += paper[i][j]
    # print(cnt1, cnt2, cnt3, cnt4)
    if total == 0:
        print(visited)
        print(cnt1, cnt2, cnt3, cnt4)
        return
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1:
                if isOkay(i,j,color1) and not visited[i][j]:
                    let_Visited(i, j, color1)
                    bruteForce(i, j, cnt1+1, cnt2, cnt3, cnt4)
                    # return_Visited(i, j, color1)
            if paper[i][j] == 1:
                if isOkay(i,j,color2) and not visited[i][j]:
                    let_Visited(i, j, color2)
                    bruteForce(i, j, cnt1, cnt2+1, cnt3, cnt4)
                    # return_Visited(i, j, color2)
            if paper[i][j] == 1:
                if isOkay(i,j,color3) and not visited[i][j]:
                    let_Visited(i, j, color3)
                    bruteForce(i, j, cnt1, cnt2, cnt3+1, cnt4)
                    # return_Visited(i, j, color3)
            if paper[i][j] == 1:
                if isOkay(i,j,color4) and not visited[i][j]:
                    let_Visited(i, j, color4)
                    bruteForce(i, j, cnt1, cnt2, cnt3, cnt4+1)
                    # return_Visited(i, j, color4)

paper = [list(map(int,input().split())) for _ in range(10)]
color1 = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
color2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
color3 = [
        [0,0],
        [0,0]
    ]
color4 = [
        [0]
    ]

visited = [[0]*10 for _ in range(10)]
max_v = 0
bruteForce(0,0,0,0,0,0)