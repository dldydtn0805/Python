black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

def create_user(dummy_data):
    censored_user_list = {}
    for data in dummy_data:
        if censorship(data) is True:
            censored_user_list[data['name']] = data['company'] #딕셔너리에 키를 내가 문자열로 넣는것 뿐만 아니라 순회하는 요소의 키를 변수로 넣는걸 생각하지 못했다   
    return censored_user_list

def censorship(data):
    if data['company'] in black_list:
        print(f'{data["company"]} 소속의 {data["name"]} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다')
        return True

import requests
# from pprint import pprint as print

dummy_data = []

def new_dict(parsed_data):    
    global dummy_data
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and 80 > float(parsed_data['address']['geo']['lng']) > -80 : 
        item = {
        'company': parsed_data['company']['name'],
        'lat': parsed_data['address']['geo']['lat'],
        'lng': parsed_data['address']['geo']['lng'],
        'name': parsed_data['name']
    }
        dummy_data.append(item)
        
for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    new_dict(parsed_data)

print(create_user(dummy_data))
