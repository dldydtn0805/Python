import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    number = int(input())
    # 숫자의 10으로 나눈 나머지를 인덱스로한 카운팅 정렬을 구성한다
    c = [0] * 12
    for i in range(6):
        c[number % 10] += 1
        # 숫자의 10으로 나눈 몫을 다시 숫자에 갱신
        number //= 10

    i = 0
    runn = 0
    tri = 0

    while i < 10:
        # 카운팅 정렬 값이 3일때는 triplet 이므로, tri += 1
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
        # 값이 6일 수 있기 때문에 한번 더 해준다
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
        # 카운팅 정렬 값이 연속해서 1이상이 3번 오면 run 이므로, run += 1
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            runn += 1
        # 값이 2이상일 수 있기 때문에 한번 더 해준다
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            runn += 1
        # 다음번 차례로 가기
        i += 1
    # Baby gin 조건에따라 결과를 출력하기
    if runn == 1 and tri == 1:
        print(f'#{tc}', 1)
    elif tri == 2:
        print(f'#{tc}', 1)
    elif runn == 2:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)