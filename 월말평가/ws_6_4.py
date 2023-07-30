# ws_6_4.py

# 아래 함수를 수정하시오.
def get_keys_from_dict(xxx):
    list22 = []
    for kkk in xxx.keys():
        list22.append(kkk)
    return list22

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)

#for k 딕셔너리.keys() 구문을 사용한다
