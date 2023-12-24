import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque()
    # 큐에 들어갈 것은 값과, 수식이다
    queue.append((start, ''))
    visited = [False] * 10001
    # bfs 로 작동하므로 가장 가까운 순서대로 반영된다
    while queue:

        current_value, current_susik = queue.popleft()

        # 목표 값에 도달했으므로 return 시켜준다
        if current_value == B:
            print(current_susik)
            return

        # zfill 메서드를 이용해서 0으로 채워진 네자리 숫자를 만들고 left 계산 값과 right 계산 값을 할당해준다
        stringfied_value = (str(current_value).zfill(4))
        left_rotated_value = int(stringfied_value[1]+stringfied_value[2]+stringfied_value[3]+stringfied_value[0])
        right_rotated_value = int(stringfied_value[3]+stringfied_value[0]+stringfied_value[1]+stringfied_value[2])

        # 계산한적이 없을때는 상관없이 큐에 넣어주고, 계산한 적이 있고 가장 최근 수식이 'R'인 경우에는 left 계산을 하지 않도록 해준다 (무한 루프 방지 위해서)
        if not visited[left_rotated_value]:
            visited[left_rotated_value] = True
            if current_susik == '':
                queue.append((int(left_rotated_value), current_susik + 'L'))
            elif current_susik and current_susik[-1] != 'R':
                queue.append((int(left_rotated_value), current_susik + 'L'))

        # 무한루프 방지 해주기
        if not visited[right_rotated_value]:
            visited[right_rotated_value] = True
            if current_susik == '':
                queue.append((int(right_rotated_value),current_susik+'R'))
            elif current_susik and current_susik[-1] != 'L':
                queue.append((int(right_rotated_value),current_susik+'R'))

        # 값이 5000 미만일때만 큐에 2배 해서 넣어주기 가능하고 , 5000 이상일때는 1만으로 나눈 나머지를 넣어주어야 한다

        if current_value*2 < 5000:
            if not visited[current_value * 2]:
                queue.append((current_value*2, current_susik+'D'))
                visited[current_value * 2] = True
        else:
            if not visited[current_value*2 % 10000]:
                visited[current_value*2 % 10000] = True
                queue.append((current_value*2 % 10000, current_susik+'D'))

        # 1을 뺀 값이 0 이상일때는 큐에 넣어주기 가능하고, 0 미만일때는 9999로 넣어주어야한다
        if not visited[current_value-1]:
            visited[current_value -1 ] = True
            if current_value-1 >= 0:
                queue.append((current_value-1, current_susik+'S'))
            else:
                queue.append((9999, current_susik+'S'))

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, (input().split()))
    bfs(A)


