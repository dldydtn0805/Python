import sys
sys.setrecursionlimit(10**9)

base = 3
input = "3"

result_string = ''

def get_part(size):
    if size is 1:
        return '-'

    first_part_index = 0
    second_part_index = size / base
    third_part_index =

    # 27
    # 1-9,
    # 10-18,
    # 18-27


    for i in range():

    return get_part(left) + get_part(center) + get_part(right)

def get_cantor_set(input):
    result_string = get_part(3 ** input)
    for i in range(3 ** input):
        def generate_strings(n):
            x

            return result

        # Get user input for 'n'
        n = int(input("Enter the value of n: "))

        # Generate strings and print the result
        result_list = generate_strings(n)
        print(result_list)

