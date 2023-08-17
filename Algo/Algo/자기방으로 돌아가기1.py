import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # 복도
    hallway = [0]*201
    for _ in range(n):
        a, b = map(int,input().split())
        # a가 더 크면 a가 시작점
        if a < b:
            start = (a+1)//2
            end = (b+1)//2
        else:
        # b가 더 크면 b가 시작점
            start = (b+1)//2
            end = (a+1)//2
        # 지나다니는 횟수 체크
        for i in range(start, end+1):
            hallway[i] += 1

    print(f'#{tc}', max(hallway))


