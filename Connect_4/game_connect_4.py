import time
from players_connect_4 import Humanplayer,Randcomputer,Unbeatable_ai,Players
class Connect4:
    def __init__(self, board = None, winner = None, depth = None):
        self.board = board if board is not None else [" " for i in range(42)]  
        self.winner = winner 
        self.depth = depth

    def copy(self):
        return Connect4(board= self.board.copy(), winner = self.winner, depth = self.depth) # we are returning an instance, that will have the exact state of the connect4

    @staticmethod
    def print_board_indexes(): # this is to visualize the board when the game starts
        board_slots= ["  " for i in range(35)]
        column_numbers = [str(i).zfill(2) for i in range(7)] # Add leading zeros for uniform width
        print("| " + " | ".join(column_numbers) + " |") # representing playable columns
        for row in [board_slots[ind*7:(ind+1)*7] for ind in range(5)]: # looping through the list , housing the  list of each row
            print("| " + " | ".join(row) + " |")

    def print_progression(self): 
        for row in [self.board[ind*7:(ind+1)*7] for ind in range(6)]:
            print("| " + "  | ".join(row)+"  |")
        print(" ")

    def available_spot(self): 
        # to check if there are available spots
        return " " in self.board
    
    def num_empty_squares(self):
        # to check for empty spaces in the bo
        return self.board.count(" ")
    
    def Playable_columns(self):
        # return a list of columns that has a playable spot in it
        return [i for i in range(7) if any(self.board[7*n+i] == " " for n in range(6))]
        

    def implement_usermove(self, column_indexes,letter):
        for i in column_indexes:
            if self.board[i] == " ": # this is checking for the first unoccupied index within the column, to drop the letter
                self.board[i] = letter
                return i
            
    def check_for_diagonal_win(self,diagonal,letter):
        starting_point = 0 #start from index o
        while starting_point <= (len(diagonal)-4): # then loop till you obtain any possible win in the diagonal
            if all (spot == letter for spot in diagonal[starting_point:starting_point+4]):
                self.winner = letter 
                return True
            starting_point += 1

    def make_winner(self,spot,letter):
        col_ind = spot %7 # find the col where spot lies (0-6)
        row_position = spot//7 # find row were spot  lies (0-5)

        #row check
        starting_point = max(0,col_ind-3)  #this determines where our window starts from 
        list_to_check = min(col_ind+1,7-col_ind) # this is the number of windows we would have to look at from the starting point

        for _ in range(list_to_check):
            if all (self.board[(7*row_position)+index] == letter for index in range(starting_point,starting_point+4)): # finding  a possible winner window in the row
                self.winner = letter 
                return True # we have a winner
            starting_point += 1 # increment, to move to the next window
        
        # column check
        if row_position<=2: # check if move is worth a cloumn check 
            next_spot = spot # initiate succeding spot
            if all(self.board[next_spot := next_spot+7]==letter for _ in range(3)): # check for the next three spots after that
                self.winner = letter        # choose your winner
                return True             # break function
            
        # left diagonal check
        if spot not in [0, 1, 2, 7, 8, 14, 27, 33, 34, 39, 40, 41]:
            succeding_rows_LD = row_position  #  used to move to the row of the next diagonal spot
            preceding_rows_RD = row_position  #  used to move to the row of the preceeding diagonal spot
            successor_LD = spot  # INCREMENT FROM 6
            predecessor_LD = spot  # DECREMENT FROM 6
            succeedings_LD = [self.board[spot]] # house all feasible succeeding diagonal spots
            preceedings_LD = [] # house all feasible preceeding diagonal spots
            while True:
                successor_LD += 6 ; succeding_rows_LD += 1 # we are moving foward from one diagonal spot to another
                if succeding_rows_LD <= 5 and successor_LD in [self.board[7 * succeding_rows_LD + i] for i in range(7)]:  # the first condition is to make sure we dont go beyond our board # the second is to check if the nextspot(successor_RD), is in the nest row
                    succeedings_LD.append(self.board[successor_LD]) # then we add it to the feasible succeedings row for our check
                    continue  #  skip the rest of the code block until you have exhausted the first condition, so we can't ALL possible succeeding row
                
                # we do the same but backward
                predecessor_LD -= 6; preceding_rows_RD -= 1 #we are moving backwared from one diagonal spot to another
                if preceding_rows_RD >= 0 and predecessor_LD in [self.board[7 * preceding_rows_RD + i] for i in range(7)]:
                    preceedings_LD.append(self.board[predecessor_LD])
                    continue
                break
            diagonal = preceedings_LD[::-1] + succeedings_LD # we are placing our preceedings_LD in normal order and joining it with the succeedings_LD , that way we have our full diaganal
            if self.check_for_diagonal_win(diagonal, letter):  # check for winner
                return True  # to end any possible checks after
       
        # right diagonal check
        if spot not in [4,5,6,12,13,20,35,36,37,28,29,21]:
            succeding_rows_RD = row_position  
            preceeding_rows_RD = row_position  
            successor_RD = spot # INCREMENT FROM 8
            predecesor_RD = spot# DECREMENT FROM 8
            succeedings_RD = [self.board[spot]]
            precedings_RD = []
            while  True:
                successor_RD += 8 ; succeding_rows_RD += 1
                if succeding_rows_RD<=5 and successor_RD in [self.board[7*succeding_rows_RD+i] for i in range(7)]: 
                    succeedings_RD.append(self.board[successor_RD]) 
                    continue 
                predecesor_RD -= 8; preceeding_rows_RD -= 1
                if preceeding_rows_RD>=0 and predecesor_RD in [self.board[7*preceeding_rows_RD+i] for i in range(7)]:
                    precedings_RD.append(self.board[predecesor_RD])
                    continue
                break
            if self.check_for_diagonal_win(precedings_RD[::-1]+succeedings_RD,letter):
                return True
            

    def heuristic_eval(self,Ai,opp):
        # to evaluate the state of a board when it reaches its maximum depth in our minimax algorithm 
        score = 0
        for col in range(-7,0): # we use negative becausse because of the walrius operator below
            current_column = [self.board[col := col+7] for i in range(6)] # access all the members of each column
            slice_start,slice_stop = 0,4 # starting window
            for i in range(3): # 3 because this is the maximum numbers of windows we can get
                current_window  = current_column[slice_start:slice_stop]
                if current_window.count(Ai) == 3 and current_window.count(opp) == 0:
                    score += 150
                elif current_window.count(Ai) == 2 and current_window.count(opp) == 0:
                    score += 75
                elif current_window.count(Ai) == 1 and current_window.count(opp) == 0:
                    score += 10
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 3:
                    score -= 150
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 2:
                    score -= 75
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 1:
                    score -= 10 
                slice_start, slice_stop = slice_start+1,slice_stop+1 

        # row check
        row_start,row_stop = 0,7
        for row in range(6):
            current_row = self.board[row_start:row_stop] # we access rows this way, because their indecies are linear e.g 7,8,9...13
            slice_start,slice_stop = 0,4
            for i in range(4):
                current_window  = current_row[slice_start:slice_stop]
                if current_window.count(Ai) == 3 and current_window.count(opp) == 0:
                    score += 150
                elif current_window.count(Ai) == 2 and current_window.count(opp) == 0:
                    score += 75
                elif current_window.count(Ai) == 1 and current_window.count(opp) == 0:
                    score += 10
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 3:
                    score -= 150
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 2:
                    score -= 75
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 1:
                    score -= 10 
                slice_start, slice_stop = slice_start+1,slice_stop+1
            row_start += 7
            row_stop += 7

        # right diagonal check 
        RD_outsiders = [4,5,6,12,13,20,35,36,37,28,29,21] # these are the edge cases 
        RD_start_num = [0,1,2,3,7,14] # these are the start 
        
        for i in RD_start_num:
            current_diagonal = [self.board[i]]
            while i+8 not in RD_outsiders and i+8 <= 41: # we iterate until we obtain all the values withing a paricular diagonal
                i += 8
                current_diagonal.append(self.board[i])  # we store that in the correct diagonal we are working with 
            slice_start,slice_stop = 0,4
            while slice_stop<=len(current_diagonal):
                current_window  = current_diagonal[slice_start:slice_stop]
                if current_window.count(Ai) == 3 and current_window.count(opp) == 0:
                    score += 150
                elif current_window.count(Ai) == 2 and current_window.count(opp) == 0:
                    score += 75
                elif current_window.count(Ai) == 1 and current_window.count(opp) == 0:
                    score += 10
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 3:
                    score -= 150
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 2:
                    score -= 75
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 1:
                    score -= 10 
                slice_start, slice_stop = slice_start+1,slice_stop+1

        # left diagonal check
        LD_outsiders = [0, 1, 2, 7, 8, 14, 27, 33, 34, 39, 40, 41]
        LD_start_num = [3,4,5,6,13,20]
        
        for i in LD_start_num:
            current_diagonal = [self.board[i]]
            while i+6 not in LD_outsiders and i+6 < 41:
                i += 6
                current_diagonal.append(self.board[i])  
            slice_start,slice_stop = 0,4
            while slice_stop<=len(current_diagonal):
                current_window  = current_diagonal[slice_start:slice_stop]
                if current_window.count(Ai) == 3 and current_window.count(opp) == 0:
                    score += 150
                elif current_window.count(Ai) == 2 and current_window.count(opp) == 0:
                    score += 75
                elif current_window.count(Ai) == 1 and current_window.count(opp) == 0:
                    score += 10
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 3:
                    score -= 150
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 2:
                    score -= 75
                elif current_window.count(Ai) == 0 and current_window.count(opp) == 1:
                    score -= 10 
                slice_start, slice_stop = slice_start+1,slice_stop+1
                
        return score
                
        

def play(game,player1,player2,display):
    if display: #decide whether you want the board interface to appear
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
for i in range(10):
    player2 = Randcomputer("O") #the computer class contains an instance variable therefore it is defined within the loop 
    player1 = Unbeatable_ai("X")
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