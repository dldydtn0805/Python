import sys
sys.stdin = open('input.txt')

number = int(input())
x = 1
cnt = 0
# 숫자가 낮을때는 정상 작동하고
# 숫자가 높을때는 정상 작동 안하는 이유는 뭘까???
while x<number:
    if 3*x > number:
        if 2*x > number:
            x= x+1
            cnt += 1
        else:
            x= x* 2
            cnt += 1
    else:
        x = x*3
        cnt += 1
print(cnt)