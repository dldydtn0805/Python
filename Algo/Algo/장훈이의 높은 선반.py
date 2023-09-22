def recur(level, acc_height):
    global ans
    #가지치기, 현재까지 탑이 선반 높이를 넘어간다면 앞으로는 더 볼 필요가 없다
    if acc_height >= b:
        ans = min(ans, acc_height)
        return
    # 기저 조건
    if level == n:
        return
    # 해당 점원을 탑에 쓸 경우
    recur(level + 1 , acc_height + arr[level])
    # 안쓸 경우
    recur(level+1, acc_height)


T = int(input())
for tc in range(1,T+1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    recur(0,0)
    print(f'#{tc}', ans-b)