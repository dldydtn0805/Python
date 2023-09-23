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
            # paper[x+i][y+j] = 0

def return_Visited(x, y, arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if x + i >= 10 or y + j >= 10:
                continue
            visited[x+i][y+j] = 0

def bruteForce(cnt, cur_i, cur_j):
    global max_v
    # for i in range(len(paper_cnt)):
    #     if paper_cnt[i] > 5:
    #         return
    # total = 0
    # for i in range(10):
    #     for j in range(10):
    #         total += paper[i][j]
    # if total == 0:
    #     print(paper_cnt)
    #     return
    if visited == paper:
        print(visited)
        print(paper_cnt)
    for i in range(cur_i, 10):
        for j in range(cur_j, 10):
            if paper[i][j] == 1:
                for k in range(len(color)):
                    if isOkay(i,j,color[k]) and not visited[i][j]:
                        let_Visited(i, j, color[k])
                        paper_cnt[k] += 1
                        bruteForce(cnt+1, i, j)
                        # return_Visited(i, j, color[k])
                        # paper_cnt[k] -= 1


paper = [list(map(int,input().split())) for _ in range(10)]
color = [
    [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [
        [0,0],
        [0,0]
    ],
    [
        [0]
    ]
]
visited = [[0]*10 for _ in range(10)]
paper_cnt = [0]*4
max_v = 0
bruteForce(0,0,0)