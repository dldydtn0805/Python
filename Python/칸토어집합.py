import sys
sys.stdin = open('input.txt')

def make_cantor(start, n):
    # n이 1이라면 다시 돌아와야 해
    if n == 1:
        return
    # 가운데 부분을 빈 문자열로 교체
    for i in range(start + n//3, start+ (n//3)*2):
        strings[i] = ' '
    # 왼쪽 부분만 다시 한번 분할 정복
    make_cantor(start, n//3)
    # 오른쪽 부분만 다시 한번 분할 정복
    make_cantor(start + n//3*2, n//3)

while True:
    try:
        number = int(input())
        strings = ['-']*3**number
        make_cantor(0, len(strings))
        print(''.join(strings))
    except:
        exit()