import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    danzo = list(map(int, input().split()))
    # 두 수릅 곱한 값들을 danzos에 넣어준다
    danzos = []
    for i in range(len(danzo)):
        for j in range(len(danzo)):
            if i != j:
                    x = danzo[i]*danzo[j]
                    danzos.append(str(x))
    result = []
    # danzos를 순회하면서 단조 증가하는 수가 아닌 경우 break, 단조 증가하는 수인 경우 result에 넣어준다
    for danz in danzos:
        now = 1
        for j in range(len(danz)-1):
            if danz[j] > danz[j+1]:
                now = 0
                break
        if now:
            result.append(int(danz))
    if result:
        print(f'#{tc}', max(result))
    else:
        print(f'#{tc}', -1)