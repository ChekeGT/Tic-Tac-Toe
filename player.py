import random
import time
import math
class Player:

    def __init__(self, mark) -> None:
        self.mark = mark
    
    def play(self, option, board):
        board.make_a_move(option, self.mark)
        return None
    
    def __str__(self) -> str:
        return f"{self.name}({self.mark})"

class HumanPlayer(Player):

    def __init__(self, name, mark) -> None:
        self.name = name
        super().__init__(mark)
    def play(self, board):
        print(board)
        option = int(input("Insert your option(1-8):"))
        try:
            return super().play(option, board)
        except ValueError:
            print("You inserted an incorrect option, please try again")
            self.play(board)

class MachinePlayer(Player):
    
    def __init__(self, mark) -> None:
        self.name = "Machine"
        super().__init__(mark)
    
    def play(self, board):
        blank_spaces = board.get_blank_spaces()
        opt = random.choice(blank_spaces)
        return super().play(opt, board)

class GeniusComputerPlayer(Player):

    def __init__(self, mark) -> None:
        self.name = "Machine"
        super().__init__(mark)
    
    def play(self, board):
        blank_spaces = board.get_blank_spaces()
        if len(blank_spaces) == 9:
            option = random.choice(blank_spaces)
        else:
            option = self.minimax(board, self.mark)['position']
        return super().play(option, board)
    
    def minimax(self, board, player):
        """
        Make a movement and give it a value the value is provided by the formula  x * (number of available spots + 1) 
        where x is -1 if we lose 0 if we make a tie and +1 if we win.
        From all of our options we will choose the one that provides us the greater value ;)
        The value of a path is determined by the worst thing that could happen the lesser value
        """  
        enemy = 'O' if player == 'X' else 'X'

        winner = board.game_has_been_winned()
        blank_spaces = board.get_blank_spaces()

        # Base cases, this will be the bottom of the minimax algorithm and based on these
        # we will be making our decision paths towards the best possible option.
        if winner:
            return {
                'position': None, 
                'score': 1 * (len(blank_spaces) + 1) if winner == self.mark else -1 * (len(blank_spaces) + 1)
                }
        elif len(blank_spaces) == 0:
            return {
                'position': None,
                'score': 0
            }
        
        if player == self.mark:
            best = {
                'position': None,
                'score': -math.inf
            } # Each score should maximize it
        else:
            best = {
                'position': None,
                'score': math.inf
            } # Each score should minimize it
        recursions = 0
        for possible_move in board.get_blank_spaces():
            # Step 1: Make a move, try that spot
            board.make_a_move(possible_move, player)
            # Step 2: Recurse using minimax to simulate a game after making that move
            provisional_best_move = self.minimax(board, enemy)

            # Step 3: Undo the move, this will apply for all the recursions so our game 
            # will be the same as when we start this for loop.
            board.undo_move(possible_move)
            provisional_best_move['position'] = possible_move 

            # Step 4: Pick the best choice for the player. A.K.A update the dictionary with the best possible move based on the score.
            
            #This will provide the better option for the max_player A.K.A our machine
            if player == self.mark:
                if provisional_best_move['score'] > best['score']:
                    best = provisional_best_move
            #And this will provide the better option for the min_player A.K.A our opponent.
            else:
                if provisional_best_move['score'] < best['score']:
                    best = provisional_best_move
        return best
