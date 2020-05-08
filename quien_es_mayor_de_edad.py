def is_user_one_mayor_que_user_two():
    return age_user_one > age_user_two


def is_user_one_menor_que_user_two():
    return age_user_one < age_user_two


def print_older_user_message(old_user, young_user):
    print(f'Ey {old_user} eres mayor que {young_user}')


user_one = input('Hola usuario 1 como es tu nombre? : ')
age_user_one = int(input(f'{user_one} cual es tu edad? : '))
user_two = input('Hola usuario 2 como es tu nombre? : ')
age_user_two = int(input(f'{user_two} cual es tu edad? : '))

if is_user_one_mayor_que_user_two():
    print_older_user_message(user_one, user_two)
elif is_user_one_menor_que_user_two():
    print_older_user_message(user_two, user_one)
else:
    print(f'Ey {user_one} y {user_two} ustedes tienen la misma edad!')
