# import sys
# sys.stdin = open('input.txt')

def check(q):
# 0 1 2
# 3 4 5
# 6 7 8
    global cnt, flag2
    if q[0]==q[1]==q[2]!='.':
        cnt += 1
        if q[0] == 'O':
            flag2 = 1
    if q[0]==q[4]==q[8]!='.':
        cnt += 1
        if q[0] == 'O':
            flag2 = 1
    if q[0]==q[3]==q[6]!='.':
        cnt += 1
        if q[0] == 'O':
            flag2 = 1
    if q[1]==q[4]==q[7]!='.':
        cnt += 1
        if q[1] == 'O':
            flag2 = 1
    if q[2]==q[5]==q[8]!='.':
        cnt += 1
        if q[2] == 'O':
            flag2 = 1
    if q[3]==q[4]==q[5]!='.':
        cnt += 1
        if q[3] == 'O':
            flag2 = 1
    if q[6]==q[4]==q[2]!='.':
        cnt += 1
        if q[6] == 'O':
            flag2 = 1
    if q[6]==q[7]==q[8]!='.':
        cnt += 1
        if q[6] == 'O':
            flag2 = 1
tictok = [list(input()) for _ in range(9)]
quest = (tictok[:-1])
for q in quest:
    cnt = 0
    flag = 0
    flag2 = 0
    check(q)
    cnt_o = 0
    cnt_x = 0
    for i in range(9):
        if q[i] == 'O':
            cnt_o += 1
        elif q[i] == 'X':
            cnt_x += 1
    if cnt_x == 5 and cnt_o == 4:
        flag = 1
    if cnt == 1:
        flag = 1
    if cnt_x < cnt_o:
        flag = 0
    if cnt_x > cnt_o:
        if flag2 == 1:
            flag = 0
    if flag:
        print('valid')
    else:
        print('invalid')
