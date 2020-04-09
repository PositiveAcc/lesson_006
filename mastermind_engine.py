from random import randint

game_number = ''
bulls_and_cows = {'bulls': 0, 'cows': 0}

def make_a_number():
    return str(randint(1, 9))+str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))


def check_number(user_number):
    tmp_list = []
    for i, value in enumerate(user_number):
        global game_number
        if game_number[i] == user_number[i]:
            bulls_and_cows['bulls'] += 1
        tmp_list.append(game_number[i])
    for i, value in enumerate(tmp_list):
        if value != user_number[i]:
            for vl in user_number:
                if value == vl:
                    bulls_and_cows['cows'] += 1

    return bulls_and_cows


def game_not_over(number):
    check_number(user_number=number)
    return bulls_and_cows['bulls'] < 4

