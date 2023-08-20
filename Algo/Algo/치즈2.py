import sys
sys.stdin = open('input.txt')

def bfs(si, sj):
    # 노 치즈 존
    queue = []
    # 외곽 치즈 저장소
    temp = []
    visited = [[0]*m for _ in range(n)]
    # 큐, 방문 세팅
    visited[si][sj] = 1
    queue.append((si,sj))
    # 치즈 녹는 시간
    cnt = 1
    while True:
        # 노 치즈 존을 순회하기
        if queue:
            i, j = queue.pop(0)
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<n and 0<=nj<m:
                    # 방문 안했을때만!
                    if visited[ni][nj] == 0:
                        # 치즈가 없다면 노 치즈 존에 넣은 후 방문 처리
                        if graph[ni][nj] == 0:
                            queue.append((ni,nj))
                            visited[ni][nj] = 1
                        # 치즈가 있다면 외곽 치즈 저장소에 넣고 치즈 녹는 시간 입력
                        elif graph[ni][nj] == 1:
                            temp.append((ni,nj))
                            visited[ni][nj] = cnt+1
        # 노 치즈 존 순회 끝났다면
        else:
            # 만약 외곽 치즈 저장소가 비었으면 끝내기
            if not temp:
                break
            # 만약 외곽 치즈 저장소가 있다면, 치즈 값을 0으로 하고 노 치즈 존에 넣어준다
            else:
                for i in temp:
                    a, b = i
                    graph[a][b] = 0
                    queue.append((a,b))
                # 녹는 시간 추가 해주고 임시 치즈 저장소 비워준다
                cnt += 1
                temp.clear()

    return visited

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

# 최종적으로 반환된 모든 치즈의 녹는 시간
chz = bfs(0,0)
# 최후의 치즈 탐색
max_v = 0
for i in range(n):
    for j in range(m):
        if max_v < chz[i][j]:
            max_v = chz[i][j]
# 최후의 치즈 개수를 탐색
max_cnt = 0
for i in range(n):
    for j in range(m):
        if max_v == chz[i][j]:
            max_cnt += 1
# 최후의 치즈 녹는 시간
print(max_v-1)
# 최후의 치즈 개수
print(max_cnt)

