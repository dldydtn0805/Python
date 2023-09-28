def can_purchase(N, C, weights):
    # 무게 정렬
    weights.sort()

    # 첫번쨰 항목 탐색~
    for i in range(N):
        # 두번쨰 항목 탐색~
        for j in range(i + 1, N):
            # 세번째 항목 탐색~
            for k in range(j + 1, N):
                # 세 개 무게 합산
                total_weight = weights[i] + weights[j] + weights[k]

                # 합 무게가 목표 무게와 같으면 1을 반환
                if total_weight == C:
                    return 1

                # 합 무게가 목표 무게보다 크면, 종료하고 다음 반복
                elif total_weight > C:
                    break

    # 어떠한 조합도 없을경우 0
    return 0


N, C = map(int, input().split())
weights = list(map(int, input().split()))

# 구매 가능한지 확인
result = can_purchase(N, C, weights)

print(result)