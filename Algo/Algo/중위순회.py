import sys
sys.stdin = open('input.txt')

def inorder(p, N): # N 완전이진트리의 마지막 정점
    if p <= N:
        inorder(p*2, N)
        print(tree[p], end ='')
        inorder(p*2+1, N)

for tc in range(1, 11):
    N = int(input())
    tree = [0] *(N+1) # n번 노드까지 있는 완전 이진 트리
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]
    # 중위 순회
    print(f'#{tc}', end=' ')
    inorder(1, N) # root = 1
    print()