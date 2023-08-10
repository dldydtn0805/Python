import sys
sys.stdin = open('input.txt')



for tc in range(1, 11):
    case, v = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[0]*100 for _ in range(100)]
    visited = [0]*(100)
    for i in range(0, len(arr)-1, 2):
        v1, v2 = arr[i], arr[i+1]
        adj[v1][v2] = 1

    route = []

    stack = []

    visited = [0]*100

    n = 0
    route.append(n)
    visited[n] = 1

    while True:
        for w in range(0, 100):
            if adj[n][w] == 1 and visited[w] == 0:

                stack.append(n)

                n = w
                route.append(n)

                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()

            else:
                break
    # print(route)
    if visited[99] == 1:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)