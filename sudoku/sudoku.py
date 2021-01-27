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


used[0] = list(grid[0][:3])
used[1] = list(grid[0][3:6])
used[2] = list(grid[0][6:9])
backupList = []
backupList.append(np.copy(grid))
print(backupList)
usedBackup = used

print(used)
for indRow in range(1, 9):
    reset = True
    possible = [1,2,3,4,5,6,7,8,9]
    shuffle(possible)
    print(possible)
    for indColumn in range(0, 9):
        # print(indRow, indColumn)
        reset = True
        resCount = 0
        while(reset):
            for tested in range(9):
                rand = possible[tested]
                subInd = whichSubGrid(indRow, indColumn)
                cond1 = checkSubGrid(subInd, rand)
                cond2 = checkRow(indRow, rand)
                cond3 = checkCollumn(indColumn, rand)
                print("Tester le numero ", rand)
                if (cond1 and cond2 and cond3):
                    grid[indRow][indColumn] = int(rand)
                    used[subInd].append(int(rand))
                    print(rand , " ecrit en", indRow, " et ", indColumn)
                    reset = False
                    break
                else:
                    if(tested == 8):
                        reset = True
                        print("-------------------------------RESET-------------------------------------")
                        print("PRE Backup grid")
                        print(grid)
                        grid = backupList[-1]
                        used = usedBackup
                        print("POST Backup grid")
                        print(grid)
                        print(used)
                        shuffle(possible)
                    print("nombre " ,rand , " deja pris")
        backupList.append(np.copy(grid))

        if(grid[indRow][indColumn]):
            print("passed ", grid[indRow])
print("Generated sudoku")
print(grid)
