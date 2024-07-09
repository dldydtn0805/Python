import sys
arr = bytearray(2**22)
number = ""
while True :
    input = sys.stdin.read(1)
    if input.isnumeric() :
        number += input
    else :
        division = int(number) // 8
        remainder = int(number) % 8
        if not arr[division] & (1 << remainder) :
            print(int(number), end=' ')
            arr[division] |= 1 << remainder
        number = ""
        if input != " " :
            break
