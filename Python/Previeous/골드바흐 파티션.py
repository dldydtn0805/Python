import sys
input = sys.stdin.readline

#소수 골라내기 (에라토스테네스의 체 활용)
#0 과 1은 소수가 아니므로 제외해주고 최대값인 100000001까지 소수 여부 판단하기위한 리스트 세팅
sosu = [0, 0] + [1]*999999

for i in range(2, 1000001):
    # 아직 소수인지 체크 안했다면
    if sosu[i]:
        # i 자기 자신을 제외한 2배 , 3배 , 4배 ..... 최대값인 10000001까지 소수가 아니므로 소수 체크 해제
        for j in range(i*2, 1000001, i):
            sosu[j] = 0

T = int(input())

#문제 풀이
for i in range(T):
    cnt = 0
    n = int(input())
    # 2부터 딱 n의 절반만 확인해서 중복으로 세지 않게 해준다
    for j in range(2, n//2+1):
        # j가 소수이고 n-j도 소수라면 골드바흐 파티션이므로 카운트 1 증가
        if sosu[j] and sosu[n-j]:
            cnt += 1
    print(cnt)