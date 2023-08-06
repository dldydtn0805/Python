"""
코딩반 학생들에게 이진 탐색을 연습할 수 있는 게임을 시키기로 했다
짝을 이룬 A,B 두사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면,
이진탐색 만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임이다

책의 전체 쪽수와 두사람이 찾을 쪽 번호가 주어졌을때 이진탐색에서 이긴 사람이 누구인지 알아내 출력하시오
비긴 경우는 0을 출력한다

입력

책의 전체 쪽수 P, 쪽번호 각각 Pb, Pb가 차례로 주어진다


출력

A, B, 0 중 하나를 출력한다
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    P, Pa, Pb = map(int, input().split())
    # cnt_a, b 는 각각 이진 탐색 횟수
    cnt_a = 0
    cnt_b = 0
    # A 페이지 이진 탐색 시작
    # 이진 탐색에서 사용할 최솟값, 최댓값 설정
    min_P = 1
    max_P = P
    while True:
        mi = int((min_P+max_P)/2)
        cnt_a += 1
        if Pa == mi:
            break
        if Pa > mi:
            min_P = mi
        elif Pa < mi:
            max_P = mi
    # print(cnt_a)

 # B 페이지 이진 탐색 시작
 # 이진 탐색에서 사용할 최솟값, 최댓값 설정
    min_P = 1
    max_P = P
    while True:
        mi = int((min_P+max_P)/2)
        cnt_b += 1
        if Pb == mi:
            break
        if Pb > mi:
            min_P = mi
        elif Pb < mi:
            max_P = mi
    # print(cnt_b)
    # A가 더 카운트 횟수가 많다면, B가 이긴다
    if cnt_a > cnt_b:
        print(f'#{tc}', 'B')

    # B가 더 카운트 횟수가 많다면, A가 이긴다
    elif cnt_a < cnt_b:
        print(f'#{tc}','A')

    # 같다면, 비긴다
    elif cnt_a == cnt_b:
        print(f'#{tc}',0)
