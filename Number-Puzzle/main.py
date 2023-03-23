import random
import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
# extra flags available FULLSCREEN or DOUBLEBUF for smoother graphics
win = pygame.display.set_mode((500, 500))  # returns surface object for drawing

# function is used to set the caption or title of the game window that is created using Pygame.
# can be reset using set_caption anywhere in the code below
pygame.display.set_caption("Puzzle Game")

# Create the game board
# expression creates a list containing 4 sublist,
# each of which contains 4 elements initialized to the value 0.
board = [[0 for x in range(4)] for y in range(4)]

#  creates a sequence of integers starting from 1 and ending at 15
#  and the list() constructor converts this sequence into a list.
numbers = list(range(1, 16))

# numbers list contains the numbers from 1 to 15 in order,
# and shuffle() is used to randomly shuffle the order of these numbers.
random.shuffle(numbers)

for i in range(4):
    for j in range(4):
        if i == 3 and j == 3:  # this is the location for empty cell
            board[i][j] = None  # Empty cell in the board is kept as None
        else:
            board[i][j] = numbers.pop()  # filling up the board with numbers from numbers list and popping them off

# Define colors
BOARD_BASE = (148, 151, 160)  # colour of the board cells
BLACK = (0, 0, 0)  # just black
PRIMARY_1 = (38, 30, 26)  # colour of empty cell and text
PRIMARY_2 = (87, 79, 80)  # colour of bottom score bar

# Define font
font = pygame.font.Font(None, 48)  # first argument None using system font; otherwise could use path to font file

# Define starting coordinates for drawing the game board
x, y = 50, 50  # the top left edge of the board starts drawing from this (x,y) point

# Define the size of each cell
cell_size = 100

# Variable to store number of moves which are defined by key press (up, down, right, left)
moves = 0

# Main game loop
running = True
while running:
    # Key press event handling

    #  pygame.event.get() function returns a list of all pending
    #  events that have occurred since the last time it was called.
    for event in pygame.event.get():

        #  pygame.QUIT event occurs when a user presses close button
        if event.type == pygame.QUIT:
            running = False

        #  checking if user pressed any key on the keyboard
        if event.type == pygame.KEYDOWN:

            #  checking if the KEYDOWN event correspond to 'up' key on the keyboard
            if event.key == pygame.K_UP:
                # iterate over each cell in the game board, except for the first row, which cannot be shifted upwards.
                for i in range(1, 4):
                    for j in range(4):
                        # this checks if the target cell is the empty one because that's the
                        # one that would move
                        if board[i][j] is None:
                            board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
                            moves += 1
                            break
                    else:
                        continue
                    break
            elif event.key == pygame.K_DOWN:
                #  we start the loop counter at 2 because the last row of the game board (index 3)
                #  cannot be shifted downwards. Each time we decrease one so -1 and last raw we want
                #  to iterate is row 0 so end row is marked as -1, so it stops at 0.
                for i in range(2, -1, -1):
                    for j in range(4):
                        if board[i][j] is None:
                            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                            moves += 1
                            break
                    else:
                        continue
                    break
            elif event.key == pygame.K_LEFT:
                for i in range(4):
                    #   iterate over each cell in the game board, except for the first column,
                    #   which cannot be shifted to the left.
                    for j in range(1, 4):
                        if board[i][j] is None:
                            board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
                            moves += 1
                            break
                    else:
                        continue
                    break
            elif event.key == pygame.K_RIGHT:
                for i in range(4):
                    #  we start the loop at index 2 instead of 3 is because the last column of the game board
                    #  (index 3) cannot be shifted towards the right, as it is already the rightmost column.
                    for j in range(2, -1, -1):

                        if board[i][j] is None:
                            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                            moves += 1
                            break
                    else:
                        continue
                    break

    # Check for a win

    # drawing the winning board where all numbers are in correct order

    #  j + i * 4 + 1 calculates the value to be stored in each cell
    # +1 because i=0,j=0 will give 0 but the count starts from 1 instead
    win_board = [[j + i * 4 + 1 for j in range(4)] for i in range(4)]
    win_board[3][3] = None
    if board == win_board:
        text = font.render("You win!", True, PRIMARY_1)
        # creates a rectangular area that encloses a block of text,
        # based on the size of the text and its position on the screen.
        text_rect = text.get_rect(center=(250, 250))
        win.blit(text, text_rect)  # attach the winning blit to the 'win' surface which is original game board

    # Draw the game board
    for i in range(4):
        for j in range(4):
            # x and y are variables that specify the top-left corner of the game board on the screen.
            # The left parameter is set to x + j * cell_size,
            # which specifies the horizontal position of the cell based on its column index.
            # The top parameter is set to y + i * cell_size,
            # which specifies the vertical position of the cell based on its row index.
            # The width and height parameters are set to cell_size, which specify the dimensions of the cell.
            rect = pygame.Rect(x + j * cell_size, y + i * cell_size, cell_size, cell_size)
            if board[i][j] is not None:
                pygame.draw.rect(win, BOARD_BASE, rect)
                text = font.render(str(board[i][j]), True, PRIMARY_1)
                text_rect = text.get_rect(center=rect.center)
                win.blit(text, text_rect)  # attaching the board to the surface 'win'
            else:
                pygame.draw.rect(win, PRIMARY_1, rect)

    # Draw the number of moves
    moves_text = font.render("Moves: " + str(moves), True, BLACK)
    moves_rect = moves_text.get_rect(center=(250, 475))
    win.fill(PRIMARY_2, (0, 450, 500, 50))
    win.blit(moves_text, moves_rect)

    # Update the game window
    pygame.display.update()

# Quit Pygame
pygame.quit()
