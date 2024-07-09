import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = [input() for _ in range(5)]
    # 가장 긴 단어 찾기
    max_word = 0
    for word in words:
        max_word = max(len(word), max_word)
    i = 0
    # 단어에 비어있는 부분 0으로 채우기
    while True:
        if i == 5:
            break
        if max_word > len(words[i]):
            words[i]+= '@'
            continue
        if max_word == len(words[i]):
            i += 1
            continue
    word = ''

    # @ 제외하고 세로읽기 하기
    for i in range(max_word):
        for j in range(5):
            if words[j][i] != '@':
                word += words[j][i]
    print(f'#{tc}', word)

