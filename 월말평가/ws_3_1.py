number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

increase_user()
print(number_of_people)

#global 선언을 통해 global 변수를 함수내에서 변경 가능하게 한다