import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            pass
        elif i == 0:
            maze[i][j] = maze[i][j-1] + maze[i][j]
        elif j == 0:
            maze[i][j] = maze[i-1][j] + maze[i][j]
        else:
            maze[i][j] = max(maze[i-1][j] , maze[i][j-1] ) + maze[i][j]
print(maze[-1][-1])
