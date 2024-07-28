def check_row(row, col, value):
    for i in range(9):
        if arr[row][i] == value and i != col:
            return False
    return True


def check_col(row, col, value):
    for i in range(9):
        if arr[i][col] == value and i != row:
            return False
    return True

def check_box(i, j, value):
    if 0 <= i < 3 and 0 <= j < 3:
        for ni in range(0,3):
            for nj in range(0,3):
                if arr[ni][nj] == value and i != ni and j != nj:
                    return False
    elif 0 <= i < 3 and 3 <= j < 6:
        for ni in range(0,3):
            for nj in range(3,6):
                if arr[ni][nj] == value and i != ni and j != nj:
                    return False
    elif 0 <= i < 3 and 6 <= j < 9:
        for ni in range(0,3):
            for nj in range(6,9):
                if arr[ni][nj] == value and i != ni and j != nj:
                    return False
    elif 3 <= i < 6 and 0 <= j < 3:
        for ni in range(3,6):
            for nj in range(0,3):
                if arr[ni][nj] == value and i != ni and j != nj:
                    return False
    elif 3 <= i < 6 and 3 <= j < 6:
        for ni in range(3,6):
            for nj in range(3,6):
                if arr[ni][nj] == value and i != ni and j != nj:
                    return False
    elif 3 <= i < 6 and 6 <= j < 9:
        for ni in range(3,6):
            for nj in range(6,9):
                if arr[ni][nj] == value and i != ni and j != nj:
                    return False
    elif 6 <= i < 9 and 0 <= j < 3:
        for ni in range(6,9):
            for nj in range(0,3):
                if arr[ni][nj] == value and i != ni and j != nj:
                    return False
    elif 6 <= i < 9 and 3 <= j < 6:
        for ni in range(6,9):
            for nj in range(3,6):
                if arr[ni][nj] == value and i != ni and j != nj:
                    return False
    elif 6 <= i < 9 and 6 <= j < 9:
        for ni in range(6,9):
            for nj in range(6,9):
                if arr[ni][nj] == value and i != ni and j != nj:
                    return False
    return True

def backtracking(i, j):
    if i == 9:
        for answer in arr:
            print(''.join(map(str,answer)))
        exit()
    if j < 8:
        next_i, next_j = i, j+1
    else:
        next_i, next_j = i+1, 0

    if arr[i][j] == 0:
        for num in range(1, 10):
            if check_row(i, j, num) and check_col(i, j, num) and check_box(i, j, num):
                arr[i][j] = num
                backtracking(next_i, next_j)
                arr[i][j] = 0
    else:
        backtracking(next_i, next_j)

arr = [list(map(int, input())) for _ in range(9)]
N = 9
backtracking(0, 0)
