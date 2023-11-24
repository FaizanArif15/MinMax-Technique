from copy import *
from random import *

class PuzzleState:
    
    def __init__(self,initial_state, parent = None, move = [0,0], minmax = None, data = 0) -> None:
        self.puzzle = initial_state
        self.parent = parent
        self.minmax = minmax
        self.move = move
        self.data = data
        
            
    
    def check_for_wining(self):    
        
            # check for first row
            X = 0
            y = 2
            if self.puzzle[0][0] == "O" and self.puzzle[0][1] == "O" and self.puzzle[0][2] == "O":
                self.data = 1
                return "Player O win"
            elif self.puzzle[0][0] == "X" and self.puzzle[0][1] == "X" and self.puzzle[0][2] == "X":
                self.data = -1
                return "Player X win"
            
            # check for second row
            X = 0
            y = 2
            if self.puzzle[1][0] == "O" and self.puzzle[1][1] == "O" and self.puzzle[1][2] == "O":
                self.data = 1
                return "Player O win"
            elif self.puzzle[1][0] == "X" and self.puzzle[1][1] == "X" and self.puzzle[1][2] == "X":
                self.data = -1
                return "Player X win"
            
            # check for third row
            X = 0
            y = 2
            if self.puzzle[2][0] == "O" and self.puzzle[2][1] == "O" and self.puzzle[2][2] == "O":
                self.data = 1
                return "Player O win"
            elif self.puzzle[2][0] == "X" and self.puzzle[2][1] == "X" and self.puzzle[2][2] == "X":
                self.data = -1
                return "Player X win"
            
            # check for first colum
            X = 0
            y = 2
            if self.puzzle[0][0] == "O" and self.puzzle[1][0] == "O" and self.puzzle[2][0] == "O":
                self.data = 1
                return "Player O win"
            elif self.puzzle[0][0] == "X" and self.puzzle[1][0] == "X" and self.puzzle[2][0] == "X":
                self.data = -1
                return "Player X win"
            
            # check for second colum
            X = 1
            y = 2
            if self.puzzle[0][1] == "O" and self.puzzle[1][1] == "O" and self.puzzle[2][1] == "O":
                self.data = 1
                return "Player O win"
            elif self.puzzle[0][1] == "X" and self.puzzle[1][1] == "X" and self.puzzle[2][1] == "X":
                self.data = -1
                return "Player X win"
                
            # check for third colum
            X = 2
            y = 2
            if self.puzzle[0][2] == "O" and self.puzzle[1][2] == "O" and self.puzzle[2][2] == "O":
                self.data = 1
                return "Player O win"
            elif self.puzzle[0][2] == "X" and self.puzzle[1][2] == "X" and self.puzzle[2][2] == "X":
                self.data = -1
                return "Player X win"
                
            # check for diagonal upper left to lower right
            X = 0
            y = 2
            if self.puzzle[0][0] == "O" and self.puzzle[1][1] == "O" and self.puzzle[2][2] == "O":
                self.data = 1
                return "Player O win"
            elif self.puzzle[0][0] == "X" and self.puzzle[1][1] == "X" and self.puzzle[2][2] == "X":
                self.data = -1
                return "Player X win"
            
            # check for diagonal upper right to lower left
            X = 2
            y = 0
            if self.puzzle[0][2] == "O" and self.puzzle[1][1] == "O" and self.puzzle[2][0] == "O":
                self.data = 1
                return "Player O win"
            elif self.puzzle[0][2] == "X" and self.puzzle[1][1] == "X" and self.puzzle[2][0] == "X":
                self.data = -1
                return "Player X win"
            
            # check for draw match
            if not any(None in item for item in self.puzzle):
                self.data = 0
                return "Draw match"
        
    
    def find_possible_moves(self):
        blank_space = []
        for row in range(3):
            for column in range(3):
                if self.puzzle[row][column] == None:
                    blank_space.append((row,column))
        return blank_space
    
    def move_box(self,row,column):
        current_state1 = deepcopy(self.puzzle)
        current_state = PuzzleState(current_state1,parent=self,move=[row,column])
        if self.minmax == "max":
            current_state.minmax = "min"
            current_state.puzzle[row][column] = "O"
        elif self.minmax == "min":
            current_state.minmax = "max"
            current_state.puzzle[row][column] = "X"
        return current_state
            
