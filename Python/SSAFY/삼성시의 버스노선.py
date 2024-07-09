import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    # 버스
    arr1 = [list(map(int, input(). split())) for _ in range(n)]
    p = int(input())
    # 정류장
    arr2 = [int(input()) for _ in range(p)]
    # 정류장에 지나가는 버스의 수를 기록할 리스트
    paper = [0]*p
    for i in range(n):
        for j in range(p):
            # 해당 정류장에 버스가 지나가면 기록
            if arr1[i][0] <= arr2[j] <= arr1[i][1]:
                paper[j] += 1
    print(f'#{tc}', *paper)

