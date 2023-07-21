
ws_3_1_number_of_people = 0
def increase_user():
    global ws_3_1_number_of_people
    ws_3_1_number_of_people += 1
    return ws_3_1_number_of_people
print('현재 가입 된 유저 수 :',increase_user())