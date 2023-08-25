import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    cards = input()
    deck = []
    flag = 1
    for i in range(0, len(cards)-1, 3):
        if cards[i:i+3] not in deck:
            deck.append(cards[i:i+3])
        else:
            flag = 0

    sums =0
    sumd =0
    sumh =0
    sumc =0
    for i in deck:
        if i[0] == 'S':
            sums += 1
        if i[0] == 'D':
            sumd += 1
        if i[0] == 'H':
            sumh += 1
        if i[0] == 'C':
            sumc += 1
    if flag:
        print(f'#{tc}', 13-sums, 13-sumd, 13-sumh, 13-sumc)
    else:
        print(f'#{tc}', "ERROR")