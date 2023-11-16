import random

player_symbol = ' '    #Эти две переменные будут хранить данные о символе игрока и компьютера после ввода пользователем значения
computer_symbol = ' '

def draw_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def check_win(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def get_player_move(board, player):
    while True:
        position = int(input('На какую позицию хотите поставить символ? Счет клеток начинается с нуля: '))
        if board[position] == " ":
            break
        else:
            print('Эта позиция уже занята')
            continue
    board[position] = player
    return board

def get_computer_move(board, player):
    while True:
        position = random.randint(0, 8)
        if board[position] == " ":
            break
        elif " " not in board:
            break
        else:
            continue
    board[position] = player
    return board

def main():
    repeater = '+'      #переменная создает цикл, внутри которого пользователь может продолжать играть, не завершая работу программы
    while repeater == '+':
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        global player_symbol
        global computer_symbol
        player_symbol = input('Введите символ за который будете играть: ')

        if player_symbol == "X":   #поскольку крестики ходят первыми по правилу, то здесь выполняется блок кода, где крестики стартуют
            computer_symbol = "O"
            while True:
                draw_board(board)
                get_player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    print('******************************')
                    print('Вы победили!')
                    break
                get_computer_move(board, computer_symbol)
                if check_win(board, computer_symbol):
                    print('******************************')
                    print('Победил компьютер!')
                    break
                if " " not in board:
                    print('******************************')
                    print('Похоже, ничья!')
                    break
            draw_board(board)
            print('******************************')
            print('Вот как выглядит поле теперь')
            repeater = input('Хотите сыграть еще раз? Если да - введите +')

        elif player_symbol == "O":     #аналогичная ситуация, но компьютер ходит первым
            computer_symbol = "X"
            while True:
                get_computer_move(board, computer_symbol)
                if check_win(board, computer_symbol):
                    print('******************************')
                    print('Победил компьютер!')
                    break
                draw_board(board)
                print('******************************')
                if " " not in board:
                    print('******************************')
                    print('Похоже, ничья!')
                    break
                get_player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    print('******************************')
                    print('Вы победили!')
                    break
                draw_board(board)
                print('******************************')
                if " " not in board:
                    print('******************************')
                    print('Похоже, ничья!')
                    break
            draw_board(board)
            print('******************************')
            print('Вот как выглядит поле теперь')
            repeater = input('Хотите сыграть еще раз? Если да - введите + ')

main()
