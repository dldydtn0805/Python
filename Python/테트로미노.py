import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(start_i, start_j, tetris_value, tetris_length):
    global ans

    # 테트리스 길이가 4일때 함수를 되돌린다
    if tetris_length == 4:
        if ans < tetris_value:
            ans = tetris_value
        return

    visited[start_i][start_j] = True
    
    for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        updated_i, updated_j = start_i + di, start_j + dj
        if 0<=updated_i<N and 0<=updated_j<M and not visited[updated_i][updated_j]:
            # 테트리스 길이 3에서 결과 값과 미리 비교하여 백트래킹을 시도
            if tetris_length == 3 and tetris_value + tetris[updated_i][updated_j] < ans:
                continue
            dfs(updated_i,updated_j, tetris_value + tetris[updated_i][updated_j] , tetris_length+1)

            # 함수에서 빠져나온 뒤에 방문했던 사실 또한 되돌려주어야 한다
            visited[updated_i][updated_j] = False


N, M = map(int, input().split())
tetris = [list(map(int, input().split())) for _ in range(N)]

# ans에 최댓값을 갱신해준다
ans = 0

# visited 를 for 문 밖에서 선언해준다
visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        # dfs 안에서 길이 4의 테트리스 형태의 값을 찾아준다 (단, ㅗ 모양은 찾을수 없다)
        dfs(i,j,tetris[i][j],1)
        # 함수에서 빠져나온 뒤에 방문했던 사실 또한 되돌려주어야 한다
        visited[i][j] = False
        # ㅗ 모양을 left, right, up, down 케이스로 나누어 값을 찾는다
        left, right, up, down = 0, 0, 0, 0
        if 0<=j-1<M and 0<=i-1<N and 0<=i+1<N:
            left = tetris[i][j] + tetris[i][j-1] + tetris[i-1][j] + tetris[i+1][j]
        if 0<=j+1<M and 0<=i-1<N and 0<=i+1<N:
            right = tetris[i][j] + tetris[i][j+1] + tetris[i-1][j] + tetris[i+1][j]
        if 0<=j+1<M and 0<=j-1<M and 0<=i-1<N:
            up = tetris[i][j] + tetris[i][j+1] + tetris[i][j-1] + tetris[i-1][j]
        if 0<=j+1<M and 0<=j-1<M and 0<=i+1<N:
            down = tetris[i][j] + tetris[i][j+1] + tetris[i][j-1] + tetris[i+1][j]
        ans = max(ans, left, right, up, down)

print(ans)