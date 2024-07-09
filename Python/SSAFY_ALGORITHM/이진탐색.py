"""
def binarysearch(a, N, key):
    start = 0
    end = N-1
    while start <= end: # 탐색 구간이 존재
        middle = (start + end) // 2
        if a[middle] == key: #검색 성공
            return True
        elif a[middle] > key: # 중간값이 키보다 크다면
            end = middle-1 # 끝값을 중간값 - 1로 수정
        elif a[middle] < key: # 중간 값이  키보다 작다면
            start = middle+1 # 시작값을 중간값 + 1로 수정
    return False # 검색 실패
이진탐색
"""

"""
def BruteForce(t, p):
    i = 0
    j = 0
    while i < N and j < M:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == M:
        return i - M
    else:
        return -1
t = 'this is a book'
p = 'is'
N = len(t)
M = len(p)
print(BruteForce(t,p))

브루트 포스
"""

"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = list(input())
    stack = []
    now = 1
    case = {'}':'{', ')':'('}
    for word in words:
        if word in ['{', '(']:
            stack.append(word)
        if word in ['}', ')']:
            if stack:
                if case[word] != stack.pop():
                    now = 0
            else:
                now = 0
    if stack:
        now = 0
    print(now)

괄호검사

"""

"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = list(input())
    stack = []
    try:
        for word in words:
            if word not in '{}()':
                stack.append(int(word))
            elif word == '(':
                stack.append(word)
            elif word == '{':
                stack.append(word)
            elif word == ')':
                while True:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                    if stack[-2] == '(':
                        stack.pop(-2)
                        break

            elif word == '}':
                while True:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                    if stack[-2] == '{':
                        stack.pop(-2)
                        break
        if len(stack) == 1:
            print(f'#{tc}', stack[-1])
        else:
            print(f'#{tc}', -1)
    except:
        print(f'#{tc}', -1)
괄호 덧셈
"""

