# ws_4_3.py

import requests
from pprint import pprint as print

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
        

# 무작위 유저 정보 요청 경로
for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
# API 요청
    response = requests.get(API_URL)
# JSON -> dict 데이터 변환
    parsed_data = response.json()

# 응답 데이터 출력
    # print(response)

# 변환 데이터 출력
    # print(parsed_data)
# # 변환 데이터의 타입
#     print(type(parsed_data))

# 특정 데이터 출력

    new_dict(parsed_data)
print(dummy_data)