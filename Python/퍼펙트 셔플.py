import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    card = list(input().split())
    deck = []
    # 카드 갯수가 홀수일때
    if n % 2:
        for i in range(n//2+1):
            deck.append(card[i])
            # 범위 넘어가지 않도록
            if n // 2 + i+1<n:
                deck.append(card[n // 2 + i+1])
    else:
        for i in range(n//2):
            deck.append(card[i])
            deck.append(card[n//2+i])
    print(f'#{tc}', *deck)