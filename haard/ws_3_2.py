from ws_3_1 import increase_user

number_of_people = 0

print('현재 가입 된 유저 수 :',number_of_people)
print('현재 가입 된 유저 수 :', increase_user())

def create_user(name, age, address):
    user_info = {}
    user_info['name'] = name, 
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    return user_info
    
print(create_user(name = '홍길동', age =  30, address = '서울'))

