import sys
input = sys.stdin.readline
from copy import deepcopy

N, M = map(int, input().split())
K = int(input())
planet = [list(input().rstrip()) for _ in range(N)]
prefix = [[[0, 0, 0] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        case = 0
        if planet[i][j] == 'J':
            case = 0
        elif planet[i][j] == 'O':
            case = 1
        elif planet[i][j] == 'I':
            case = 2
        if i == 0 and j == 0:
            prefix[i][j][case] = 1
        elif i == 0:
            prefix[i][j] = deepcopy(prefix[i][j-1])
            prefix[i][j][case] += 1
        elif j == 0:
            prefix[i][j] = deepcopy(prefix[i-1][j])
            prefix[i][j][case] += 1
        else:
            if case == 0:
                prefix[i][j][0] = prefix[i][j-1][0] + prefix[i-1][j][0] - prefix[i-1][j-1][0] + 1
                prefix[i][j][1] = prefix[i][j-1][1] + prefix[i-1][j][1] - prefix[i-1][j-1][1]
                prefix[i][j][2] = prefix[i][j-1][2] + prefix[i-1][j][2] - prefix[i-1][j-1][2]
            elif case == 1:
                prefix[i][j][0] = prefix[i][j - 1][0] + prefix[i - 1][j][0] - prefix[i - 1][j - 1][0]
                prefix[i][j][1] = prefix[i][j - 1][1] + prefix[i - 1][j][1] - prefix[i - 1][j - 1][1] + 1
                prefix[i][j][2] = prefix[i][j - 1][2] + prefix[i - 1][j][2] - prefix[i - 1][j - 1][2]
            elif case == 2:
                prefix[i][j][0] = prefix[i][j - 1][0] + prefix[i - 1][j][0] - prefix[i - 1][j - 1][0]
                prefix[i][j][1] = prefix[i][j - 1][1] + prefix[i - 1][j][1] - prefix[i - 1][j - 1][1]
                prefix[i][j][2] = prefix[i][j - 1][2] + prefix[i - 1][j][2] - prefix[i - 1][j - 1][2] + 1

for _ in range(K):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    if a == 0 and b == 0:
        print(*prefix[c][d])
    elif a == 0:
        J = prefix[c][d][0] - prefix[c][b - 1][0]
        I = prefix[c][d][1] - prefix[c][b - 1][1]
        O = prefix[c][d][2] - prefix[c][b - 1][2]
        print(J, I, O)
    elif b == 0:
        J = prefix[c][d][0] - prefix[a - 1][d][0]
        I = prefix[c][d][1] - prefix[a - 1][d][1]
        O = prefix[c][d][2] - prefix[a - 1][d][2]
        print(J, I, O)
    else:
        J = prefix[c][d][0] - prefix[a-1][d][0] - prefix[c][b-1][0] + prefix[a-1][b-1][0]
        I = prefix[c][d][1] - prefix[a-1][d][1] - prefix[c][b-1][1] + prefix[a-1][b-1][1]
        O = prefix[c][d][2] - prefix[a-1][d][2] - prefix[c][b-1][2] + prefix[a-1][b-1][2]
        print(J, I, O)
