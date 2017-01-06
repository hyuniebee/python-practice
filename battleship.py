from random import randint

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def create_ships(ship_list, ship_row, ship_col, count):
    ship_list[count].append(ship_row)
    ship_list[count].append(ship_col)
    print "Ship created"
    return ship_list

board = []
number_of_ships = int(raw_input("Please input number of ships:"))
board_dimension = int(raw_input("Please input board dimension:"))
num_turns = int(raw_input("Please input number of turns:"))

for x in range(board_dimension):
    board.append(["O"] * board_dimension)

print "Battleship Time"
print_board(board)

#Initialize the ship list
ship_list = []
count = 0

# Needed this to be a while loop to re-create ships that were repeated
while count < number_of_ships:
    ship_list.append([]) # Create a nested list for every time going through while loop
    ship_row = random_row(board)
    ship_col = random_col(board)
    print ship_row
    print ship_col
    if count > 0:
        if((ship_row == ship_list[count-1][0]) and (ship_col == ship_list[count-1][1])):
            print "Repeated ships..."
            ship_list.remove([]) # Delete the last newly created list
        else:
            create_ships(ship_list, ship_row, ship_col, count)
            count = count + 1
    else:
        create_ships(ship_list, ship_row, ship_col, count)
        count = count + 1
print ship_list

