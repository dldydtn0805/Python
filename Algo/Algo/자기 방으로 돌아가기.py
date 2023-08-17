import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    cross = []
    hallway = [0]*200
    i = 0
    cnt = 0
    while True:
        # i번째 학생과 j번째 학생들 비교
        a,b = arr[i]
        for j in range(i, n):
        # flag = 겹친다
            flag = 0
            for k in range(2):
                if a < arr[j][k] < b:
                    visited[i][j] = 1
                    flag = 'on'
        i += 1
        if i == n:
            break
    result = []
    for i in range(n):
        result.append(sum(visited[i]))
    # while cross:
    #     cnt += 1
    #     x = cross.pop()
    #     while x in cross:
    #         cross.remove(x)
    # print(f'#{tc}', cnt+1)
    # cnt = 0
    # print(result)
    # for i in result:
    #     if result[i]:
    #         print(cnt)
    # print(cnt)
    max_v = 0
    for i in range(n):
        for j in result:
            if j > max_v:
                max_v = max(j, max_v)
    print(f'#{tc}', max_v+1)


