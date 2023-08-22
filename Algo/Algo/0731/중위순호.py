import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):

    N = int(input())
    tree = [0] *(N+1) # n번 노드까지 있는 완전 이진 트리
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])]