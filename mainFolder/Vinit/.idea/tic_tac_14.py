import random
def tic():
    lis=['']*9
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = (( 1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 6, 9), (2, 5, 8), (3, 4, 7), (1, 5, 7), (3, 5, 8))


    def who():
        a=input("who will play first?")
        return a

    def tic_tac():
        print('   |   |')
        print(' ' + lis[7] + ' | ' + lis[8] + ' | ' + lis[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + lis[4] + ' | ' + lis[5] + ' | ' + lis[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + lis[1] + ' | ' + lis[2] + ' | ' + lis[3])
        print('   |   |')

    def inputPlayerLetter():
          letter = ''
          while not (letter == 'X' or letter == 'O'):
              print('Do you want to be X or O?')
              letter = input().upper()


    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = "X"


    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p2()
        else:
            board[n] = "O"


        def check_board():
            count = 0
            for a in win_commbinations:
                if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                    print("Player 1 Wins!\n")
                    print("Congratulations!\n")
                    return True

                if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                    print("Player 2 Wins!\n")
                    print("Congratulations!\n")
                    return True
            for a in range(9):
                if board[a] == "X" or board[a] == "O":
                    count += 1
                if count == 9:
                    print("The game ends in a Tie\n")
                    return True
        while not end:
            draw()
            end = check_board()
            if end == True:
                break
            print("Player 1 choose where to place a cross")
            p1()
            print()
            draw()
            end = check_board()
            if end == True:
                break
            print("Player 2 choose where to place a nought")
            p2()
            print()

        if input("Play again (y/n)\n") == "y":
            print()
            tic_tac_toe()

tic()