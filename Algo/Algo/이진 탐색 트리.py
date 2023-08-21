import sys
sys.stdin = open('input.txt')

# 트리에 값 넣기
def inorder(n):
    global cnt
    if n:
        inorder(c1[n])
        cnt += 1
        value[n] = cnt
        inorder(c2[n])

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    tree = []
    c1 = [0]*(n+1)
    c2 = [0]*(n+1)
    # 트리 값
    value = [0]*(n+1)
    cnt = 0
    # 완전 이진 트리 형태 구성
    for i in range(1, n//2+1):
        for j in [i*2, i*2+1]:
            if j <= n:
                tree.append((i, j))
    # 트리 바탕으로 자식 노드 구성
    while tree:
        i, j = tree.pop(0)
        if c1[i] == 0:
            c1[i] = j
        else:
            c2[i] = j
    inorder(1)
    print(f'#{tc}', value[1], value[n//2])