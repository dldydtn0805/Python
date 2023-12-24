import sys
# sys.stdin = open('input.txt')

'''
64cm 길이의 막대기가 있다

x cm인 막대기를 만들고싶다

따라서 원래 가지고있던 막대기를 자르고 풀로 붙여서 x cm 막대기로 만들고자한다

1. 가지고있는 막대의 길이를 모두 더함, 처음에는 64cm 막대 하나만 있음, 이때 합이 x보다 크면 아래 과정

    1. 가지고있는 막대중 가장 짧은 막대를 절반으로 자름
    
    2. 만약 자른 막대의 절반중 하나를 버리고 남아있는 막대의 길이의 합이 x보다 크거나 같다면 위에서 자른 막대의 절반중 하나를 버린다
    
2. 남은 막대를 풀로 붙여서 xcm를 만든다
'''

def reverse(str):
    n = len(str)
    result = ''
    for i in range(n-1,-1,-1):
        result+= str[i]
    print(result.count('1'))

# 2진수를 만드는 함수
def makeBinary(num, bin):
    if num == 1:
        reverse(bin+'1')
        return
    if num%2 == 0:
        makeBinary(num//2, bin+'0')
    else:
        makeBinary(num//2, bin+'1')
x = int(input())
makeBinary(x, '')

