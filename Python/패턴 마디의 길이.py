import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    madi = input()
    check = []
    result = []
    for i in range(len(madi)):
        # 앞에서부터 계속 넣어주다가
        check.append(madi[i])
        if check[0] == madi[i]:
            if len(check) > 2:
                if check[1] == madi[i+1]:
                    break
    print(f'#{tc}', len(check[:-1]))