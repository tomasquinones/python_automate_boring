# conway's game of life
import random, time, copy
WIDTH = 80
HEIGHT = 30

# create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # creates a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('X') # add a living cell
        else:
            column.append(' ') # add a dead cell
    nextCells.append(column) # nextCells is a list of column lists

generationCount = 1

while True: # Main program loop
    print('\n\n\n\n\n') # separate each step with newlines
    currentCells = copy.deepcopy(nextCells)
    
    print(f'Generations: {generationCount}')
    generationCount += 1
    
    #print currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # print the O or .
        print() # print a newline at the end of the row

    # Calculate the next step's cells based on current step's cells:

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get neighboring coordinates:
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count number of living neightbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == 'X':
                numNeighbors += 1 # Top-left neighbor is alive
            if currentCells[x][aboveCoord] == 'X':
                numNeighbors += 1 # Top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == 'X':
                numNeighbors += 1 # Top-right neighbor is alive
            if currentCells[leftCoord][y] == 'X':
                numNeighbors += 1 # Left neighbor is alive
            if currentCells[rightCoord][y] == 'X':
                numNeighbors += 1 # Right neighbor is alive
            if currentCells[leftCoord][belowCoord] == 'X':
                numNeighbors += 1 # Lower-left neighbor is alive
            if currentCells[x][belowCoord] == 'X':
                numNeighbors +=1 # Below neighbor is alive
            if currentCells[rightCoord][belowCoord] == 'X':
                numNeighbors +=1 # Below right neighbor is alive

            # set cell bsed on Conway's Game of Life Rules:
            if currentCells[x][y] == 'X' and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = 'X'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = 'X'
            else:
                # Evertyhing else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(.5) # Add 1-second pause to reduce flickering.
