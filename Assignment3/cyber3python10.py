board={ '1':' ','2':' ','3':' ',
        '4':' ','5':' ','6':' ',
        '7':' ','8':' ','9':' ',
      }
count=0
player=1
end_check=0
def wonloose(player1,player2):
    if board['1'] == board['2'] == board['3'] == player1:
        print('player one won!')
        return 1
    if board['4'] == board['5'] == board['6'] == player1:
        print('player one won!')
        return 1
    if board['7'] == board['8'] == board['9'] == player1:
        print('player one won!')
        return 1
    if board['1'] == board['5'] == board['9'] == player1:
        print('player one won!')
        return 1
    if board['3'] == board['5'] == board['7'] == player1:
        print('player one won!')
        return 1
    if board['1'] == board['4'] == board['7'] == player1:
        print('player one won!')
        return 1
    if board['2'] == board['5'] == board['8'] == player1:
        print('player one won!')
        return 1
    if board['3'] == board['6'] == board['9'] == player1:
        print('player one won!')
        return 1

        # to check if player two has won
    if board['1'] == board['2'] == board['3'] == player2:
        print('player two won!')
        return 1
    if board['4'] == board['5'] == board['6'] == player2:
        print('player two won!')
        return 1
    if board['7'] == board['8'] == board['9'] == player2:
        print('player two won!')
        return 1
    if board['1'] == board['5'] == board['9'] == player2:
        print('player two won!')
        return 1
    if board['3'] == board['5'] == board['7'] == player2:
        print('player two won!')
        return 1
    if board['1'] == board['4'] == board['7'] == player2:
        print('player two won!')
        return 1
    if board['2'] == board['5'] == board['8'] == player2:
        print('player two won!')
        return 1
    if board['3'] == board['6'] == board['9'] == player2:
        print('player two won!')
        return 1
    return 0
print('1| 2 | 3')
print("___|___|___")
print('4 | 5 | 6')
print("___|___|___")
print('7 | 8 | 9')
print("   |   |   ")
print("****************")
player1 = input("enter your choice 'X' or 'O'")
if (player1 == 'X'):
        player2 = 'O'
elif (player1 == 'O'):
    player2 = 'X'
while True:
        print(" " + board["1"] + " | " + " " + board["2"] + "| " + " " + board["3"] + " ")
        print('_|_|_')
        print(" " + board["4"] + " | " + " " + board["5"] + "| " + " " + board["6"] + " ")
        print('_|_|_')
        print(" " + board["7"] + " | " + " " + board["8"] + "| " + " " + board["9"] + " ")
        print('   |   |   ')
        print('*****************')
        end_check = wonloose(player1, player2)
        if count == 9 or end_check == 1:
            break
        while True:
            if player == 1:
                p1 = input("player one's turn")
                if p1 in board and board[p1] == ' ':
                    board[p1] = player1
                    player = 2
                    break
                else:
                    print('wrong input!, enter value again')
                    continue
            else:
                p2 = input("player two's turn")
                if p2 in board and board[p2] == ' ':
                    board[p2] = player2
                    player = 1
                    break
                else:
                    print('wrong input!, enter value again')
            count += 1
            print("*************")
