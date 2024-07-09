import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
t = list(map(int, input().split()))
#
max_card = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            card = 0
            if i != j and i != k and j != k:
                card += t[i] + t[j] + t[k]
            if card <= M:
                max_card = max(card, max_card)
print(max_card)