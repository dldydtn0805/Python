import sys
input=sys.stdin.readline
k, n = map(int, input().split())
arr=[0]*k
for i in range(k):
    arr[i]=int(input())
# 자르기 전의 랜선들 입력 받아서 그 중 가장 긴 길이의 랜선을 찾아낸다
max_v = max(arr)
result=0
# 매개변수 탐색을 진행한다
def binary(start, end):
    global result
    # 재귀 중지 조건, 시작이 끝보다 커서는 안된다
    if end<start:
        return
    mid=(start+end)//2
    temp=0
    # 해당 턴에 잘라지는 랜선의 갯수를 temp에 담는다
    for a in arr:
        temp+=a//mid
    # 개수가 n 이상이라면 result에 담고 시작을 mid + 1 로 바꾸고 재귀
    if temp>=n:
        result=mid   
        binary(mid+1, end)
    # 그 외의 경우에는 끝을 mid - 1로 바꾸고 재귀
    else:
        binary(start, mid-1)
binary(0, max_v*2)
print(result)