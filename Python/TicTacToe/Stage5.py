class Board:
    def __init__(self, input):
        self.cells = list(input)
        
    def check_diagonals(self, player):
        return self.cells[0] == self.cells[4] == self.cells[8] == player or self.cells[6] == self.cells[4] == self.cells[2] == player
    
    def check_verticals(self, player):
        for i in range(3):
            if self.cells[i+0] == self.cells[i+3] == self.cells[i+6] == player:
                return True
        return False
    
    def print_board(self):
        print("---------")
        print(f"| {self.cells[0]} {self.cells[1]} {self.cells[2]} |")
        print(f"| {self.cells[3]} {self.cells[4]} {self.cells[5]} |")
        print(f"| {self.cells[6]} {self.cells[7]} {self.cells[8]} |")
        print("---------")        

    def check_horizontals(self, player):
        for i in range(0, 7, 3):
            if self.cells[i+0] == self.cells[i+1] == self.cells[i+2] == player:
                return True
        return False
    
    def check_player(self, player):
        return self.check_diagonals(player) or self.check_horizontals(player) or self.check_verticals(player)
    
    def check_winner(self):
        count_o = len([el for el in self.cells if el == "O"])
        count_x = len([el for el in self.cells if el == "X"])

        if not (-1 <= (count_o - count_x) <= 1):
            return "Impossible"
        if self.check_player("X") and self.check_player("O"):
            return "Impossible"
        if self.check_player("X"):
            return "X wins"
        if self.check_player("O"):
            return "O wins"

        if len([el for el in self.cells if el == " "]) == 0:
            return "Draw"
        return "Game not finished"

class Game:
    board = Board("         ")
    player = "X"
    
    def __init__(self, boardstring="         "):
        Game.board = Board(boardstring)
        
    def move(self):
        while True:
            try:
                x, y = [int(a) for a in input("Enter the coordinates: ").split()]
            except ValueError:
                print("You should enter numbers!")
                continue
            if not isinstance(x, int) or not isinstance(y, int):
                print("You should enter numbers!")
                continue
            if x > 3 or y > 3 or x < 1 or y < 1:
                print("Coordinates should be from 1 to 3!")
                continue
            if Game.board.cells[3*(3-y)+(x-1)] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            Game.board.cells[3*(3-y)+(x-1)] = self.player
            break


game = Game()
while True:
    game.board.print_board()
    status = game.board.check_winner()
    if status == "Game not finished":
        game.move()
        if game.player == "X":
            game.player = "O"
        elif game.player == "O":
            game.player = "X"
    else:
        print(status)
        break