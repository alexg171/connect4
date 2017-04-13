def grid_maker(h, w):
    grid = [["-" for i in range(w)] for i in range(h)]
    return grid

def print_grid(grid):
    for row in grid:
        print (row)

def get_input():
    print("=================================")
    col = input(">>>")
    if (col.isdigit()):
        col = int(col)
        if (col > 6 or col < 0):
            print ("Try a valid number.")
            get_input()
        else:
            play_column(col)
    else:
        print ("Try a number.")
        get_input()

player = 'O'
def play_column(col):
    global player
    if (grid[5][col] == '-'):
        grid[5][col] = player
    elif (grid[4][col] == '-'):
        grid[4][col] = player
    elif (grid[3][col] == '-'):
        grid[3][col] = player
    elif (grid[2][col] == '-'):
        grid[2][col] = player
    elif (grid[1][col] == '-'):
        grid[1][col] = player
    elif (grid[0][col] == '-'):
        grid[0][col] = player
    print_grid(grid)
    if (player == 'O'):
        player = 'X'
    else:
        player = 'O'

############################################        
grid = grid_maker(6,7)
print_grid(grid)
while True:
    get_input()
