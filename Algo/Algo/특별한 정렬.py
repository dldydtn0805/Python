import sys
sys.stdin = open('input.txt')

def min_v(N):
    minidx = 0
    for i in range(len(N)):
        if N[minidx] > N[i]:
            minidx = i
        N[minidx], N[i] = N[i], N[minidx]
    return N[0], N[1:]


def max_v(N):
    maxidx = 0
    for i in range(len(N)):
        if N[maxidx] < N[i]:
            maxidx = i
        N[maxidx], N[i] = N[i], N[maxidx]
    return N[0], N[1:]

T= int(input())
for tc in range(1,T+1):
    N = list(map(int, input().split()))
    count = 0
    c = [0]*len(N)
    while True:
        if count % 2 == 0:
            N = max_v(N)[1]
            c[count] = max_v(N)[0]
        elif count % 2 == 1:
            N = min_v(N)[1]
            c[count] = max_v(N)[0]
        if count == len(N):
            break
        count += 1
    print(c)

