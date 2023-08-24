from collections import deque
import sys
sys.stdin = open('input.txt')

input = __import__('sys').stdin.readline

n = int(input())
room = [0]
for _ in range(n):
    room.append(int(input()))

adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))


def dfs(power, room_number, start):
    # 이동이 완료되면 갱신
    ans[start] = room_number

    for togo, need in adj[room_number]:
        # 다음 노드로 갈 수 있는 에너지를 가지고 있고 and 다음 노드가 더 상단에 위치한다면
        if power >= need and room_value[togo][1] < room_value[room_number][1]:
            # 이동하기
            dfs(power - need, togo, start)


# bfs로 1번 룸에서 가장 가까운 방들 순서 정해주기.
def set_room_value_bfs():
    # 방 번호, 방의 level
    room_value = [(0, 0)] * (n + 1)
    value = 1
    q = deque()
    visit = [0] * (n + 1)
    visit[1] = 1
    q.append(1)
    while q:
        for _ in range(len(q)):
            now = q.popleft()
            room_value[now] = (now, value)
            for togo, need in adj[now]:
                if visit[togo] == 0:
                    visit[togo] = 1
                    q.append(togo)
        value += 1
    return room_value


room_value = set_room_value_bfs()
# print(room_value)
ans = [0] * (n + 1)

for i in range(1, n + 1):
    dfs(room[i], i, i)
    print(ans[i])