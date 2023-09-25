import sys
from collections import deque
sys.stdin = open('input.txt')

'''
뮤탈은 1기, SCV는 N기

각 SCV의 남아있는 체력이 주어진다

뮤탈은 한번에 3개의 SCV 공격 가능하다

첫째로 공격받는 SCV는 체력 9를 잃는다

둘째로 공격받는 SCV는 체력 3을 잃는다

셋째로 공격받는 SCV는 체력 1을 잃는다

SCV 체력이 0 또는 그 이하가 되면 파괴된다 한 공격에서 같은 SCV 여러번 공격 안된다

모든 SCV 파괴하기위해 공격해야하는 횟수의 최솟값은?


'''
def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for _ in range(3):

n = int(input())

graph = list(map(int, input().split()))
