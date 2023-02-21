from random import randint


class Minefield:
    def __init__(self):
        self.board = [['x' for column in range(5)]for row in range(5)]
        self.player_board = [['x' for column in range(5)]for row in range(5)]
        self.mines = 0

    def print_board(self):
        for row in self.player_board:
            print(row)

    def reveal_mines(self):
        for row in range(5):
            for column in range(5):
                if self.board[row][column] == "M":
                    self.player_board[row][column] = "M"
        print("Better luck next time. The location of the mines is shown below:")
        for row in self.player_board:
            print(row)

    def make_board(self, mines):
        self.mines = mines
        while self.mines > 0:
            row = randint(0, 4)
            column = randint(0, 4)
            if self.board[row][column] == 'x':
                self.board[row][column] = 'M'
                self.mines -= 1

    def board_numbers(self, sel_row, sel_col):
        count = 0
        count += sum([prox_check(self.board, sel_row-1, sel_col), prox_check(self.board, sel_row-1, sel_col-1),
                      prox_check(self.board, sel_row-1, sel_col+1), prox_check(self.board, sel_row+1, sel_col),
                      prox_check(self.board, sel_row+1, sel_col-1), prox_check(self.board, sel_row+1, sel_col+1),
                      prox_check(self.board, sel_row, sel_col-1), prox_check(self.board, sel_row, sel_col+1)])
        self.player_board[sel_row][sel_col] = str(count)

    def plant_flag(self, sel_row, sel_col):
        self.player_board[sel_row][sel_col] = "F"


def prox_check(board, row, column):
    if row < 0 or column < 0:
        return 0
    try:
        if board[row][column] == 'M':
            return 1
        else:
            return 0
    except:
        return 0


def number_input(message, x, y):
    try:
        choice = int(input(message))
        if x <= choice <= y:
            return choice
        else:
            raise Exception
    except:
        choice = randint(x, y)
        print("Fine. %s it is." % choice)
        return choice


def win():
    print("You win")


def lose(board):
    print("You lose")
    board.reveal_mines()


def yes_no_check(message):
    print(message)
    print("Press Y for Yes, or anything else for No")
    response = input()
    if response.upper() == "Y":
        return True
    else:
        return False


def new_game():
    board = Minefield()
    mines = number_input("How many mines do you want? Min = 1, max= 15", 1, 15)
    board.make_board(mines)
    board.print_board()
    clear_space_left = (25 - mines)
    while mines > 0:
        sel_row = number_input("Please select a row from 0 to 4", 0, 4)
        sel_col = number_input("Please select a column from 0 to 4", 0, 4)
        if yes_no_check("Is this mine?"):
            board.plant_flag(sel_row, sel_col)
        else:
            if board.board[sel_row][sel_col] == "M":
                print("Bad luck")
                mines = 0
            board.board_numbers(sel_row, sel_col)
            clear_space_left -= 1
        board.print_board()
    if clear_space_left == 0:
        win()
    else:
        lose(board)


def instructions():
    print("""Welcome to Minesweeper!

* You will be asked to select a number of mines. 
* A grid will be generated containing 25 cells, composed of the mines you selected mixed amongst empty space.
* You will be asked to select a row and a column.
* If you feel this cell is a mine, you can plant a flag there and move on to your next selection.
* If you feel the cell you've chosen is safe ground, take a chance and skip the flag altogether.
    Guess correctly and the cell text will change to a number which shows the amount of mines in the surrounding cells
* You win when all the safe empty space has been revealed.
* If you hit any mines, however, you lose.

Good luck
""")


def main():
    new_game()


run = True
instructions()
while run:
    main()
    run = yes_no_check("Would you like to play again?")
print("Thanks for playing")