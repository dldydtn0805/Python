
n = list(input())
f = int(input())

n[-1], n[-2] = '0', '0'
start = int(''.join(n))
n[-1], n[-2] = '9', '9'
end = int(''.join(n))

for i in range(start, end+1):
    if i % f == 0:
        if i-start == 0:
            print('00')
        elif i-start < 10:
            print('0'+f'{i-start}')
        else:
            print(i-start)
        exit()