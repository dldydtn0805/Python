import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    password = [list(map(int, input())) for _ in range(n)]
    # print(password)
    for i in range(n):
        for j in range(m-1, -1, -1):
            if password[i][j]:
                row = i
                last = j
                break
    # 0 ~ 9 까지 암호 코드
    A = [0,0,0,1,1,0,1]
    B = [0,0,1,1,0,0,1]
    C = [0,0,1,0,0,1,1]
    D = [0,1,1,1,1,0,1]
    E = [0,1,0,0,0,1,1]
    F = [0,1,1,0,0,0,1]
    G = [0,1,0,1,1,1,1]
    H = [0,1,1,1,0,1,1]
    I = [0,1,1,0,1,1,1]
    J = [0,0,0,1,0,1,1]
    # 입력값에서 암호문 뽑아오기
    word = password[row][last-55:last+1]
    queue = []
    temp = []

    # 큐에 암호문 각각 담아서 비교하기
    for i in range(56):
        queue.append(word.pop(0))
        if len(queue) == 7:
            if queue == A:
                temp.append(0)
                queue.clear()
            if queue == B:
                temp.append(1)
                queue.clear()
            if queue == C:
                temp.append(2)
                queue.clear()
            if queue == D:
                temp.append(3)
                queue.clear()
            if queue == E:
                temp.append(4)
                queue.clear()
            if queue == F:
                temp.append(5)
                queue.clear()
            if queue == G:
                temp.append(6)
                queue.clear()
            if queue == H:
                temp.append(7)
                queue.clear()
            if queue == I:
                temp.append(8)
                queue.clear()
            if queue == J:
                temp.append(9)
                queue.clear()

    # 요구조건 확인하고 출력하기

    sum_v = 0
    result = 0
    for i in temp:
        result += i

    for i in range(8):
        if (i+1)%2:
            sum_v += 3*temp[i]
        else:
            sum_v += temp[i]
    if sum_v % 10:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', result)
