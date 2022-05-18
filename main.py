class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


def players_input_check():
    while True:
        player_one = input('Player one name: ')
        player_two = input('Player two name: ')
        while player_one.isdigit() or '' == player_one or '  ' in player_one:
            print('Player 1 please input a correct name')
            player_one = input('Player one name: ')

        while player_two.isdigit() or '' == player_two or '  ' in player_two:
            print('Player 2 please input a correct name')
            player_two = input('Player two name: ')

        else:
            break

    while True:
        first_sign = input(f'{player_one} would you like to play with "X" or "O"? ').upper()
        if first_sign == "X" or first_sign == "O":
            break

    second_sign = "O" if first_sign == "X" else "X"

    return Player(player_one, first_sign), Player(player_two, second_sign)


def print_the_field():
    field = ['|  1  |  2  |  3  |', '|  4  |  5  |  6  |', '|  7  |  8  |  9  |']
    print('This is the numeration of the board:')
    for row in field:
        print(row)
    return field


def check_for_draw(playing_field):
    draw_flag = True
    for x in range(len(playing_field)):
        for y in range(len(playing_field)):

            if not playing_field[x][y]:
                draw_flag = False
    if draw_flag:
        print(f'{first_player.name} and {second_player.name} you have a draw')
        exit()


def player_choice_validation(player_choice, playing_field, row, col):
    flag = True
    if not player_choice.isdigit():
        flag = False
        return flag
    elif not 1 <= int(player_choice) <= 9 or playing_field[row][col] == first_player.sign or playing_field[row][col] == second_player.sign:
        check_for_draw(playing_field)
        flag = False
        return flag
    else:
        return flag


def making_row_col_for_choice(player_choice):

    if int(player_choice) <= 3:
        row = 0
        col = int(player_choice) - 1

    elif int(player_choice) <= 6:
        row = 1
        col = int(player_choice) - 4

    else:
        # player_choice <= 9
        row = 2
        col = int(player_choice) - 7

    return row, col


def first_or_second_player_winner(*args):

    first_player_list_elements = [first_player.sign, first_player.sign, first_player.sign]
    second_player_list_elements = [second_player.sign, second_player.sign, second_player.sign]
    if args[0] == first_player_list_elements or args[1] == first_player_list_elements or args[2] == first_player_list_elements:
        return first_player.name
    elif args[0] == second_player_list_elements or args[1] == second_player_list_elements or args[2] == second_player_list_elements:
        return second_player.name
    elif args[0] == first_player_list_elements or args[1] == first_player_list_elements:
        return first_player.name
    elif args[0] == second_player_list_elements or args[1] == second_player_list_elements:
        return second_player.name


def print_the_board(playing_field):

    for r in range(len(playing_field)):
        for c in range(len(playing_field)):

            if not playing_field[r][c]:
                playing_field[r][c] = ' '

    for x in playing_field:
        print(f'| {x[0]} | {x[1]} | {x[2]} |')

    for r in range(len(playing_field)):
        for c in range(len(playing_field)):

            if playing_field[r][c] == ' ':
                playing_field[r][c] = False


def winner_or_not(playing_field):

    #logic with all
    first_player_list_elements = [first_player.sign, first_player.sign, first_player.sign]
    second_player_list_elements = [second_player.sign, second_player.sign, second_player.sign]
    x = all(playing_field[0])
    y = all(playing_field[1])
    z = all(playing_field[2])
    x_list = playing_field[0]
    y_list = playing_field[1]
    z_list = playing_field[2]
    # horizontal
    if x or y or z:
        if x and x_list == first_player_list_elements or x_list == second_player_list_elements:
            print_the_board(playing_field)
            print(f'{first_or_second_player_winner(x_list, y_list, z_list)} is a winner')
            exit()
        elif y and y_list == first_player_list_elements or y_list == second_player_list_elements:
            print_the_board(playing_field)
            print(f'{first_or_second_player_winner(x_list, y_list, z_list)} is a winner')
            exit()
        elif z and z_list == first_player_list_elements or z_list == second_player_list_elements:
            print_the_board(playing_field)
            print(f'{first_or_second_player_winner(x_list, y_list, z_list)} is a winner')
            exit()
    # vertical
    a = all([playing_field[0][0], playing_field[1][0], playing_field[2][0]])
    b = all([playing_field[0][1], playing_field[1][1], playing_field[2][1]])
    c = all([playing_field[0][2], playing_field[1][2], playing_field[2][2]])
    a_list = [playing_field[0][0], playing_field[1][0], playing_field[2][0]]
    b_list = [playing_field[0][1], playing_field[1][1], playing_field[2][1]]
    c_list = [playing_field[0][2], playing_field[1][2], playing_field[2][2]]
    if a or b or c:
        if a and a_list == first_player_list_elements or a_list == second_player_list_elements:
            print_the_board(playing_field)
            print(f'{first_or_second_player_winner(a_list, b_list, c_list)} is a winner')
            exit()
        elif b and b_list == first_player_list_elements or b_list == second_player_list_elements:
            print_the_board(playing_field)
            print(f'{first_or_second_player_winner(a_list, b_list, c_list)} is a winner')
            exit()
        elif c and c_list == first_player_list_elements or c_list == second_player_list_elements:
            print_the_board(playing_field)
            print(f'{first_or_second_player_winner(a_list, b_list, c_list)} is a winner')
            exit()
    #diagonals left and right
    l_diagonal = all([playing_field[0][0], playing_field[1][1], playing_field[2][2]])
    r_diagonal = all([playing_field[0][2], playing_field[1][1], playing_field[2][0]])
    l_diagonal_list = [playing_field[0][0], playing_field[1][1], playing_field[2][2]]
    r_diagonal_list = [playing_field[0][2], playing_field[1][1], playing_field[2][0]]
    if l_diagonal or r_diagonal:
        if l_diagonal and l_diagonal_list == first_player_list_elements or l_diagonal_list == second_player_list_elements:
            print_the_board(playing_field)
            print(f'{first_or_second_player_winner(l_diagonal_list, r_diagonal_list)} is a winner')
            exit()
        elif r_diagonal and r_diagonal_list == first_player_list_elements or r_diagonal_list == second_player_list_elements:
            print_the_board(playing_field)
            print(f'{first_or_second_player_winner(l_diagonal_list, r_diagonal_list)} is a winner')
            exit()
    print_the_board(playing_field)


def making_move(row, col, playing_field, current_player):

    winning_flag = False
    for r in range(len(playing_field)):
        for c in range(len(playing_field)):

            if r == row and c == col and playing_field[r][c] == False:
                playing_field[row][col] = first_player.sign if current_player == first_player.name else second_player.sign
    #create here a func that will check if there is a winner
    winner_or_not(playing_field)
    return winning_flag


def creating_field_and_making_a_move():
    move_count = 1
    playing_field = [[False, False, False], [False, False, False], [False, False, False]]
    while True:

        player_move = second_player.name if move_count % 2 == 0 else first_player.name
        player_choice = input(f'{player_move} choose a free position [1-9] : ')
        row, col = making_row_col_for_choice(player_choice)
        while not player_choice_validation(player_choice, playing_field, row, col):
            print(f'{player_move} please make a correct input, or choose another position')
            player_choice = input(f'{player_move} choose a free position [1-9] : ')
            row, col = making_row_col_for_choice(player_choice)
        # to reach here the validation was success

        if making_move(row, col, playing_field, player_move):
            continue
        move_count += 1


first_player, second_player = players_input_check()
board = print_the_field()
print(f'{first_player.name} starts first!')
creating_field_and_making_a_move()
