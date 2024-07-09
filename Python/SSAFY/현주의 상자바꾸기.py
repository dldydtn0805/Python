"""

현주는 1번부터 N번까지 N개의 상자를 가지고있다

각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0으로 적혀있다

현주는 Q회 동안 일정한 범위의 연속한 상자를 동일한 숫자로 변경한다

i(1<=i<=Q)번째 작업에 대해 L번 상자부터 R번 상자까지의 값을 i로 변경

현주가 Q회 동안 위의 작업을 순서대로 한 다음 N개의 상자에 적혀있는 값들을 순서대로 출력하라

입력

각 케이스의 첫번째 줄에는 두 정수 N Q (1<= N,Q <=10^3)가 공백으로 주어진다
다음 Q개의 줄의 i번째 줄에는 Li, Ri (1<=Li <= Ri <= N)이 주어진다

출력

각 케이스 마다 Q개의 작업을 수행한 다음 1번부터 N번까지의 상자에 적혀있는 값들을 순서대로 출력 한다

"""

# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N개의 상자, Q번의 작업
    N, Q = map(int, input().split())
    arr = [0]*N
    # Q번의 작업을 반복
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            arr[j] = i+1
    print(f'#{tc}', *arr)

