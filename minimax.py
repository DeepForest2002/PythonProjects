#creating a unbeatable bot for tic tac to


board={1:' ', 2:' ', 3:' ',
       4:' ', 5:' ', 6:' ',
       7:' ', 8:' ', 9:' '}
def printboard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')
printboard(board)
def emptyplace(position):
    if board[position]==' ':
        return True

    return False
# print(emptyplace(1)) It returns false because the place is not empty
def check_draw():
    for key in board.keys():
        if board[key]==' ':
            return False #It will return false beause we cannot continue the game if there is any empty place

        else:
            return True

    pass
def check_win():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    if board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    if board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    if board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    if board[2] == board[5] and board[2] == board[5] and board[2] != ' ':
        return True
    if board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    if board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    if board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True
    else:
        return False
    pass
def insert_letter(letter,position):
    if emptyplace(position):#Checking the place if free or not
        board[position]=letter
        printboard(board)
    if check_draw():
        print("Draw")
        exit()
    if check_win():
        if letter=='X':
            print("Bot wins")
        else:
            print("Player wins")
            exit()

    else:
        print("Opps! You have entered wrong position")
        position=int(input("Please enter your position again\n"))
        insert_letter(letter,position)
        return

# print(insert_letter('X',1)) it will throw opps
player='O'
bot='X'
def player_move():
    position=int(input("Please, Enter a position for 'O':"))
    insert_letter(player,position)
    return
def computer_move():
    position=int(input("Please, Enter a position for 'X':"))
    insert_letter(bot, position)
    return
while not check_win():
    computer_move()
    player_move()