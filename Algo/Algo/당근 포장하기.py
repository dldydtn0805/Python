import sys
sys.stdin = open('input.txt')

# 대 중 소 상자에 나누어 담음
# 같은 크기의 당근은 같은 상자
# 비어있는 상자가 있으면 안됨
# 한 상자에 n//2개를 초과하는 당근이 있으면 안됨
# 각 상자에 든 당근의 개수 차이가 최소가 되야함


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    carrot = list(map(int, input().split()))
    s = []
    m = []
    l = []

    carrot.sort()
    # 세개의 상자에 바로 넣어주는건 힘드므로 정렬을 먼저 하자
    # 어차피 같은 상자에 같은 크기의 당근을 넣어야하므로 먼저 넣어주자

    carrot_dict = {}
    for i in carrot:
        cnt_carrot = carrot.count(i)
        carrot_dict.setdefault(i, cnt_carrot)

    value = []

    for k, v in carrot_dict.items():
        value.append((v, k))

    value.sort(reverse=True)

    # print(value)
    # # 개수 많은 순서대로 상자에 넣어주기

    # 당근 길이가 3 이상이고 3번째로 많은 개수가 4번째로 많은 개수보다 많을때?
    if len(value) > 3 and value[2][0] > value[3][0] and value:
        for _ in range(value[0][0]):
            l.append(value[0][1])
        value.pop(0)
        for _ in range(value[0][0]):
            m.append(value[0][1])
        value.pop(0)
        for _ in range(value[0][0]):
            s.append(value[0][1])
        value.pop(0)

    # 2번째로 많은 개수가 3번째로 많은 개수보다 많을떄
    elif value[1][0] > value[2][0] and value:
        for _ in range(value[0][0]):
            m.append(value[0][1])
        value.pop(0)
        for _ in range(value[0][0]):
            s.append(value[0][1])
        value.pop(0)
    # 1번째로 많은 개수가 2번째로 많은 개수보다 많을때
    elif value[0][0] > value[1][0] and value:
        for _ in range(value[0][0]):
            s.append(value[0][1])
        value.pop(0)

    # 갯수 많은 순으로 담았음
    x = ((len(value)+1)//3)
    while len(l) < x and value:
        l.append(value[0][1])
        value.pop(0)

    while len(m) < x and value:
        m.append(value[0][1])
        value.pop(0)

    while len(s) < x and value:
        s.append(value[0][1])
        value.pop(0)

    print(l)
    print(m)
    print(s)

    if s and m and l and not value:
        if len(s) <= n//2 and len(m) <= n//2 and len(l) <= n//2:
            print(f'#{tc}', abs(len(s)-len(m)))
        else:
            print(f'#{tc}', -1)
    else:
        print(f'#{tc}', -1)