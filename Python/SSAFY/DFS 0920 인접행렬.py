# 인접 행렬
# 장점 = 사용이 간편하다, 구현이 쉽다
# 단점 = 메모리 낭비 - 0도 표시하기 때문에

graph = [
    [0,1,0,1,0],
    [1,0,1,1,1],
    [0,1,0,0,0],
    [1,1,0,0,1],
    [0,1,0,1,0]
]

# make_star
# stack 버전
def make_star_stack(start):
    visited = []
    stack = [start]
    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue
        #방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 갈수있는 곳들을 stack에 추가
        # 큰 번호부터 조회 하고 싶다면
        # for next in range(5):
        # 작은번호부터 조회 하고 싶다면
        for next in range(4,-1,-1):
            # 연결이 안되어있다면 continue
            if graph[now][next] == 0:
                continue #재귀 등을 구현할때 조건을 만족하지 않을때를 기준으로 pass하는 방식으로 구현해보자 like prunning

            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)
    return visited
print("make_star stack = ", end= '')
print(*make_star_stack(0))
# 재귀
# map 크기, 길이를 알때 append 형식 말고 아래와 같이 사용하면 빠르다
visited = [0]*5
path = [] # 방문 순서 기록

def make_star(now):
    visited[now] = 1 # 현재지점 방문 표시
    #print(now, end=' ')
    path.append(now)
    # 인접한 노드들을 방문
    for next in range(5):
        if graph[now][next] == 0:
            continue
        if visited[next]:
            continue
        make_star(next)

print('make_star 재귀 =', end=' ')
make_star(0)
print(path)
