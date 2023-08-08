"""
"기러기", "토마토", "스위스"와 같이 똑바로 읽어도 거꾸로 읽어도 똑같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수를 구하라.
[제약 사항]

각 칸의 들어가는 글자는 'A', 'B', 'C' 중 하나이다.

ABA도 회문이며, ABBA도 회문이다. A 또한 길이 1짜리 회문이다.

가로 또는 세로로 이어진 회문의 개수만 센다.

아래 그림에서 노란색 경로를 따라가면 길이 7짜리 회문이 되지만 직선이 아니기 때문에 인정되지 않는다.

[입력]

총 10개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가 주어지며, 다음 줄에 8x8 크기의 글자판이 주어진다.

[출력]

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 찾은 회문의 개수를 출력한다.

"""
import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    new_arr = []
    cnt = 0

    #가로 배열 탐색
    for i in range(8):
        # 가로 전체 8에서 단어 길이 n을 빼준다
        for j in range(8-n+1):
            word = ''
            # 기준 인덱스에서 가로로 1,2,3,..,n번 까지 단어를 합쳐준다
            for k in range(n):
                word += arr[i][j+k]
            # 역단어 만들고 비교해서 같으면 카운트 1 증가
            re_word = word[::-1]
            if word == re_word:
                cnt += 1

    # 세로 배열 탐색
    for i in range(8):
        # 세로 전체 8에서 단어 길이 n을 빼준다
        for j in range(8-n+1):
            word = ''
            # 기준 인덱스에서 세로로 1,2,3,...,n번 까지 단어를 합쳐준다
            for k in range(n):
                word += arr[j+k][i]
            # 역단어 비교 같으면 1 증가
            re_word = word[::-1]
            if word == re_word:
                cnt += 1
    print(f'#{tc}', cnt)


