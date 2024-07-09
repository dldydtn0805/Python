import sys
input = sys.stdin.readline
# n= 물병 갯수, k= 한번에 옮길 수 있는 병, 각 물병에는 물이 1리터씩 들어있음
n, k = map(int, input().split())
cnt = 0
# 2진수로 만든 상태에서 1의 갯수가 k보다 넘지 않은 선에서 아래를 반복한다
while bin(n).count('1') > k:
    n += 1
    cnt += 1
print(cnt)