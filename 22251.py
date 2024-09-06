import sys
input = sys.stdin.readline

def create_dict(x, y):
    X = make_digit[x]
    Y = make_digit[y]
    for i in range(len(X)):
        if X[i] != Y[i]:
            cnt[x][y] += 1
            cnt[y][x] += 1
N, K, P, X = map(int, input().split())
cnt = [[0 for _ in range(10)] for _ in range(10)]
make_digit = {
    0 : '1110111',
    1 : '0010010',
    2 : '1011101',
    3 : '1011011',
    4 : '0111010',
    5 : '1101011',
    6 : '1101111',
    7 : '1010010',
    8 : '1111111',
    9 : '1111011'
}

for i in range(9):
    for j in range(i, 10):
        create_dict(i,j)



start = str(X)
while len(start) < K:
    start = '0' + start
ans = 0

for i in range(1, N+1):
    tmp = str(i)

    while len(tmp) < K:
        tmp = '0' + tmp
    cal = 0
    for i in range(len(tmp)):
        cal += cnt[int(tmp[i])][int(start[i])]
    if 1 <= cal <= P:
        ans += 1

print(ans)
