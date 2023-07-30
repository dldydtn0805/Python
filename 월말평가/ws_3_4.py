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

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

print(list(map(create_user, name, age, address)))

#list로 감싸는것까지만 하면 함수에 포함된 print문이 출력된다
#최종적으로 list를 출력을 하면 map이 반영된 return값들이 리스트에 감싸져서 나온다 