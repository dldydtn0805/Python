# ws_4_3.py

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
print(dummy_data)

#딕셔너리에 능숙하게 값을 할당해서 생성할수있다
#조건문을 사용해서 append 할수있다

