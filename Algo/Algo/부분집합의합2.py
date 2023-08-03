# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    #1에서 10까지의 숫자를 원소로 가진 집합 A
    A = list(map(int, input().split()))
    check = 0 # 목표 케이스의 개수
    for i in range(1<<10): # 1<<10 전체 부분집합 구성 순회, 10은 전체 원소의 개수
        result = 0 #부분집합의 합
        cnt = 0 #부분집합의 원소 개수
        for j in range(10): # 부분집합 구성 순회, 10은 전체 원소의 개수
            if i & (1<<j): #i의 j번 비트가 1인 경우
                result += A[j] # 부분집합의 합을 구한다
                cnt += 1 #부분집합의 원소 개수를 구한다

        # j 반복문 1회를 돌려 부분집합 1개를 구했을때,
        if result == 0 and cnt > 1: # 만약 부분집합의 합이 0, 개수가 1 이상 이라면
            check = 1 #목표 케이스의 개수를 추가하고
            continue # 다시 i 반복문을 순회한다
        # print()
        # print(result)
    print(f'#{tc}', check)