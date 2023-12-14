import sys
import math
# sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k, c, r = map(int, input().rstrip().split())
# 각 스킬 기본적으로 얻을수있는 별가루
bases = list(map(int, input().rstrip().split()))
# 각 스킬의 가중치
ss = list(map(int, input().rstrip().split()))
# 각 스킬 사용시 피로도
ps = list(map(int, input().rstrip().split()))
ans = 0
skills = [0 for _ in range(k)]
# 콤보
combos = 0
# 피로도
tired = 0

for _ in range(n):
    x = int(input())
    if x == 0:
        # 피로도는 0보다 작을수없음
        if tired < r:
            tired = 0
        else :
            tired -= r
        # 콤보 초기화
        combos = 0
        pass
    # x - 1로 하는 이유는 0일때 휴식이기 때문이다
    else:
        # 수식에따라 총 별가루 개수 넣어주기
        ans += ((bases[x-1] * ( 1 + ((combos * c) / 100) ) *(1 + ((skills[x-1]*ss[x-1])/100))))
        # 스킬 숙련도 올려주기
        skills[x-1] += 1
        # 콤보 올리기
        combos += 1
        # 피로도 늘리기
        tired += ps[x-1]
        # 만약 피로도가 100보다 커지면
        if tired > 100:
            print(-1)
            exit()
        ans = int(ans)
print((ans))