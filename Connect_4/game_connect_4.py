import time
from players_connect_4 import Humanplayer,Randcomputer,Unbeatable,Players
# Try developing an alogorithm to stop a game when a win is no longer possible
class Connect4:
    def __init__(self, board = None, winner = None):
        # self.board = board if board is not None else [" " for i in range(42)]  
        self.board = board if board is not None else [
            # Row 0 (Top) - Only columns 1, 3, 5 empty
            " ", " ", " ", " ", " ", " ", " ",
            "O", " ", " ", " ", " ", " ", " ",  # Row 1
            "X", "O", "O", "X", "X", "O", " ",  # Row 2
            "O", "X", "X", "O", "X", "X", "O",  # Row 3
            "X", "O", "O", "X", "X", "O", "O",  # Row 4
            "O", "X", "X", "O", "O", "X", "X"   # Row 5 (Bottom)
            ]
        self.winner = winner 

    def copy(self):
        return Connect4(board= self.board.copy(), winner = self.winner) # we are returning an instance, that will have the exact state of the connect4

    @staticmethod
    def print_board_indexes(): # game starter
        board_slots= ["  " for i in range(35)]
        column_numbers = [str(i).zfill(2) for i in range(7)] # Add leading zeros for uniform width
        print("| " + " | ".join(column_numbers) + " |") # representing playable columns
        for row in [board_slots[ind*7:(ind+1)*7] for ind in range(5)]: # looping through the list , housing the  list of each row
            print("| " + " | ".join(row) + " |")

    def print_progression(self):
        # For game progression
        for row in [self.board[ind*7:(ind+1)*7] for ind in range(6)]:
            print("| " + "  | ".join(row)+"  |")
        print(" ")

    def available_spot(self): 
        # to check if there are available spots
        return " " in self.board
    
    def num_empty_squares(self):
        return self.board.count(" ")
    
    def Playable_columns(self):
        return [i for i in range(7) if any(self.board[7*n+i] == " " for n in range(6))]
        

    def implement_usermove(self, column_indexes,letter): # takes a reversed list of the indecies
        for i in column_indexes:
            if self.board[i] == " ": # this is checking for the first unoccupied index within the column, to drop the letter
                self.board[i] = letter
                return i
            
    def looping_through(self,row,letter):
        starting_point = 0 #start from index o
        while starting_point <= (len(row)-4): # then loop till you obtain all the possible win in the column or row
            if all (spot == letter for spot in row[starting_point:starting_point+4]):
                self.winner = letter 
                return True
            starting_point += 1

    def make_winner(self,spot,letter):
        board = [i for i in range(42)]
        col_ind = spot %7
        row_position = spot//7 # find row were spot  lies

        #row check
        starting_point = max(0,col_ind-3)  # this is where list should start generating from , depending on the col_index
        list_to_check = min(col_ind+1,(7-col_ind)) # this is the number of 4-seg list that should be generated depending on 
        # row = [self.board[(7*row_position)+i] for i in range(7)] # obtian all indicies on row
        for _ in range(list_to_check):#iterate through row
            if all (self.board[(7*row_position)+i] == letter for i in range(starting_point,starting_point+4)): #try using a lazy format
                self.winner = letter 
                return "won" #break function
            starting_point += 1
        
        # column check
        if row_position<=2: # check if move is worth a cloumn check 
            next_spot = spot # intiate succeding spot
            if all(self.board[next_spot := next_spot+7]==letter for _ in range(3)): # check for the next three spots after that
                self.winner = letter        # choose your winner
                return "won"             # break function
            
        # left diagonal check
        if spot not in [0, 1, 2, 7, 8, 14, 27, 33, 34, 39, 40, 41]:
            row_position_LD = row_position  # lets make a copy of the row_position
            preceding_row = row_position_LD  # obtain succeeding row
            successor_LD = spot  # INCREMENT FROM 6
            predecessor_LD = spot  # DECREMENT FROM 6
            succeedings_LD = [self.board[spot]]
            precedings_LD = []
            while True:
                successor_LD += 6
                row_position_LD += 1
                if row_position_LD <= 5 and successor_LD in [self.board[7 * row_position_LD + i] for i in range(7)]:  # iterating forward from the spot within its diagonal
                    succeedings_LD.append(self.board[successor_LD])
                    continue  # skip the rest of the code block until you have exhausted the if statement

                predecessor_LD -= 6
                preceding_row -= 1
                if preceding_row >= 0 and predecessor_LD in [self.board[7 * preceding_row + i] for i in range(7)]:
                    precedings_LD.append(self.board[predecessor_LD])
                    continue
                break
            if self.looping_through(precedings_LD[::-1] + succeedings_LD, letter):  # check for winner
                return "won"  # to end any possible checks after
       
        # right diagonal check
        if spot not in [4,5,6,12,13,20,35,36,37,28,29,21]:
            succeding_rows_RD = row_position  # used to check validity of the next row
            preceeding_rows_RD = row_position  # used to check validity of the previous row
            successor_RD = spot # INCREMENT FROM 8
            predecesor_RD = spot# DECREMENT FROM 8
            succeedings_RD = [self.board[spot]]
            precedings_RD = []
            while  True:
                successor_RD += 8 
                succeding_rows_RD += 1
                if succeding_rows_RD<=5 and successor_RD in [self.board[7*succeding_rows_RD+i] for i in range(7)]: # iterating forward from the spot within its diagonal
                    succeedings_RD.append(self.board[successor_RD]) # 
                    continue # skip the rest of the code block until you have exhausted the if statement
                predecesor_RD -= 8
                preceeding_rows_RD -= 1
                if preceeding_rows_RD>=0 and predecesor_RD in [self.board[7*preceeding_rows_RD+i] for i in range(7)]:
                    precedings_RD.append(self.board[predecesor_RD])
                    continue
                break
            if self.looping_through(precedings_RD[::-1]+succeedings_RD,letter): # check for winner
                return "won" # to end any possible checks after
            

def play(game,player1,player2,display):
    if display: #decide whether you want a ui interface
        game.print_board_indexes()
        print(" ")
    current_player = player1
    while game.available_spot(): # play as long as there is an available spot
        current_player.make_move(game)
        if display:
            game.print_progression()
            print(" ")
        if game.winner: # end game once there is a winner
            if display:
                print(f"{game.winner} player has won the game")
                print(" ")
            return "Ended"
        current_player = player1 if current_player == player2 else player2
    if display:
        print("it is a tie")


player1_W = 0
player2_W = 0
Tie = 0

start = time.perf_counter()
for i in range(1):
    player2 = Randcomputer("O") #the computer class contains an instance variable therefore it is defined within the loop 
    player1 = Unbeatable("X")
    Con4 = Connect4()
    play(Con4,player1,player2,display = False)
    if Con4.winner == "X":
        player1_W += 1
    elif Con4.winner == "O":
        player2_W += 1
    else:
        Tie += 1
end = time.perf_counter()


print(f"x won {player1_W}\n o won {player2_W} \n tied {Tie}")
print(f"fime take : {end - start:.4f} seconds")