import sys
input = sys.stdin.readline
# n= 물병 갯수, k= 한번에 옮길 수 있는 병, 각 물병에는 물이 1리터씩 들어있음
n, k = map(int, input().split())
# 물병 구입 횟수
cnt = 0
# 물병 총 갯수를 반으로 나눈 값이 k 이상일때만 실행
while n//2 > k:
    n //= 2
    if n%2:
        cnt += 1
        n += 1
print(cnt)