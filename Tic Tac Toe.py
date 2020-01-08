#Michael Calhoun
#Tic Tac Toe
#11/19

#Global Constants
X = "X"
O = "O"
NUM_SQUARES = 9
TIE = "TIE"
EMPTY = " "

#working 
def instructions():
    """Display Game Instructions."""
    print(
        """
        Welcome to Tic-Tac-Toe you will be enetering a number 1-9.
        The number will correspond to the board position as illustrated:

                    1 | 2 | 3
                    ---------
                    4 | 5 | 6
                    ---------
                    7 | 8 | 9
                    
        Prepare yourself, you will be playing against a computer :). \n
        """
        )

def ask_yes_no(question):
    response = None
    while response not in ("y","yes","no","n"):
        response = input(question).lower()
    x = response[0]
    return x

#working
def new_board():
    board = []
    for i in range (NUM_SQUARES):
        board.append(EMPTY)
    return board

#board = new_board()
#print(board)

# Working
def display_board(board):
    print(str.format("""
                    {0} | {1} | {2}
                    ---------
                    {3} | {4} | {5}
                    ---------
                    {6} | {7} | {8}
                    """,board[0],board[1],board[2],
                        board[3],board[4],board[5],
                        board[6],board[7],board[8]))

#board = new_board()
#board [4] = X
#display_board(board)
#board [0] = X
#display_board(board)
#board [8] = X
#display_board(board)

# Working
def pieces():
    go_first = ask_yes_no("do you want to go first? (y/n) ")
    if go_first == "y":
        human = X
        comp = O
    else:
        comp = X
        human = O
    return comp,human

#comp, human = pieces()
#print(comp)
#print(human)

# Working
def ask_number(question, low, high):
    response = -1
    while response not in range(low,high):
        try:
            response = int(input(question))
        except:
            print("thats not a number")
            
    return response

#x = ask_number("pick a number between 1 and 5",0,5)
#print(x)

# Working
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board [square] == EMPTY:
            moves.append(square)
    return moves

#board = new_board()
#moves = legal_moves(board)
#print(moves)

# Working
def human_move(board,human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where would you like to move? (1 - 9):",1,NUM_SQUARES+1)-1
        if move not in legal:
            print("\nFoolish Mortal Thats Not An Option.\n")
    print("Fine...")
    return move

#board = new_board()
#move = human_move(board,X)
#print (move)

# Working
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

#turn = X
#print(turn)
#turn = next_turn(turn)
#print(turn)

# Working?
def winner(board):
    """Determine the winner.""" #<---- Doc String
    WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    
    return None


#board = new_board()
#board[6] = O
#board[7] = O
#board[8] = O
#x = winner(board)
#print (x)

def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's A TIE!\n")
    if the_winner == computer:
        print("Ha No Mortal Can Beat Me!\n")
    elif the_winner == human:
        print("You Are Lucky This Time Mortal But Next Time You Wont Be!\n")

def comp_move(board,human,computer):
    #make a copy of the board
    board_copy = board[:]
    #best spots for the computer
    if computer == X:
        BEST_MOVES = (8,0,6,7,2,1,4,5,3)
    if computer == O:
        BEST_MOVES =(4,0,2,6,8,1,3,5,7)
        
    
    print("I Choose Square Number", end= " ")
    #if computer can win take that move
    for move in legal_moves(board):
        board_copy[move] = computer
        if winner(board_copy) == computer:
            print(move+1) 
            return move
        
        board_copy[move] = EMPTY
    #if human can win block that move    
    for move in legal_moves(board):
        board_copy[move] = human
        if winner(board_copy) == human:
            print(move+1)
            return move
    
        board_copy[move] = EMPTY
    #pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move+1)
            return move


def game():
    instructions()
    comp, human = pieces()
    board = new_board()
    turn = X
    display_board(board)
    win = winner(board)
    while win == None:
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = comp_move(board,human,comp)
            board[move] = comp
        display_board(board)
        turn = next_turn(turn)
        win = winner(board)
        
    
    congrat_winner(win, comp, human)
game()
    

    
        
    

#board = new_board()
#board[0] = X
#board[1] = O
#x = comp_move(board,O,X)
#print(x)

