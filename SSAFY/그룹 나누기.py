# import sys
# sys.stdin = open('input.txt')

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x==y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find_set(x):
    if x == parent[x]:
        return x
    # 경로 압축을 해서 각 노드들의 리턴 값이 대표자를 향하도록 수정해준다
    parent[x] = find_set(parent[x])
    return parent[x]

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [i for i in range(n)]
    for i in range(0, 2*m, 2):
        x = arr[i]
        y = arr[i+1]
        # 신청서 접수
        union(x-1,y-1)
    # 전체 몇개의 조가 만들어지는지 만들기 위해서 각 노드들의 대표가 누구인지 체크한다
    sets = []
    for i in range(len(parent)):
        sets.append(find_set(parent[i]))
    sets = set(sets)
    print(f'#{tc}', len(sets))