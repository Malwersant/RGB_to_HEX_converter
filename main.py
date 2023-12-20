user_input_1 = int(input())
user_input_2 = int(input())
user_input_3 = int(input())
user_list = [user_input_1, user_input_2, user_input_3]
# user_list = [user_input_1]

v1 = list(range(10))
v2 = ['a', 'b', 'c', 'd', 'e', 'f']

v = v1 + v2

d = dict(list(enumerate(v)))


def hex_calculate_iteration():
    string = ''
    end_string = ''
    for i in user_list:
        base, reminder = [i // 16, i % 16]
        while base != 0 or reminder >= 1:
            string = str(d[reminder]) + string
            base, reminder = [base // 16, base % 16]
        end_string += string
        string = ''
    return '#' + end_string


print(hex_calculate_iteration())




