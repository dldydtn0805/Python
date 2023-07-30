# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(aaa):
    list33 = []
    while len(aaa) > 0:
        if aaa[0] % 2 == 1:
            aaa.pop(0)
        elif aaa[0] % 2 == 0:
            list33.extend([aaa.pop(0)])
    return list33
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)


#인자로 받은 aaa의 개수가 0 이상일때 작업을 반복한다
#aaa의 0번 인덱스를 2로 나눈 나머지가 1이면 홀수, 0번 인덱스를 삭제한다 반환값은 저장하지 않는다
#aaa의 0번 인덱스를 2로 나눈 나머지가 0이면 짝수, 0번 인덱스를 삭제하고 반환값을 list33에 extend로 저장한다
