import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    # 화덕 크기 n, 피자 개수 m
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    # 피자 인덱스
    index = [i+1 for i in range(m)]
    # 인덱스용 오븐
    num= []
    # 오븐
    oven = []
    # 피자 다 넣기
    while pizza:
        # 치즈 0이 아니면
        if 0 not in oven:
            # 오븐에 피자 넣기
            while len(oven) < n:
                x = pizza.pop(0)
                y = index.pop(0)
                oven.append(x)
                num.append(y)
            # 피자 굽기
            oven.append(oven.pop(0)//2)
            num.append(num.pop(0)) # 인덱스
        else:
            # 치즈가 0이라면 꺼내기
            oven.pop()
            num.pop()
            # 새 피자 넣기
            x = pizza.pop(0)
            y = index.pop(0)
            oven.append(x)
            num.append(y)

    # 오븐에 피자가 다 들어갔다면
    while True:
        # 이제는 피자를 넣어주는 과정을 빼고 계속 굽기
        if 0 not in oven:
            oven.append(oven.pop(0)//2)
            num.append(num.pop(0))
        else:
            oven.pop()
            num.pop()
        # 피자가 하나만 남았다면,
        if len(oven) == 1:
            break
    print(f'#{tc}', num.pop())