def minmax(current_state):
    finish = current_state.check_for_wining()
    
    if finish:
        return current_state.data
    
    if current_state.minmax == "max":
        max_value = float("-inf")
        possible_moves = current_state.find_possible_moves()
        for move in possible_moves:
            new_state = current_state.move_box(move[0],move[1])
            value = minmax(new_state)
            if max_value <= value:
                max_value = value
        return max_value
    
    elif current_state.minmax == "min":
        min_value = float("inf")
        possible_moves = current_state.find_possible_moves()
        for move in possible_moves:
            new_state = current_state.move_box(move[0],move[1])
            value = minmax(new_state)
            if min_value >= value:
                min_value = value
        return min_value
    
def solve_tictactoe(initial_state):
    
    best_move = (0,0)
    best_value = float("-inf")
    
    current_state = PuzzleState(initial_state, minmax="max")
    
    possible_moves = current_state.find_possible_moves()    
    for move in possible_moves:
        new_state = current_state.move_box(move[0],move[1])
        value = minmax(new_state)
        if best_value <= value:
            best_value = value
            best_move = move
    
    return best_move

def check_user_input(initial_state,user_input):

    if user_input == 1 and initial_state[0][0] == None:
        return [0,0]
    elif user_input == 2 and initial_state[0][1] == None:
        return [0,1]
    elif user_input == 3 and initial_state[0][2] == None:
        return [0,2]
    elif user_input == 4 and initial_state[1][0] == None:
        return [1,0]
    elif user_input == 5 and initial_state[1][1] == None:
        return [1,1]
    elif user_input == 6 and initial_state[1][2] == None:
        return [1,2]
    elif user_input == 7 and initial_state[2][0] == None:
        return [2,0]
    elif user_input == 8 and initial_state[2][1] == None:
        #print("sdfsh")
        return [2,1]
    elif user_input == 9 and initial_state[2][2] == None:
        return [2,2]
    else:
        print("enter again position")
        user_input = int(input("Enter your position 1 to 9: "))
        return check_user_input(initial_state,user_input)

if __name__ == "__main__":
    
    initial_state = [[None for i in range(3)]for j in range(3)]
    
    print("Who will take the first move")
    first_move_option = int(input("0 means computer and 1 means you: "))
    print()
    for row in initial_state:
        print(row)
    print()
    if first_move_option == 0:
        while True:
            computer_move = solve_tictactoe(initial_state)
            initial_state[computer_move[0]][computer_move[1]] = "O"
            finish = PuzzleState(initial_state).check_for_wining()
            for row in initial_state:
                print(row)
            print()
            if finish:
                print(finish)
                break
            user_input = int(input("Enter your position 1 to 9: "))
            user_move = check_user_input(initial_state,user_input)
            initial_state[user_move[0]][user_move[1]] = "X"
            finish = PuzzleState(initial_state).check_for_wining()
            for row in initial_state:
                print(row)
            print()
            if finish:
                print(finish)
                break
    else:
        while True:
            user_input = int(input("Enter your position 1 to 9: "))
            user_move = check_user_input(initial_state,user_input)
            initial_state[user_move[0]][user_move[1]] = "X"
            finish = PuzzleState(initial_state).check_for_wining()
            for row in initial_state:
                print(row)
            print()
            if finish:
                print(finish)
                break
            computer_move = solve_tictactoe(initial_state)
            initial_state[computer_move[0]][computer_move[1]] = "O"
            finish = PuzzleState(initial_state).check_for_wining()
            for row in initial_state:
                print(row)
            print()
            if finish:
                print(finish)
                break
            
