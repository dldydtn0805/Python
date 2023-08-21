import sys
sys.stdin = open('input.txt')

def inorder(n):
    global result
    if n:
        inorder(c1[n])
        result += value[n]
        inorder(c2[n])
for tc in range(1, 11):
    n = int(input())
    c1 = [0] * (n+1)
    c2 =[0] * (n+1)
    value = [0] * (n+1)
    result = ''
    for _ in range(n):
        vertex = list(input().split())
        index = int(vertex[0])
        # 오른쪽 자식
        if len(vertex) > 3:
            c2[index] = int(vertex[3])
            c1[index] = int(vertex[2])
        elif len(vertex) > 2:
            c2[index] = int(vertex[2])
        value[index] = vertex[1]
    inorder(1)
    print(result)
