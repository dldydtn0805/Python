number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    
    increase_user()
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    return user_info

print('현재 가입 된 유저 수 : ',number_of_people)
print(create_user('홍길동', 30, '서울'))
print('현재 가입 된 유저 수 : ',number_of_people)

#함수의 위치인자를 입력해서 딕셔너리에 할당한다.
#함수의 return 값을 print하는 방법을 알수있다