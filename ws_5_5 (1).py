# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(my_list):
    i = 0
    list22 = []
    while len(my_list) > 0 :
        if my_list[i] % 2 == 1:
            my_list.pop(i)
        elif my_list[i] % 2 == 0:
            list22.extend([my_list.pop(i)])
    return list22
    pass

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)