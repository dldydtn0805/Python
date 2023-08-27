import sys
sys.stdin = open('input.txt')

# 대 중 소 상자에 나누어 담음
# 같은 크기의 당근은 같은 상자
# 비어있는 상자가 있으면 안됨
# 한 상자에 n//2개를 초과하는 당근이 있으면 안됨
# 각 상자에 든 당근의 개수 차이가 최소가 되야함

# 이상적인 각 상자의 당근 개수는 n//3으로 나눈 개수만큼 있는것

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    carrot = list(map(int, input().split()))
    wonbon = carrot[:]
    carrot = list(set(carrot))
    s = []
    m = []
    l = []
    carrot.sort()
    len_s = 0
    len_m = 0
    len_l = 0
    while carrot:
        a = carrot.pop(0)
        x = wonbon.count(a)
        if len(s) < n//2 and len(m) < n // 2 and len(l) < n//2:
            for _ in range(x):
                s.append(a)
        elif len(m) < n // 2 and len(l) < n//2 :
            for _ in range(x):
                m.append(a)
        elif len(l) < n//2:
            for _ in range(x):
                l.append(a)

    print(s)
    print(m)
    print(l)
        # # if len(carrot) >= 2*n//3:
        # #     if not s:
        # #         s.append(a)
        # #         continue
        # # elif n//3 <= len(carrot) < 2*n//3:
        # #     if not m:
        # #         m.append(a)
        # #         continue
        # if len(carrot) < n//3:
        #     if not l:
        #         l.append(a)
        #         continue
