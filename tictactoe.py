import os

win_conditions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def print_board():
    print("""

                      \t\t  {0} | {1} | {2}
                    \t\t-------------
                      \t\t  {3} | {4} | {5}
                    \t\t-------------
                      \t\t  {6} | {7} | {8}

             """.format(*board))


def clear():
    return os.system('cls')


playing = True
while playing:
    clear()
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('\x1b[6;30;42m' + '\n       LETS PLAY TIC-TAC-TOE        \n' + '\x1b[0m')
    print('Enter the number to play (1-9)')

    print_board()
    player1 = input('Enter Player1 name ( X ) : ' + '\033[94m')
    print('\033[0m')
    player2 = input('Enter Player2 name ( O ) : ' '\033[94m')
    print('\033[0m')
    if player1 == player2:
        player2 += '_2'
    if not player1:
        player1 = 'Player1'
    if not player2:
        player2 = 'Player2'
    # board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    turn = 1
    clear()
    player1_box = []
    player2_box = []

    def check_turn():
        global turn
        if turn % 2 == 1:
            return player1
        else:
            return player2

    def win_checker():
        for z in win_conditions:
            if z[0] in player1_box and z[1] in player1_box and z[2] in player1_box:
                print('\33[32m' + f'\n \t\t\t\t {player1} wins \n \n' + '\33[0m')
                return 1
            elif z[0] in player2_box and z[1] in player2_box and z[2] in player2_box:
                print('\33[32m' + f'\n \t\t\t\t {player2} wins \n \n' + '\33[0m')
                return 1

    print_board()
    for game in range(9):

        if 1 == win_checker():
            break
        try:
            choice = int(input(f'{check_turn()}\'s turn : '))
            if choice not in player2_box and choice not in player1_box:

                if check_turn() == player1:
                    board[choice - 1] = '\33[91mX\33[0m'
                    player1_box.append(choice)

                else:
                    board[choice - 1] = '\33[93mO\33[0m'
                    player2_box.append(choice)

                turn += 1
            else:
                print('Invalid input. Game ended')
                break
        except Exception:
            print('Invalid input.Game ended')
            break
        clear()
        print_board()
        if game >= 8:
            print('\33[3m' + 'Game Drawn' + '\33[0m')
    playing = int(input('Do you want to play again? 0 or 1: '))
