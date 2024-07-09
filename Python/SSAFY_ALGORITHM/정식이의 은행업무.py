import sys
sys.stdin = open('input.txt')
T = int(input())
def check2(cnt,x):
    if cnt == 1:
        s = 0
        cnt = 0
        for j in range(len(x)-1, -1, -1):
            if x[j]:
                s += 2**cnt
            cnt += 1
        result1.append(s)
        return
    for i in range(1, len(x)):
        if x[i] == 0:
            x[i] = 1
        else:
            x[i] = 0
        check2(cnt+1, x)
        if x[i] == 0:
            x[i] = 1
        else:
            x[i] = 0

def check3(cnt, x):
    global result
    if cnt == 1:
        s = 0
        cnt = 0
        for j in range(len(x) - 1, -1, -1):
            if x[j]:
                s += 3 ** cnt * x[j]
            cnt += 1
        result2.append(s)
        return
    temp = [0,1,2]
    for i in range(len(x)):
        for t in range(len(temp)):
            if temp[t] != x[i]:
                aa = x[i]
                x[i] = temp[t]
                check3(cnt+1, x)
                x[i] = aa

for tc in range(1, T+1):
    a = list(map(int, input()))
    b = list(map(int, input()))
    result1 = []
    result2 = []
    check2(0,a)
    check3(0,b)
    # print(result1)
    # print(result2)
    for i in result1:
        for j in result2:
            if i == j:
                print(f'#{tc}', i)
