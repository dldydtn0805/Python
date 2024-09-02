import sys, math
input = sys.stdin.readline

def get_pichulia_numbers(X):
    disliked = []
    num = 11
    while num <= X:
        disliked.append(num)
        num = num*10+1

    disliked_cnt = 0
    L = len(disliked)

    for i in range(1, 1<<L):
        lcm = 1
        bits = bin(i).count('1')
        for j in range(L):
            if i & (1 << j):
                lcm = math.lcm(lcm, disliked[j])
                if lcm > X:
                    break
        if lcm > X:
            continue
        if bits % 2 == 1:
            disliked_cnt += N // lcm
        else:
            disliked_cnt -= N // lcm

    return disliked_cnt

N = int(input())
print(get_pichulia_numbers(N))
