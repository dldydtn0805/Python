from modifi_ws_3_1 import increase_user
num = 0

print('현가유:', num)

def create_user(name, age, address):
    print('현가유:', increase_user())
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    return user_info

print(create_user('홍길동', 30, '서울'))