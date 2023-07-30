# hw_6_2.py

# 아래 함수를 수정하시오.
def remove_duplicates_to_set(xxx):
    for x in xxx:
        while xxx.count(x) > 1:
            xxx.remove(x)
    return set(xxx)

		
result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)

#set() 함수만 사용해도 중복된 요소가 제거된다

