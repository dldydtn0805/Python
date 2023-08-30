import sys
sys.stdin = open('input.txt')
# 순열을 만드는 재귀 함수
def f(i, N):
    flag = 1
    # 순열이 완성됐을때 전체 합을 0으로 두고
    # 순열을 순회하면서 전체 합에 더해준다
    # 단 시작과 처음이 0이어야 하므로 p[0]와 p[-1]은 0이다
    if i == N:
        total = 0
        if p[0] == 0 and p[-1] == 0:
            for i in range(len(p)-1):
                # 나란히 순열을 순회하기 위해서 j = i+1로 설정한다
                j = i + 1
                total += arr[p[i]][p[j]]
            # 최종 값을 넣어준다
            result.append(total)
        return

    else: # used를 사용해서 순열을 하나하나 채워나가는 작업을 한다
        for j in range(N):
            if used[j] == 0: # 아직 사용 되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N 개의 숫자에서
    # 순열을 만들어줄 리스트에 0부터 N-1까지 담는다
    card = [i for i in range(N)]
    used = [0] * N # 이미 사용한 카드인지 표시
    # 순열의 끝을 0으로 만들어주기 위해 N+1로 설정함
    p = [0]*(N+1)
    arr = [list(map(int ,input().split())) for _ in range(N)]
    result = []
    f(0,N)
    print(f'#{tc}', min(result))
