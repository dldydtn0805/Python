import sys
from collections import deque
# sys.stdin = open('input.txt')
# 트리의 갯수를 cnt에 저장하자
def bfs(start):
    global cnt
    #연결된 노드가 없으면, 단일 트리
    if not graph[start]:
        cnt += 1
        return
    #이미 방문했었으면, 이미 트리 개수를 증가시켰으므로, 포함 안함
    if visited[start]:
        return
    #그 외의 경우는 카운트를 증가시키고
    cnt += 1
    visited[start] = 1
    queue = deque()
    queue.append((0, start))
    #플래그에 이번 트리에 포함된 요소들을 중복되지 않게 체크해준다
    flag = [0] * (n + 1)
    flag[start] = 1
    flag2 = 0
    while queue:
        pre, cur = queue.popleft()
        for to in range(len(graph[cur])):
            next = graph[cur][to]
            if not visited[next]:
                visited[next] = 1
                # 다음으로 갈 노드가 방문한 적이 없는 노드라면, 큐에 다음으로갈 노드와 현재 노드를 같이 저장해준다
                queue.append((cur, next))
            #만약 다음으로 갈 노드가 바로 직전에 온 노드가 아닐때, 다음으로 갈 노드가 트리에 방문했었다면 flag2를 들어준다
            if next != pre:
                if flag[next]:
                    flag2 = 1
            flag[next] = 1
    # 만약 플래그 2가 들어져 있다면 트리가 아니므로 카운트를 감소시킨다
    if flag2:
        cnt -= 1
# 그래프를 입력받고 , BFS를 돌려서 트리여부를 판단해보자 !
tc = 0
while True:
    tc += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        f, t = map(int, input().split())
        graph[f].append(t)
        graph[t].append(f)
    cnt = 0
    visited = [0]*(n+1)

    for i in range(1,n+1):
        bfs(i)
    if cnt > 1:
        print(f'Case {tc}: A forest of {cnt} trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: No trees.')
