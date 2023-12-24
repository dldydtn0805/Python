def BruteForce(pattern, target):
    N = len(target)
    M = len(pattern)
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    # 각 인덱스가 타겟과 패턴의 길이보다 작을 동안 반복
    cnt = 0
    while j < M and i < N:
        # 패턴과 다른 곳을 발견 했을때,
        if target[i] != pattern[j]:
            # j 만큼 온 상태에서 틀린 곳을 발견 함
            # 지금 위치 - j + 1 다음 위치가 된다
            i = i - j
            # -1로 j를 초기화 하는 이유, 패턴과 일치하는 문자열이 발견 됐을때, j+1을 해주기 때문
            j = -1
        # 패턴과 같을 때
        i = i + 1
        j = j + 1
        if j == M:
            return i-M
        #패턴 인덱스 j가 패턴의 길이만큼 탐색 된 것 == 탐색 성공
    return -1 # 검색이 안될때

for tc in range(1, 11):
    n = int(input())
    word1 = input()
    word2 = input()
    print(BruteForce(word1, word2))