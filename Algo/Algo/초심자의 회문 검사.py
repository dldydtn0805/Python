"""
거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문이라 한다

회문이면 1을 출력 아니면 0을 출력하라

"""


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    n = len(word)
    check = 0
    # 단어를 순회하면서
    for i in range(n):
        # 첫글자와 끝글자, 두번째글자와 끝에서 두번째 글자, ... , 탐색
        if word[i] == word[n-i-1]:
            check = 1
        else:
            check = 0
    print(f'#{tc}', check)
