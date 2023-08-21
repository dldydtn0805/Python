import sys
sys.stdin = open('input.txt')

# 중위 순회 하면서 값 채우기
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
        # 길이 4일때 양쪽 노드
        if len(vertex) > 3:
            c2[index] = int(vertex[3])
            c1[index] = int(vertex[2])
        # 길이 3일때 왼쪽 노드
        elif len(vertex) > 2:
            c1[index] = int(vertex[2])
        value[index] = vertex[1]
    # 중위 순회
    inorder(1)
    print(f'#{tc}', result)
