import sys
sys.stdin = open('input.txt')
# 방문을 해주면서 최소 합을 구해주는 BFS
def bfs(si, sj):
    visited = [[0]*n for _ in range(n)]
    queue = []
    queue.append((si,sj))
    visited[si][sj] = arr[si][sj]
    while queue:
        # 이동하면서 갱신하기위해 pop
        i, j = queue.pop(0)
        for di, dj in [[1,0],[-1,0], [0,1], [0,-1]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<n and 0<=nj<n:
                # 큐에 이동한 위치를 담아주고 이동한 위치에서의 합을 넣어준다
                if not visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
                    queue.append((ni,nj))
                # 만약에 현재 합보다 갱신할 합이 더 작으면 갱신해준다
                elif visited[ni][nj] > visited[i][j] + arr[ni][nj]:
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]
    return visited[n-1][n-1]

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc}', bfs(0,0))

