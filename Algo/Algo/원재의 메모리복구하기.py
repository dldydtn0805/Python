import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    memory = list(map(int,input()))
    cnt = 0
    sangtae = 0
    # 맨 앞에서부터 만들어가는 느낌
    for i in range(len(memory)):
        if sangtae == 0:
            if memory[i] == 1:
                sangtae = 1
                cnt += 1
            elif memory[i] == 0:
                continue
        elif sangtae == 1:
            if memory[i] == 1:
                continue
            elif memory[i] == 0:
                sangtae = 0
                cnt += 1
    print(f'#{tc}', cnt)
