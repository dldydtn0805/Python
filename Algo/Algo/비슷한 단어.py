"""
https://www.acmicpc.net/problem/2607
"""

import sys
sys.stdin = open('input.txt')

n = int(input())
words = [list(input()) for _ in range(n)]

main11 = words[0]
word = words[1:]
result = 0
for w in word:
    # 기준단어
    main = main11[:]
    # 기준단어와 비교단어 길이가 1 차이날 경우
    if abs(len(main)-len(w)) == 1:
        # 비교 단어가 더 길때
        if len(w) > len(main):
            for element in main:
                if element in w:
                    w.remove(element)
            # 구성 요소가 차이가 1개 날때 result += 1
            if len(w) == 1:
                result += 1
        # 기준 단어가 더 길때
        elif len(main) > len(w):
            for element in w:
                if element in main:
                    main.remove(element)
            # 구성 요소가 차이가 1개 날때 result += 1
            if len(main) == 1:
                result += 1

    # 둘의 길이가 같을때
    elif len(w) == len(main):
        # 구성 요소가 같을때 result += 1
        if set(w) == set(main):
            result += 1
        # 구성 요소가 다를때
        else:
            for element in w:
                if element in main:
                    main.remove(element)
            # 구성요소 1개가 차이날때 result += 1
            if len(main) == 1:
                result += 1
print(result)