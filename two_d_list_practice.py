# TwoDListPractice

WIDTH = 64
HEIGHT = 32

myGrid = []


# Creates the Grid filled with hashes #
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        column.append('#')
    myGrid.append(column)

# Methodically iterates through myGrid to print the row, column by column
for y in range(HEIGHT):
    for x in range(WIDTH):
        print(myGrid[x][y], end= '')
    print()
