import sys
sys.stdin = open('input.txt')

def make2(x):
    # 10진수로 만들고
    if x not in 'ABCDEF':
        num = (int(x))
    else:
        num = ord(x) - ord('A')+10
    # 2진수로 만들기
    # print()
    # print(num)
    output = ''
    for j in range(3, -1, -1):
        if num&(1<<j):
            output += '1'
        else:
            output += '0'
    print(output, end='')


T = int(input())
for tc in range(1,T+1):
    n, n_16 = input().split()
    print(f'#{tc} ', end = '')
    for i in range(int(n)):
        make2(n_16[i])
    print()
