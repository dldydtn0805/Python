import sys
# sys.stdin = open('input.txt')
import heapq
input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))
cnt = 0

while len(cards)>2:

    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    heapq.heappush(cards, x+y)
    cnt += (x+y)

if n == 1:
    print(0)

else:
    print(cnt+sum(cards))