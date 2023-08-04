import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 단어 퍼즐의 변의 길이 N, 단어의 길이 K
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 단어 들어갈 수 있는 횟수
    total = 0
    for i in range(N):
        # 연속하는 빈칸 갯수
        max_count = 0
        # 칸 연속하는 단어의 개수
        count = 1
        for j in range(N):
            # 범위가 정상적이라면,
            if 0 <= j+1 < N:
                # 연속하는 빈칸 갯수 입력
                if arr[i][j] == 1 and arr[i][j+1] == 1:
                    count += 1
                    max_count = max(count, max_count)
        # 연속하는 빈칸의 개수가 K라면
        if max_count == K:
            # 단어 들어갈 수 있는 횟수 추가
            total += 1
        print(total)





