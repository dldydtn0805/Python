import sys, math
input = sys.stdin.readline

def get_pichulia_numbers(X):
    disliked = []
    num = 11
    while num <= X:
        disliked.append(num)
        num = num*10+1

    disliked_cnt = 0

    for i in range(1, 1 << len(disliked)):
        lcm = 1
        bit_count = 0
        for j in range(len(disliked)):
            if i & (1 << j):
                lcm = math.lcm(lcm, disliked[j])
                bit_count += 1
                if lcm > X:
                    break
        if lcm > X:
            continue
        if bit_count % 2 == 1:
            disliked_cnt += X // lcm
        else:
            disliked_cnt -= X // lcm

    return disliked_cnt

N = int(input())
print(get_pichulia_numbers(N))
