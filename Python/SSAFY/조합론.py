'''
재원이는 한 도시의 시장임

도시를 나누는 강이 있는데 다리가 없어서 다리를 짓기로함

강 주변에서 다리를 짓기 적합한 곳을 사이트라고 한다 강의 서쪽에는 n개의 사이트 , 동쪽에는 m개의 사이트가 있음

서쪽의 사이트보다 동쪽의 사이트가 많음

서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 하는데 한 사이트에는 최대 한개의 다리만 연결될수 있음

재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 다리를 지으려고 함

다리끼리 겹쳐질수 없다고 할때 다리를 지을수있는 경우의수를 구하는 프로그램을 작성해라

'''

import sys, math
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    print(math.comb(n,m))
    # cnt = 0
    # for i in range(1<<m):
    #     temp = 0
    #     for j in range(m):
    #         if i & (1<<j):
    #            temp += 1
    #     if temp == n:
    #         cnt += 1
    # print(cnt)