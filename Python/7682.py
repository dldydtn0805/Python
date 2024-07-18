import sys
input = sys.stdin.readline

def check(arr):
    # row check
    row = -1
    winner = 'No'
    for i in range(3):
        if arr[i][0] != '.' and arr[i][0] == arr[i][1] == arr[i][2]:
            if row == -1:
                row = i
            else:
                return False
    if row != -1:
        winner = arr[row][0]
    # col check
    col = -1
    for i in range(3):
        if arr[0][i] != '.' and arr[0][i] == arr[1][i] == arr[2][i]:
            if col == -1:
                col = i
            else:
                return False

    if col != -1:
        winner = arr[0][col]

    # cross check
    cross = -1
    if arr[1][1] != '.' and  arr[0][0] == arr[1][1] == arr[2][2] and arr[0][2] == arr[1][1] == arr[2][0]:
        cross = 0
    elif arr[1][1] != '.' and arr[0][0] == arr[1][1] == arr[2][2]:
        # \ cross
        cross = 1
    elif arr[1][1] != '.' and arr[0][2] == arr[1][1] == arr[2][0]:
        # / cross
        cross = 2

    if cross != -1:
        winner = arr[1][1]

    if row == 0 and col == 3:
        if cross == 1:
            return False
    elif row == 3 and col == 0:
        if cross == 2:
            return False

    return winner

def game(input):
    board = [[],[],[]]
    for i in range(9):
       board[i%3].append(input[i])
    arr = board[:]
    o_cnt = 0
    x_cnt = 0
    dot_cnt = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 'O':
                o_cnt += 1
            elif arr[i][j] == 'X':
                x_cnt += 1
            else:
                dot_cnt += 1
    difference = x_cnt - o_cnt
    if difference == 0:
        # winner is O
        if check(arr) == 'O':
            return True
    elif difference == 1:
        if not dot_cnt:
            if check(arr) == 'No':
                return True
        # winner is X
        if check(arr) == 'X':
            return True
    else:
        return False



while True:
    arr = list(input().rstrip())
    if ''.join(arr) == 'end':
        exit()
    else:
        if (game(arr)): print('valid')
        else: print('invalid')

