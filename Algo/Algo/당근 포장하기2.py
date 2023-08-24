import sys
sys.stdin = open('input.txt')

# 대 중 소 상자에 나누어 담음
# 같은 크기의 당근은 같은 상자
# 비어있는 상자가 있으면 안됨
# 한 상자에 n//2개를 초과하는 당근이 있으면 안됨
# 각 상자에 든 당근의 개수 차이가 최소가 되야함

def carrycarrot():
    for k, v in carrot_dict.items():
        if len(value):
            pass


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

    print(carrot)

    carrot_dict = {}
    for i in carrot:
        cnt_carrot = carrot.count(i)
        carrot_dict.setdefault(i, cnt_carrot)

    value = []

    for k, v in carrot_dict.items():
        value.append((v, k))

    print(value)