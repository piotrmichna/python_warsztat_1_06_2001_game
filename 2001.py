from random import randint


def dice_get_command(str_command):
    # return dice=[x,y,'operation',z] or False
    dice = []

    d_command = str_command.upper()
    if 'D' not in d_command:
        return False

    # geting X
    l_command = d_command.split('D')
    if l_command[0] == '' or l_command[0] == '0':
        dice.append(1)
    else:
        try:
            dice.append(int(l_command[0]))
        except ValueError:
            print('Błędna ilość rzutów')
            return False

    # geting Y,Z
    if '+' in l_command[1]:
        z = l_command[1].split('+')
        try:
            dice += [int(z[0]), '+', int(z[1])]
        except ValueError:
            print("Błędne parametry kości")
            return False

    elif '-' in l_command[1]:
        z = l_command[1].split('-')
        try:
            dice += [int(z[0]), '-', int(z[1])]
        except ValueError:
            print("Błędne parametry kości")
            return False
    else:
        try:

            dice.append(int(l_command[1]))
        except ValueError:
            print("Błędne parametry kości")
            return False

    # dice type
    if not dice[1] in [3, 4, 6, 8, 10, 12, 20, 100]:
        print(f'Nie znam kostki {dice[1]}-ściennej!')
        return False

    return dice


def dice_roll(command_str):
    dice = []
    while not dice:
        dice = dice_get_command(command_str)

    # dice [x, y] or dice [x, y, '+'/'-', z]
    dice_value = 0
    for n in range(dice[0]):  # number rolling
        # roll_v = randint(1, dice[1])
        # print(roll_v)
        dice_value += randint(1, dice[1])

    # dice [x, y, '+'/'-', z]
    if len(dice) > 2:
        if dice[2] == '+':
            dice_value += dice[3]
        else:
            dice_value -= dice[3]

    return dice_value