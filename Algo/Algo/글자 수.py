"""
두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우, str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

파이썬의 경우 딕셔너리를 이용할 수 있다.

"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    cnt = 0
    dic = {}
    for s in str1:
        dic[s] = 0
        max_cnt = 0
        for s2 in str2:
            if s == s2:
                dic[s] += 1
    max_v = 0
    for k, v in dic.items():
        max_v =