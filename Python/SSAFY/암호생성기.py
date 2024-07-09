import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    n = int(input())
    password = list(map(int, input().split()))
    # i는 빼는 수
    i = 1
    while True:
        # 맨 앞의 수를 뒤로 보내기
        a = password.pop(0)
        # 맨 앞의 수에서 i를 뺀 상태가 0보다 작으면 탈출
        if a-i > 0:
            password.append(a-i)
        else:
            password.append(0)
            break
        # i는 1에서 5까지 반복한다
        i += 1
        if i == 6:
            i = 1
    print(f'#{tc}', *password)
