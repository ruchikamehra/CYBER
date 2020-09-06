def tictac(board):
    count=0
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")
    player1 = input("enter your choice 'X' or 'O'")
    if (player1 == 'X'):
        player2 = 'O'
    elif (player1 == 'O'):
        player2 = 'X'
    for i in range(0,5):
         choice=int(input("player1 enter your choice"))
         if(board[choice]=='#'):
                 board[choice] = 'X'
                 count += 1
         else:
                 print("That place is already filled.\nMove to which place?")
                 continue
         if(count>=5):
             if board[1] == board[2] == board[3] == 'X':
                 return ("player1 wins")
             if board[1] == board[4] == board[7] == 'X':
                 return("player1 wins")
             if board[2] == board[5] == board[8] == 'X':
                 return("player1 wins")
             if board[3] == board[6] == board[9] == 'X':
                 return("player 1 wins")
             if board[1] == board[5] == board[9] == 'X':
                 return("player 1 wins")
             if board[3] == board[5] == board[7] == 'X':
                 return("player1 wins")
         choice2=int(input("enter your choice player 2"))
         if (board[choice2]=='#'):
                 board[choice2] = 'O'
                 count += 1
         else:
                 print("That place is already filled.\nMove to which place?")
                 continue
         if(count>=5):
             if board[1] == board[2] == board[3] == 'O':
                return ("player2 wins")
             if board[1] == board[4] == board[7] == 'O':
                return ("player2 wins")
             if board[2] == board[5] == board[8] == 'O':
                return ("player2 wins")
             if board[3] == board[6] == board[9] == 'O':
                return ("player 2wins")
             if board[1] == board[5] == board[9] == 'O':
                return ("player 2 wins")
             if board[3] == board[5] == board[7] == 'O':
                return ("player2wins")
         if(count==9):
             return("draw match")
board=["#"]*10
print(tictac(board))