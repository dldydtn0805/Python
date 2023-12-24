import sys
sys.stdin = open('input.txt')

def ncr(n,r):
    global flag
    if r==0:
        trucktemp = tr[:]
        contemp = containers[:]
        trucktemp.sort()
        s = 0
        while contemp and trucktemp:
            if contemp[-1] < trucktemp[-1]:
                trucktemp.pop()
                s += contemp.pop()
                flag = 1
            else:
                contemp.pop()
        result.append(s)
    elif n<r: # 남은 원소보다 고를게 더 많은 원소를 선택해야하는 경우
        return
    else:
        tr[r-1] = trucks[n-1] # a[n-1] 조합에 포함시키는 경우
        ncr(n-1, r-1)
        ncr(n-1, r) # a[n-1]을 포함시키지 않는 경우

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    result = []
    containers = list(map(int, input().split()))
    containers.sort()
    trucks = list(map(int, input().split()))
    tr = [0] * n
    flag = 0
    if m > n:
        ncr(m,n)
    else:
        print(f'#{tc}', sum(containers[n-2:]))
    if result and flag:
        print(f'#{tc}', max(result))