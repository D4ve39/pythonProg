from random import *
import numpy as np

grid = np.zeros((9, 9))
initial = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grid[0] = initial
shuffle(grid[0])

used = [[], [], [], [], [], [], [], [], []]


def whichSubGrid(indRow, indColumn):
    indSub = 0
    if (0 <= indRow < 3 and 0 <= indColumn < 3):
        indSub = 0
    elif (0 <= indRow < 3 and 3 <= indColumn < 6):
        indSub = 1
    elif (0 <= indRow < 3 and 6 <= indColumn < 9):
        indSub = 2
    elif (3 <= indRow < 6 and 0 <= indColumn < 3):
        indSub = 3
    elif (3 <= indRow < 6 and 3 <= indColumn < 6):
        indSub = 4
    elif (3 <= indRow < 6 and 6 <= indColumn < 9):
        indSub = 5
    elif (6 <= indRow < 9 and 0 <= indColumn < 3):
        indSub = 6
    elif (6 <= indRow < 9 and 3 <= indColumn < 6):
        indSub = 7
    elif (6 <= indRow < 9 and 6 <= indColumn < 9):
        indSub = 8
    return indSub


def checkSubGrid(indSub, numb):
    res = False
    # print("Used n", indSub, "is", used[indSub])
    if (numb not in used[indSub]):
        res = True
    return res


def checkRow(indRow, numb):
    res = False
    row = grid[indRow]
    # print("Row n", indRow, "is", row)
    if (numb not in row):
        res = True
    return res


def checkCollumn(indColumn, numb):
    res = False
    column = [r[indColumn] for r in grid]
    if (numb not in column):
        res = True
    return res

def testCase(indRow, indColumn, numb):
    subInd = whichSubGrid(indRow, indColumn)
    cond1 = checkSubGrid(subInd, numb)
    cond2 = checkRow(indRow, numb)
    cond3 = checkCollumn(indColumn, numb)
    return cond1 and cond2 and cond3


used[0] = list(grid[0][:3])
used[1] = list(grid[0][3:6])
used[2] = list(grid[0][6:9])
backupList = []
backupList.append(np.copy(grid))

for indRow in range(1, 9):
    for indColumn in range(0, 9):
        
print("Generated sudoku")
print(grid)
