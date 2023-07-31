# ws_5_5.py
result = []
# 아래 함수를 수정하시오.
def my_function(list_input): 
    while len(list_input) != 0: #리스트의 요소를 모두 소진할때 까지
        element = list_input.pop(0) #리스트의 맨 앞에 요소를 제거 후 반환
        if element % 2 == 0: #반환된 요소가 짝수라면
            result.extend([element])
    return result
            


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = my_function(my_list)
print(result)