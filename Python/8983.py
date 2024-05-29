import sys
input = sys.stdin.readline

def 이진탐색(arr, target):
    왼쪽경계, 오른쪽경계 = 0, len(arr)-1
    while 왼쪽경계 <= 오른쪽경계:
        중앙 = (왼쪽경계 + 오른쪽경계) // 2
        if arr[중앙] == target:
            return 중앙
        elif arr[중앙] < target:
            왼쪽경계 = 중앙 + 1
        else:
            오른쪽경계 = 중앙 - 1
    return 오른쪽경계

M, N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for i in range(N):
    x, y = map(int, input().split())
    가까운사로 = (이진탐색(arr, x))
    최소거리 = abs(x - arr[가까운사로]) + y
    if 가까운사로 != M-1:
        오른쪽최소거리 = abs(x - arr[가까운사로+1]) + y
    else:
        오른쪽최소거리 = 1e9
    진짜최소거리 = min(최소거리, 오른쪽최소거리)
    if 진짜최소거리 <= L:
        cnt += 1
print(cnt)
