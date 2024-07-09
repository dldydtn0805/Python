import sys
N = int(input())
M = int(input())
channel = 100
# 고장난 채널이 없을 수 있으므로 try except로 구분해준다
try:
    broken_buttons = set(input().split())
except:
    broken_buttons = set()
# 1. 처음 시작하는 채널인 100에서 -- 추적
def hundred_minus_count():
    start = 100
    hundred_minus_cnt = 0
    while start > N:
        start -= 1
        hundred_minus_cnt += 1
    return hundred_minus_cnt
# 2. 처음 시작 채널 100에서 ++ 추적
def hundred_plus_count():
    start = 100
    hundred_plus_cnt = 0
    while start < N:
        start += 1
        hundred_plus_cnt += 1
    return hundred_plus_cnt
# 3. 최종 결과 N에서 ++ 역추적
def n_plus_count():
    n = N
    n_plus_cnt = 0
    while len(set(str(n)) - broken_buttons) != len(set(str(n))):
        n += 1
        n_plus_cnt += 1
        if n_plus_cnt > 500000:
            return 1e9
    return n_plus_cnt + len(str(n))

# 4. 최종 결과에서 -- 역추적
def n_minus_count():
    n = N
    n_minus_cnt = 0
    while len(set(str(n)) - broken_buttons) != len(set(str(n))):
        n -= 1
        n_minus_cnt += 1
        if n_minus_cnt > 500000:
            return 1e9
    return n_minus_cnt + len(str(n))

# N이 100보다 클때는 2번의 경우를 제외하고 1, 3, 4의 결과중 최솟값을 출력
if N > 100:
    print(min(hundred_plus_count(),n_minus_count(), n_plus_count()))
# N이 100보다 작을때는 2, 3, 4의 결과 중 최솟값을 출력
elif N < 100:
    print(min(hundred_minus_count(), n_minus_count(), n_plus_count()))
# N이 100일때는 처음 채널과 같으므로 변경할 필요가 없다
else:
    print(0)