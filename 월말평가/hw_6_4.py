# hw_6_4.py

# 아래 함수를 수정하시오.
def add_item_to_dict(dict22, aaa, bbb):
    new_dict = dict22.copy()
    dict33 = {aaa:bbb}
    new_dict.update(dict33)
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)

#딕셔너리33에 {aaa:bbb}를 할당해서 생성한다
#딕셔너리.update(다른딕셔너리)로 업데이트 한다

