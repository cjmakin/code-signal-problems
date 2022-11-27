# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers
# in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose
# the grid all contain all of the numbers from 1 to 9 one time.
#
# Implement an algorithm that will check whether the given grid of numbers represents a valid
# Sudoku puzzle according to the layout rules described above. Note that the puzzle represented
# by grid does not have to be solvable.

# 3x3 grids x 9 -> i[0-2]j[0-2] (0-4), i[0-2]j[3-5] (3-7), i[0-2]j[6-8] (6-10)
#                  i[3-5]j[0-2] (3-7), i[3-5]j[3-5] (6-10), i[3-5]j[6-8] (9-13)
#                  i[6-8]j[0-2] (6-10), i[6-8]j[3-5] (9-13), i[6-8]j[6-8] (12-16)

def getSubGrid(i, j):
    subGrid = 0

    if i <= 2:
        if j <= 2:
            subGrid = -1
        elif j >= 3 and j <= 5:
            subGrid = -2
        elif j >= 6:
            subGrid = -3
    elif i >= 3 and i <= 5:
        if j <= 2:
            subGrid = -4
        elif j >= 3 and j <= 5:
            subGrid = -5
        elif j >= 6:
            subGrid = -6
    elif i >= 6:
        if j <= 2:
            subGrid = -7
        elif j >= 3 and j <= 5:
            subGrid = -8
        elif j >= 6:
            subGrid = -9

    return subGrid


def solution(grid):
    stateDict = {}
    j, g = 0, -1

    # Create dictionary with empty array to store values in each row and column
    # rows are keys 0-9, columns are keys 10-19
    for i in range(0, 9):
        stateDict[i] = []
        stateDict[j+10] = []
        stateDict[g] = []
        j += 1
        g -= 1

    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            subGrid = getSubGrid(i, j)

            if grid[i][j] != '.':

                for value in stateDict[i]:
                    if value == grid[i][j]:
                        return False

                for value in stateDict[j+10]:
                    if value == grid[i][j]:
                        return False

                for value in stateDict[subGrid]:
                    if value == grid[i][j]:
                        return False

                stateDict[i].append(grid[i][j])
                stateDict[j+10].append(grid[i][j])
                stateDict[subGrid].append(grid[i][j])

    return True


grid1 = [[".", "4", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "1", ".", ".", "7", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "3", ".", ".", ".", "6", "."],
         [".", ".", ".", ".", ".", "6", ".", "9", "."],
         [".", ".", ".", ".", "1", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", "2", ".", "."],
         [".", ".", ".", "8", ".", ".", ".", ".", "."]]

print(solution(grid1))
