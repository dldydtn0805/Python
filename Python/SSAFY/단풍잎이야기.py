import sys
# sys.stdin = open('input.txt')

# 조합을 구하는 함수, cur로 범위 인덱스 조절하는게 핵심!
def make_star(cnt, cur):
    global max_v
    now = 0
    # 스킬셋 구성을 끝냈을때, 클리어 가능한 퀘스트 개수를 체크해주고 max_v 값에 저장해준다
    if cnt == n:
        for q in quest:
            flag = 1
            for w in q:
                if w not in skill:
                    flag = 0
            if flag:
                now += 1
        max_v = max(now, max_v)
        return
    # 스킬셋 구성하는 재귀 구문!
    for i in range(cur+1, 2*n+1):
        skill[cnt] = i
        make_star(cnt+1, i)

n, m, k = map(int, input().split())
quest = [list(map(int, input().split())) for _ in range(m)]
total = [i for i in range(1,2*n+1)]
skill = [0]*n
max_v = 0
make_star(0,0)
print(max_v)