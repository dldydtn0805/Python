import sys
# sys.stdin = open('input.txt')

# 해당 문자가 숫자인지 판단해주는 함수
def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

n = int(input())

A = [input() for _ in range(n)]
# 버블정렬을 통한 문자열 정렬
for i in range(n-1):
    for j in range(i+1, n):
        # 길이가 짧으면 앞으로 보내주기
        if len(A[j]) < len(A[i]):
            A[i], A[j] = A[j], A[i]
        # 길이가 같을때 경우의 수
        elif len(A[j]) == len(A[i]):
            # temp1에 J 문자열의 숫자의 합을, temp2에 I 문자열의 숫자의 합을 세어주었다
            temp1 = 0
            temp2 = 0
            for J in A[j]:
                if isNumeric(J):
                    temp1 += int(J)
            for I in A[i]:
                if isNumeric(I):
                    temp2 += int(I)
            # 만약 temp1이 작으면 앞으로 보내주기
            if temp1 < temp2:
                A[i], A[j] = A[j], A[i]
            # 만약 temp1과 temp2가 같으면, 값 자체를 비교해서 작다면 앞으로 보내주기
            if temp1 == temp2:
                if A[j] < A[i]:
                    A[i], A[j] = A[j], A[i]

#람다를 이용한 정렬

# A = sorted(A, key=lambda x:(len(x), (x), x)):

for a in A:
    print(a, end='\n')


