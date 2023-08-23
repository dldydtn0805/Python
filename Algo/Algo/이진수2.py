import sys
sys.stdin = open('input.txt')

def make2(n):
    # 2의 지수
    cnt = -1
    # 2진수
    output = ''
    # n이 존재하는동안 2진수를 하나씩 올려가면서 빼줬을때
    # 0 이상이면 2진수에 1 추가하고 그 외에는 0 추가하기
    while n:
        if n-2**cnt >= 0:
            output += '1'
            n -= 2**cnt
        elif n-2**cnt < 0:
            output += '0'
        cnt -= 1
    return output

T = int(input())
for tc in range(1,T+1):
    n = float(input())
    result = make2(n)
    # 2진수 길이 12 이내여야 한다
    if len(result) <= 12:
        print(f'#{tc}', result)
    else:
        print(f'#{tc}','overflow')
