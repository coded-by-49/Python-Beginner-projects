import time
from players import *
class Tictactoe:
    def __init__(self):
        # self.board = ["X","O","X","X"," "," ", " ", " ","O"] --> Test case
        self.board = [" " for i in range(9)]
        self.the_winner = None # keep track of winner

    def print_board(self):
        # forming a table by printing out each row
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            # key here is that you are not working with single character you are working with the whole list
            # row by row
            print(" | "+" | " .join(row)+" | ")


#learn about hashattr() in python
# learn about 2d list and matrices in python

    
    @staticmethod
    # prints out board with index, to direct human player
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(" | "+" | " .join(row)+" | ")

    def available_moves(self): 
        # fetch the avaible move
        moves = [i for i,block in enumerate(self.board) if block== " "]
        return moves
    
    def empty_square(self):
        # to check whether there the board is completed
        return (' ' in self.board) # RETURNS BOOLEAN
    
    def num_empty_squares(self): 
        return self.board.count(' ')
    
    def make_move(self, square, letter): # RETURNS A BOOLEAN
        """
        if valid move, then make the move (assign square to letter)
        #then return true. if invalid , return false
        """
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter): # checks whether the move just played was a winner
                self.the_winner = letter
            return True
        return False
    
    def winner(self, square, letter) :
        
        row_ind = square//3 # all letters on a particular row have the row ind
        # row = self.board[row_ind*3 : (row_ind+1) * 3] # you are obtaining all the indexes under that particular row
        row = [self.board[i + 3*row_ind] for i in range(3)] # you are obtaining all the indexes under that particular row
        if all ([spot == letter for spot in row]):
            return True 
        
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)] # obtaining all the indexes of the column 
        if all([spot== letter for spot in column]):
            return True
        
        if square % 2 == 0:
           diagonal1 = [self.board[i] for i in [4*j for j in range(3)]]
           if all([spot == letter for spot in diagonal1]):
               return True
           diagonal2 = [self.board[i] for i in [(2*j+2) for j in range(3)]]
           if all([spot == letter for spot in diagonal2]):
               return True  
        return False      
    
def play(game, x_player, o_player, print_game=True):
    if print_game: 
        game.print_board_nums()
    letter = "O" # starting letter
    while game.empty_square(): # iterate while the game still has empty square
        # get the move from the appropriate player
        if letter == "O":
            square = o_player.get_move(game)
        else: 
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f"makes a move to square {square}")
                game.print_board()
                print('') #just empty line
 
            if game.the_winner: # checks if game has been won
                if print_game:
                    print(letter + "wins!")
                return "This is just a statment to be "   # to end the game/loop

            # after we made our move, we needto alternter letters
            letter = 'O' if letter == 'X' else 'X'    # switches player
    if print_game:
        print("tie!")

X_WINS = 0
O_WINS = 0
TIES = 0
o_player = GeniusComputerPlayer("O")
x_player = RandomComputerPlayer("X")
for i in range (1):
    t = Tictactoe()
    play(t, x_player, o_player, print_game = False)
    if t.the_winner == "O":
        O_WINS += 1 
    elif t.the_winner == "X":
        X_WINS += 1
    else:
        TIES += 1
    print(f"genius computer = {O_WINS} \n random_computer = {X_WINS} \n Ties = {TIES}")

        
        

