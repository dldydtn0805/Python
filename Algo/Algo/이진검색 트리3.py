
import sys
sys.stdin = open('input.txt')
# 재귀 제한 해제
sys.setrecursionlimit(10**9)

def postorder(root, end):
    if root > end:
        return

    # 만약 root 보다 큰값이 없는 경우 전부 왼쪽 서브트리로 취급
    start = end + 1

    for i in range(root+1, end+1):
        if value[root] < value[i]:
            start = i
            break

    # 후위 순회
    # 루트 다음부터 왼쪽 서브트리 탐색
    postorder(root +1, start-1)
    # 왼쪽 서브트리 탐색 끝나면 오른쪽 서브트리 탐색
    postorder(start, end)
    # 왼쪽, 오른쪽 서브트리 탐색 끝나면 root 출력
    print(value[root])

value = []

while True:
    try:
        n = int(input())
        value.append(n)
    except:
        break

postorder(0, len(value)-1)

"""
https://storing.tistory.com/48
"""