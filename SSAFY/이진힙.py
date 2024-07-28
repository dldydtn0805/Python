import sys
sys.stdin = open('input.txt')


# 나무 심기
def enque(k):
    tree.append(k)
    c = tree.index(k)
    p = c//2
    while p:
        if tree[c] < tree[p]:
            tree[c], tree[p] = tree[p], tree[c]
            # 이부분때문에 틀렸었음 갱신 안해서
            c = p
            p = c // 2
        else:
            break


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    tree = [0]
    result = [0]
    # 입력받은 나무를 enque 함수에 넣어주기
    while numbers:
        x = numbers.pop(0)
        enque(x)
    print(tree)

    # 문제에서 요구하는 값 찾기
    point = 0
    while n:
        n //= 2
        point += tree[n]
    print(f'#{tc}', point)



