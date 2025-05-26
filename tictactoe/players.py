import math
import random
import time
import copy
# from game import print_board
class Player:
    def __init__(self,letter):
        # letter is x or o
        self.letter = letter
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter) 

    def get_move(self, game):
        #getting a random valid spot for our next move
        square = random.choice(game.available_moves()) # HOW DID IT GET ACCESS TO THIS
        return square
    
class HumanPlayer(Player): 
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self, game):
        valid_square = False
        val = None
        # what will be the breaker of this loop
        while not valid_square:
            square = input(self.letter+'\'s turn. input move (0-8):')
            # we are going to check whether this is a valid input
            # by trying to cast it to an integer, and if it is not 
            # , then we say its invalid and if the spot isn;t avaiable on this 
            # board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("invalid square, try agian")
        return val 
class GeniusComputerPlayer(Player):
    def _init_(self,letter):
        super()._init_(letter)

    def get_move(self,game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #get the sqaure based off the minimax algorithm
            square = self.minimax(game, self.letter)["position"]
        return square
    

    def minimax(self, state, Current_player, alpha = -math.inf, beta = math.inf):
        max_player = self.letter #refering to what ever letter the AI is using to play
        Opponent = 'O' if Current_player == 'X' else 'X' 
        
        if state.the_winner == Opponent: # this prevents a state being formed after a win 
            print("W") #!!!!
            return {'position': None, 'score': 1 * (state.num_empty_squares() +1) if
                    Opponent == max_player else
                    -1*(state.num_empty_squares()+1)
                    }
        elif not state.empty_square(): 
            print("d")
            return {"position": None, "score": 0} #this prevents a state being formed after a draw
        
        if Current_player == max_player: 
            best = {'position': None, "score": -math.inf} # this gives maximizers their first working score( a score that can be compared and replace)
        else:
            best = {'position': None, "score": math.inf} # this gives minimizers their first working score
        for possible_move in state.available_moves(): 
            # step 1: make a move, try that spot
            state.make_move(possible_move, Current_player) # parent move, which will lead to children moves unitl a win or draw
            # step 2: recurse using minimax to simulate multiple children games after making that move
            # state_before = copy.deepcopy(state) #!!!!
            sim_score = self.minimax(state, Opponent) # now, we alternate players
            sim_score["position"] = possible_move # arranging each sim_score according to the move that they were derived from
            
            # state_after = state #!!!!
            # if (state_before != state_after): #!!!!
            #     print("A STATE CORRUPTION HAS BEEEN DETECTED") #!!!!

            #step 3: undo the move
            state.board[possible_move] = " " # resets the move made when it moves to the next move
            state.the_winner = None # undo the winner so it wont affect base coase


            # step 4: upadate the dictionaries if necessary
            if Current_player == max_player: # we are trying to maximize the max_player
                # if the best dictionary housed in sim_score is from a minimize
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best, makes condition two possible

            else: # we are choosing the most optimal move for the opponent(minimizing the opposite playe)
                if sim_score['score'] < best['score']:  
                    best = sim_score     
                  
        return best

#  the purpose of the sim_score is to obtain the child cases of the the opponets move, so as to from the tree

# each node houses either a score win/draw from the base case  or they house the score gotten 
# from the elected current_best of their child scores (the simscore), 
# this process happens until we get to the top and an elected move is made
        