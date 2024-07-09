import sys
sys.stdin = open('input.txt')

def BruteForce(N, M, t):
    max_cards = 0
    for i in range(1<<N):
        cards = 0
        cnt = 0
        for j in range(N):
            if i & (1<<j):
                cards += t[j]
                cnt += 1
        if cards <= M and cnt == 3 :
            max_cards = max(cards, max_cards)

    return max_cards

N, M = map(int, input().split())
t = list(map(int, input().split()))

print(BruteForce(N,M,t))