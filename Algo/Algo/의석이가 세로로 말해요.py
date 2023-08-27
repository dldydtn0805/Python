import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    words = [list(input()) for _ in range(5)]
    # 가장 긴 행의 길이
    max_len = 0
    for i in range(5):
        max_len = max(max_len, len(words[i]))
    for i in range(5):
        while len(words[i]) < max_len:
            words[i].append('!@#$')
    print(f'#{tc}', end=' ')
    for i in range(max_len):
        for j in range(5):
            if not words[j][i] == '!@#$':
                print(words[j][i], end='')
    print()


