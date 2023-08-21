import sys
sys.stdin = open('input.txt')

# 전위 순회
def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(c1[n])
        preorder(c2[n])

T = int(input())
for tc in range(1,T+1):
    e, n = map(int, input().split())
    tree = list(map(int, input().split()))
    # 부모 노드를 인덱스로 하는 자식 노드 배열
    c1 = [0] * (e+2)
    c2 = [0] * (e+2)
    # 자식 노드를 인덱스로 하는 부모 노드 배열
    par = [0] * (e+2)

    for i in range(0, len(tree), 2):
        p, c = tree[i], tree[i+1]
        # 자식 노드 양쪽에 채워 넣기
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    cnt = 0
    preorder(n)
    print(f'#{tc}', cnt)