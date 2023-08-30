import sys
sys.stdin = open('input.txt')

# 순열 만들어주는 함수
def f(i, x, k):
    # 승리 여부 변수
    global run1, tri, flag
    if i == k:  # 순열 완성 K 개를 모두 고른 경우

        if p[0] != '!@#$' and p[1] != '!@#$' and p[2] != '!@#$':

            if p[0] == p[1] and p[1] == p[2] and p[0] == p[2]:
                flag = 1
            elif p[0] == p[1] + 1 and p[1] == p[2] + 1:
                flag = 1
        return

    else:  # p[i]에 들어갈 숫자를 결정
        for j in range(k):
            if used[j] == 0:  # 아직 사용 되기 전이면
                p[i] = x[j]
                used[j] = 1
                f(i + 1, x, k)
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = 12
    card = [i for i in range(N)]
    used = [0] * N  # 이미 사용한 카드인지 표시
    # 절대 없을 값으로 초기화 6자리를 해주고
    p = ['!@#$'] * (6)
    # 각각 카드 담아주는데
    a = []
    b = []
    run1 = 0
    tri = 0
    flag = 0
    # 1개부터 6개까지 순차적으로 담아주면서 순열 함수 돌리면서 플래그까지 확인
    for i in range(0, N - 1, 2):
        a.append(arr[i])
        b.append(arr[i + 1])
        x = f(0, a, len(a))
        # 만약에 플래그가 켜졌으면 a가 승리이므로
        if flag:
            print(f'#{tc}', 1)
            break
        y = f(0, b, len(b))
        # " B가 승리이므로
        if flag:
            print(f'#{tc}', 2)
            break
    else:
        print(f'#{tc}', 0)