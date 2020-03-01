# Conway's Game of Life

import random, time, collections
from bitarray import bitarray
WIDTH = 80
HEIGHT = 40

class Cells:
    def __init__(self, prev = None):
        if prev == None:
            self.bits = bitarray(WIDTH * HEIGHT)
            self.bits.setall(False)
            for x, y in self.all():
                if random.randint(0, 1) == 0:
                    self.bits[self.index(x, y)] = True
        else:
            self.bits = bitarray(prev.bits)

            for x, y in self.all():
                index = self.index(x, y)
                alive = prev.bits[index]
                neighbors = prev.neighbors(x, y)

                if alive:
                    if neighbors != 2 and neighbors!= 3:
                        # Living cells with < 2 or > 3 neighbors die:
                        self.bits[index] = False
                elif neighbors == 3:
                    # Dead cells with 3 neighbors become alive:
                    self.bits[index] = True

    def neighbors(self, x, y):
        count = 0
        for xOff in range(-1, 2): #-1, 0, 1
            for yOff in range (-1, 2): #-1, 0, 1
                # Don't add ourselves
                if xOff != 0 or yOff != 0:
                    if self.bits[self.index(x + xOff, y + yOff)]:
                        count += 1

        return count

    def print(self):
        for row in range(HEIGHT):
            start = row * WIDTH
            end = start + WIDTH
            print(self.bits[start:end].to01().replace("0", " ").replace("1", "#"))

    def index(self, x, y):
        return (y % HEIGHT) * WIDTH + (x % WIDTH)

    def all(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                yield x, y

cells = Cells()

prevIterations = collections.deque(maxlen = 10)

iteration = 1
while True:
    print(f"Iteration: {iteration}")
    cells.print()
    for prev in prevIterations:
        if cells.bits == prev:
            print(f"Stabilized after {iteration} iterations")
            exit(0)

    prevIterations.append(cells.bits)
    cells = Cells(cells)

    time.sleep(0.01)

    # Return our cursor to the top
    print("\033[F" * (HEIGHT + 2))
    iteration += 1