def get_moo(N):
    length = 3
    k = 0

    while length < N:
        k += 1
        length = 2*length+(k+3)

    while k >= 0:
        prev_length = (length - (k + 3)) // 2

        if N <= prev_length:
            k -= 1
            length = prev_length
        elif N > prev_length + (k+3):
            N -= (prev_length + (k+3))
            k -= 1
            length = prev_length
        else:
            if N == prev_length + 1:
                return 'm'
            else:
                return 'o'
    pass
N = int(input())
print(get_moo(N))
