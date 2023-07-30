import requests
from pprint import pprint as print

dummy_data = []

for i in range(1, 11):
# 무작위 유저 정보 요청 경로
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
# API 요청
    response = requests.get(API_URL)
# JSON -> dict 데이터 변환
    parsed_data = response.json()

    dict11 = {
        'company': parsed_data['company']['name'],
        'lat': parsed_data['address']['geo']['lat'],
        'lng': parsed_data['address']['geo']['lng'],
        'name': parsed_data['name']
    }

    if -80< float(dict11['lat']) < 80 and -80< float(dict11['lng']) < 80:
        dummy_data.append(dict11)

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

def create_user(dummy_data):
    censored_user_list = {}
    for data in dummy_data:
        if censorship(data) is True:
            censored_user_list[data['company']] = data['name']
    return censored_user_list
def censorship(data):
    if data['company'] in black_list:
        print(f'{data["company"]}소속의 {data["name"]} 은/는 등록할 수 없습니다')
        return False
    else:
        print('이상 없읍니다.')
        return True
    
print(create_user(dummy_data))
    
#censored_user_list = {x: y}로 키와 값을 할당하는것
#censored_user_list = {} 이후 censored_user_list[x] = y로 키와 값을 할당하는것
#둘은 다르다
#1은 딕셔너리를 새로 생성하고 키와 값을 할당한다
#2는 딕셔너리를 새로 생성하고 키와 값을 할당한다
#1은 이 과정을 한번에 한다
#2는 이 과정을 두번에 나눠서 한다
#반복문을 사이에 두고 나눠서 한다면
#1은 사이에 둘수가 없어서 계속 딕셔너리 값이 초기화된다
#2는 사이에 둘수가 있어서 딕셔너리에 값이 추가가 된다

#if 변수 in 리스트를 사용한다
