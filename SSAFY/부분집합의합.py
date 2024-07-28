import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    #1에서 12까지의 숫자를 원소로 가진 집합 A
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    #부분집합의 원소의 개수 N, 부분집합의 원소의 합 K
    N, K = map(int, input().split())
    check = 0 # 목표 케이스의 개수
    for i in range(1<<12): # 1<<12 전체 부분집합 구성 순회, 12는 전체 원소의 개수
        result = 0 #부분집합의 합
        cnt = 0 #부분집합의 원소 개수
        for j in range(12): # 부분집합 구성 순회, 12는 전체 원소의 개수
            if i & (1<<j): #i의 j번 비트가 1인 경우
                result += A[j] # 부분집합의 합을 구한다
                cnt += 1 #부분집합의 원소 개수를 구한다

        # j 반복문 1회를 돌려 부분집합 1개를 구했을때,
        if result == K and cnt == N: # 만약 부분집합의 합이 K, 개수가 N이라면
            check += 1 #목표 케이스의 개수를 추가하고
            continue # 다시 i 반복문을 순회한다
        # print()
        # print(result)
    print(f'#{tc}', check)