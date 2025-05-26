import random
import math
import time
class Players:
    def __init__(self, letter):
        self.letter = letter
    
    @staticmethod
    def reversed_indexes(instance_column): # provides the Forder of placement in the game
        return [7*n+instance_column for n in range(6)][::-1]
    
class Humanplayer(Players): # because of line 3&5 it automatically sets board_index to [i for i in range(42)] 
    def __init__(self, letter):
        super().__init__(letter)
    
    # let the human make his move
    def make_move(self,Connect4_instance):
        made = False
        while not made:
            try:
                column = int(input("Enter a column"))
                if column<0 or column>6:
                    raise ValueError
                column_indexes = self.reversed_indexes(column) # get the index of the column and reverse it
                if " " in [Connect4_instance.board[i] for i in column_indexes]: # checks whether column is filled or not
                    spot = Connect4_instance.implement_usermove(column_indexes,self.letter)# it drops the letter at that first unfilled spot it sees   
                    Connect4_instance.make_winner(spot,self.letter) # Check whether the move won the game
                    made = True                                             # then stop checking
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input")

class Randcomputer(Players):
    def __init__(self, letter):
        super().__init__(letter)
    
    def make_move(self,Connect4_instance):
        column = random.choice(Connect4_instance.Playable_columns()) # computer selects a random column
        column_indexes = self.reversed_indexes(column)
        spot = Connect4_instance.implement_usermove(column_indexes,self.letter)
        Connect4_instance.make_winner(spot,self.letter) # Check whether the move won the game

class Unbeatable(Randcomputer):
    def __init__(self, letter):
        super().__init__(letter)

    def print_progression(self,Connect4_instance):
        # For game progression
        for row in [Connect4_instance.board[ind*7:(ind+1)*7] for ind in range(6)]:
            print("| " + "  | ".join(row)+"  |")
        print(" ")

    def make_move(self, Connect4_instance):
        #FOR MY ORGINAL BUG HOW WOULD I HAVE KNOWN, THAT IT WAS COMING FROM HERE
        if "X" not in Connect4_instance.board and "O" not in Connect4_instance.board:
            super().make_move(Connect4_instance)
        else:
            _copy_ = Connect4_instance.copy()
            column = self.minimax(_copy_,self.letter)["position"] 
            column_indexes = self.reversed_indexes(column)
            spot = Connect4_instance.implement_usermove(column_indexes,self.letter)
            Connect4_instance.make_winner(spot,self.letter) # Check whether the move won the game

    def minimax(self,Connect4_instance,current_player, alpha = -math.inf, beta = math.inf):
        maxed_player = self.letter # this is the letter of the unbeatable computer
        #now we want to know which player we are minimizing and maximizing 
        former_player = "O" if current_player == "X" else "X"

        # (BASECASE) This determines whether a new state should be made or not and if not, what is the score of the winner state
        if Connect4_instance.winner == former_player:
            return {
                "position": None, "score": (Connect4_instance.num_empty_squares()+1) if former_player == maxed_player
                else -1*(Connect4_instance.num_empty_squares()+1)
            }
        elif Connect4_instance.available_spot() == False:
            return{
                  "position": None, "score": 0
            }
          
        # this creates the value of intial fathers states- either for a maximiser / minimiser state
        if current_player == maxed_player:
            current_best = {"position": None, "score":-math.inf}
        else:
            current_best = {"position": None, "score":math.inf}

        for possible_column in Connect4_instance.Playable_columns():
            # make the father move
            copy_instance = Connect4_instance.copy() # making a copy to avoid recursion curse
            column_indexes = self.reversed_indexes(possible_column)
            spot = copy_instance.implement_usermove(column_indexes,current_player) # implementing a move on the copied board 
            # time.sleep(0.3) !!!!!
            copy_instance.make_winner(spot,current_player) # Check and implement a win if there is 
           
            #recurse and create its children
            sim_score = self.minimax(copy_instance,former_player,alpha, beta)
            sim_score["position"] = possible_column

            #this is were the father picks a child(the first formed child), retains him or replaces him , after comparison with his siblings
            if current_player == maxed_player:
                if sim_score["score"] > current_best["score"]: # here we maximise
                    current_best = sim_score
                    alpha = max(current_best["score"],alpha)
                if alpha >= beta: 
                    break
            else:
                if sim_score["score"] < current_best["score"]: # here minimise
                    current_best = sim_score
                    beta= min(current_best["score"],beta)
                if beta <=  alpha:
                    break
        return current_best # we are returning this, because at the very top you need the actual move that lead to the most optimal score
