def tournament(i, j):
    # 시작점과 끝점이 같으면 시작점 반환
    if i == j:
        return i
    # a는 i에서 중간지점까지, b는 중간지점에서 j까지 계속해서 나누기
    a = tournament(i, (i+j)//2)
    b = tournament((i+j)//2+1, j)
    # 계속 나누다보면 최종 노드까지 가게되고 최종 노드에서 카드게임 진행
    return cardgame(a, b)

def cardgame(a, b):
    # 가위바위보
    if arr[a] == arr[b]:
        return a
    elif arr[a]-arr[b] == 1 or  arr[a]-arr[b] == -2:
        return a
    return b

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc}',tournament(0, n-1)+1)