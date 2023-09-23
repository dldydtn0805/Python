"""
숫자 N은 다음과 같다

N = 2^a * 3^b * 5^c * 7^d * 11^e

a b c d e를 출력하라

N은 2 이상, 10,000,000 이하이다
"""
#
# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # temp = 나눗셈 할 목록 설정
    temp = [2,3,5,7,11]
    # arr = 대상 숫자를 위 목록으로 나눌 때 횟수를 기입할 대상
    arr = [0]*5
    i = 0
    # 같은 숫자를 반복적으로 나눠야하므로 while 선택
    while True:
        # 인수일때 (나눗셈의 나머지가 0일때)
        if N % temp[i] == 0:
            # 나눈 몫을 할당하고
            N //= temp[i]
            # 횟수 카운팅한다
            arr[i] += 1
        # 더이상 인수 아닐때
        if N % temp[i] != 0:
            # 다음 숫자로 패스
            i += 1
        if i == 5:
            break
    print(f'#{tc}', *arr)
