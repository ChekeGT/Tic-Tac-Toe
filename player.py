import random
import time
class Player:

    def __init__(self, mark) -> None:
        self.mark = mark
    
    def play(self, option, board):
        board.make_a_move(option, self)
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