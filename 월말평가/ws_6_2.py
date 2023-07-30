# ws_6_2.py

# 아래 함수를 수정하시오.
def get_value_from_dict(dict22,arg22):
    return dict22.get(arg22)

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result) # Alice

#딕셔너리.get(키)로 값을 찾는다
#없는 키라면 None을 반환한다

