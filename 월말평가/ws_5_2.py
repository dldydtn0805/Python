# ws_5_2.py

# 아래 함수를 수정하시오.
def remove_duplicates(aaa):
    new_lst = []
    new_lst.extend(aaa)
    for i22 in new_lst:
        while new_lst.count(i22) > 1:
            new_lst.remove(i22)
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

#extend 메서드로 new_list에 aaa를 합친다
#new_list를 순회하면서, count 메서드로 개수를 확인한다
#개수가 1보다 클 경우에, remove 메서드로 요소를 삭제한다