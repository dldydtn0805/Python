import sys
sys.stdin = open('input.txt')

n = int(input())
words = [input() for _ in range(n)]
# 기준 단어
main = words[0]
ans = 0
for word in words[1:]:
    # 퇴장 여부(0이 되면 퇴장)
    now = 1
    # 경고
    cnt = 0
    for element in main:
        # 기준단어와 다른 낱말이 1번 발견되면 경고 더 발견되면 퇴장
        temp = 0
        if element not in word:
            temp += 1
            cnt += 1
            if temp > 1:
                now = 0
    for element in word:
        # 기준단어와 다른 낱말이 1번 발견되면 경고 더 발견되면 퇴장
        temp = 0
        if element not in main:
            temp += 1
            cnt += 1
            if temp > 1:
                now = 0
    # 두 단어의 차이가 1보다 크다면 퇴장
    if abs(len(main) - len(word)) > 1:
        now = 0
    # 두 단어의 차이가 1이라면 경고
    if abs(len(main) - len(word)) == 1:
        cnt += 1
    # 경고가 1번 이하이고 퇴장 당하지 않았다면 정답 체크
    if cnt < 2 and now == 1:
        ans += 1
print(ans)