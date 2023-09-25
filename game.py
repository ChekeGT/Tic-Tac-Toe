from player import HumanPlayer as Player
from player import MachinePlayer as Machine
import time

class Board:

    def __init__(self) -> None:
        self.board = [[" " for y in range(0,3)] for x in range(0,3)]
    
    def __str__(self) -> str:
           s = ""
           pointer = -1
           for row in self.board:
                s += "\n"
                for item in row:
                     pointer += 1
                     s += f"{item if item in ['O', 'X'] else pointer}|"
           return  s
    
    def game_has_been_winned(self):
        # Check rows
        rows = [row for row in self.board]
        columns = self.get_columns()
        diagonals = self.get_diagonals()

        possible_lines = [line for x in [rows,columns,diagonals] for line in x ]

        for line in possible_lines:
            if all([i == line[0] if line[0] in ["O", "X"] else False for i in line]):
                return line[0]
        return False
    
    def get_columns(self):
        
        rows = [row for row in self.board]
        columns = []
        for x in range(0, 3):
            column = []
            for row in rows:
                column.append(row[x])
            columns.append(column)
        return columns
    def get_blank_spaces(self):
        blank_spaces = []
        pointer = -1
        for x in range(0,3):
            for y in range(0,3):
                pointer += 1
                if self.board[x][y] == " ":
                       blank_spaces.append((pointer))
        return blank_spaces
    
    def make_a_move(self, p, player):
         
        if p in self.get_blank_spaces():
            pointer = -1
            row_pointer = p // 3
            for row in self.board:
                for x in range(0, 3):
                    pointer += 1
                    if pointer == p:
                        element_pointer = x
            self.board[row_pointer][element_pointer] = player.mark
        else:
            raise ValueError
            
                         
    
    def get_diagonals(self):
        diagonals = []
        # Getting the 
        diagonal_1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        diagonal_2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
        diagonals.append(diagonal_1)
        diagonals.append(diagonal_2)
        return diagonals

class Game:
    
    def __init__(self) -> None:
        self.board = Board()
        print("Welcome to the Tic Tac Toe Game. Hope you have some fun while playing it")
        # Creating a player 
        option = input("1) Play on Two player mode\n 2) Play vs the machine\n")
        if option == "1":
            p1_name = input("Insert your name:")
            p1_mark = input("Select betwenn O or X:")

            p2_name = input("Insert your name:")
            p2_mark = "O" if p1_mark == "X" else "X"

            self.p1 = Player(p1_name, p1_mark)
            self.p2 = Player(p2_name, p2_mark)

                
        elif option == "2":
            p1_name = input("Insert your name:")
            p1_mark = input("Select betwenn O or X:")

            self.p1 = Player(p1_name, p1_mark)

            self.p2 = Machine("X" if p1_mark == "O" else "O")
    
    def play(self):
        turn = 2
        while self.board.game_has_been_winned() == False and len(self.board.get_blank_spaces()) > 0:
            if turn % 2 == 0:
                self.p1.play(self.board)
                turn += 1
                time.sleep(0.9)
            else:
                self.p2.play(self.board)
                turn += 1
        if len(self.board.get_blank_spaces()) == 0:
            print("It is a tie.")
        else:
            winner = self.board.game_has_been_winned()
            print(f"{self.p1 if self.p1.mark == winner else self.p2} is the winner, congratulations!!")
            print(f"And this is the board {self.board}")
            

    def menu(self) -> None:
        while True:
            option = input("1) Play \n 2) Exit the game\n")
            if option == "1":
                self.play()
            elif option == "2":
                break

game = Game()
game.menu()