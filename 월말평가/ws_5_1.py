# ws_5_1.py

# 아래 함수를 수정하시오.
def reverse_string(string):
    dd = reversed(string)
    ee = ''.join(dd)
    return ee
    
result = reverse_string("Hello, World!")
print(result)

#reversed()로 뒤집혀진 iterator 객체를 만들 수 있다
#뒤집혀진 객체를 join()으로 하나의 string으로 만든다
