"""
두개의 문자열을 순차적으로 각각 패턴과 타겟으로 받아서

타겟에 패턴이 몇개 있는지를 확인하는 문제
"""


def BruteForce(pattern, target):
    # 타겟의 갯수와, 패턴의 갯수
    N = len(target)
    M = len(pattern)
    # 타겟의 인덱스
    i = 0
    # 패턴의 갯수
    j = 0
    # 일치하는 갯수
    cnt = 0
    # 각 인덱스가 각 범위 안에 있을때
    while j < M and i < N:
        # 만약 타겟과 패턴이 다르다면,
        if target[i] != pattern[j]:
            # 단어와 요소의 인덱스를 초기화
            i = i - j
            j = -1
        # 다음 인덱스로 넘어간다
        i = i + 1
        j = j + 1
        # j가 패턴의 길이와 동일해졌다면
        if j == M:
            # j를 초기화 후
            j = 0
            # 카운트를 하나 올려주고
            cnt += 1
    # 카운트를 반환한다
    return cnt


for tc in range(1, 11):
    n = int(input())
    word1 = input()
    word2 = input()
    print(f'#{tc}', BruteForce(word1, word2))