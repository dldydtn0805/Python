import sys
sys.stdin = open('input.txt')

# 완전 이진트리에서 노드의 합 구하기
def postorder(k):
    if k*2<=n:
        postorder(2*k)
        postorder(2*k+1)
        tree[k] = tree[k*2]+tree[k*2+1]

T = int(input())
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    # 나무 구성
    tree = [0]*(n+2)
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a] = b
    postorder(1)
    print(f'#{tc}', tree[l])


