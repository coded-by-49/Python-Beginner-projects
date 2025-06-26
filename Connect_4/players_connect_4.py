import random
import math

class Players:
    def __init__(self, letter):
        self.letter = letter
    
    @staticmethod
    def reversed_indexes(instance_column):
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
                    made = True                                            # then stop checking
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
        Connect4_instance.make_winner(spot,self.letter) # Check whether the move won the game and make the computer a winner

class Unbeatable_ai(Randcomputer):
    def __init__(self, letter):
        super().__init__(letter)

    def make_move(self, Connect4_instance):
        if "X" not in Connect4_instance.board and "O" not in Connect4_instance.board:
            super().make_move(Connect4_instance)
        else:
            _copy_ = Connect4_instance.copy()
            column = self.minimax(_copy_,self.letter,depth=5)["position"] 
            column_indexes = self.reversed_indexes(column)
            spot = Connect4_instance.implement_usermove(column_indexes,self.letter)
            Connect4_instance.make_winner(spot,self.letter)

    def minimax(self,Connect4_instance,current_player,depth, alpha = -math.inf, beta = math.inf):
        maxed_player = self.letter # assign whatever letter that is choosen by our unbeatiable ai 

        former_player = "O" if current_player == "X" else "X"

        # BASECASE --> this is where our recursion stops
        if Connect4_instance.winner == former_player:
                return {
                    "position": None, "score": 1000*(Connect4_instance.num_empty_squares()+1) if former_player == maxed_player
                    else -1000*(Connect4_instance.num_empty_squares()+1)
                }
        elif Connect4_instance.available_spot() == False:
                return{
                        "position": None, "score": 0
                }
        elif (depth == 0):
                return{
                    "position":None, "score": Connect4_instance.heuristic_eval(maxed_player , opp = "O" if maxed_player== "X" else "X") 
                }
        
        # our score key is going to be used for evaluatio and our position key is going to be used to track our postion 
        if current_player == maxed_player:
            current_best = {"position": None, "score":-math.inf}
        else:
            current_best = {"position": None, "score":math.inf}

        for column_played in Connect4_instance.Playable_columns():
            copy_instance = Connect4_instance.copy() # making a copy to avoid recursion curse
            column_indexes = self.reversed_indexes(column_played)
            spot = copy_instance.implement_usermove(column_indexes,current_player) # implementing a move on the copied board 
            # time.sleep(0.3) !!!!!
            copy_instance.make_winner(spot,current_player) # Check and implement a win if there is 
           
            #recurse and create its children, reduce thte depth by 1 each time this happens 
            sim_score = self.minimax(copy_instance,former_player,depth-1, alpha, beta) # this is where the score from the feasible child node is captured
            sim_score["position"] = column_played # the parent board_state that lead to the move will house a single score from children

            # 
            if current_player == maxed_player:
                if sim_score["score"] > current_best["score"]: # here we maximise (we)
                    current_best = sim_score
                    alpha = max(current_best["score"],alpha)
                if alpha >= beta: 
                    break
            else:
                if sim_score["score"] < current_best["score"]: # here minimise
                    current_best = sim_score
                    beta= min(current_best["score"],beta)
                if alpha >= beta:
                    break
        return current_best # we are returning this so that the parent move gets score of each chil node
