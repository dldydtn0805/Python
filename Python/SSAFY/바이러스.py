v = int(input())
e = int(input())
arr = [[0]*(v+1) for _ in range(v+1)]
stack = []
visited = [0] * (v+1)
# 길
route = []
# 바이러스는 양방향으로 전파
for _ in range(e):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
# 방문 기록
n = 1
visited[n] = 1

while True:
    for w in range(v+1):
        if arr[n][w] == 1 and visited[w] == 0:
            #전진
            stack.append(n)
            n = w
            #방문 기록
            visited[n] = 1
            route.append(n)
            break

    else:
        # 후진
        if stack:
            n = stack.pop()

        else:
            break

print(len(route))