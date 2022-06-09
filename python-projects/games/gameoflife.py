# Each cell with one or no neighbors dies, as if by solitude.
# Each cell with four or more neighbors dies, as if by overpopulation.
# Each cell with two or three neighbors survives.
# Each cell with three neighbors becomes populated.

# Conways Game of Life:
# by Ryan

from time import sleep

board = [

    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "O", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "O", "O", "-", "-", "-", "-"],
    ["-", "O", "O", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"]

]

def printBoard(matrix):
    for row in range(len(matrix)):
        currentRow = "| "
        for column in range(len(matrix[row])):
            currentRow += board[row][column] + " | "
        print(currentRow)


def newGeneration(matrix):
    newBoard = [

        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"]

    ]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            neighbors = 0

            if row == 0:
                if column == 0:
                    if matrix[row][column + 1] == "O":
                        neighbors += 1
                    if matrix[row + 1][column] == "O":
                        neighbors += 1
                    if matrix[row + 1][column + 1] == "O":
                        neighbors += 1
                elif column < len(matrix[row]) - 1:
                    if matrix[row][column - 1] == "O":
                        neighbors += 1
                    if matrix[row + 1][column - 1] == "O":
                        neighbors += 1
                    if matrix[row][column + 1] == "O":
                        neighbors += 1
                    if matrix[row + 1][column] == "O":
                        neighbors += 1
                    if matrix[row + 1][column + 1] == "O":
                        neighbors += 1
                elif column == len(matrix[row]) - 1:
                    if matrix[row][column - 1] == "O":
                        neighbors += 1
                    if matrix[row + 1][column] == "O":
                        neighbors += 1
                    if matrix[row + 1][column - 1] == "O":
                        neighbors += 1
            
            elif row > 0 and row < len(matrix) - 1:
                if column == 0:
                    if matrix[row - 1][column] == "O":
                        neighbors += 1 
                    if matrix[row - 1][column + 1] == "O":
                        neighbors += 1 
                    if matrix[row][column + 1] == "O":
                        neighbors += 1
                    if matrix[row + 1][column] == "O":
                        neighbors += 1
                    if matrix[row + 1][column + 1] == "O":
                        neighbors += 1
                elif column < len(matrix[row])-1:
                    if matrix[row - 1][column - 1] == "O":
                        neighbors += 1
                    if matrix[row - 1][column] == "O":
                        neighbors += 1
                    if matrix[row - 1][column + 1] == "O":
                        neighbors += 1
                    if matrix[row][column - 1] == "O":
                        neighbors += 1
                    if matrix[row + 1][column - 1] == "O":
                        neighbors += 1
                    if matrix[row][column + 1] == "O":
                        neighbors += 1
                    if matrix[row + 1][column] == "O":
                        neighbors += 1
                    if matrix[row + 1][column + 1] == "O":
                        neighbors += 1
                elif column == len(matrix[row]) - 1:
                    if matrix[row - 1][column - 1] == "O":
                        neighbors += 1
                    if matrix[row - 1][column] == "O":
                        neighbors += 1
                    if matrix[row][column - 1] == "O":
                        neighbors += 1
                    if matrix[row + 1][column] == "O":
                        neighbors += 1
                    if matrix[row + 1][column - 1] == "O":
                        neighbors += 1
            
            elif row == (len(matrix) - 1):
                if column == 0:
                    if matrix[row - 1][column] == "O":
                        neighbors += 1
                    if matrix[row - 1][column + 1] == "O":
                        neighbors += 1
                    if matrix[row][column + 1] == "O":
                        neighbors += 1

                elif column < len(matrix[row]) - 1:
                    if matrix[row - 1][column] == "O":
                        neighbors += 1
                    if matrix[row - 1][column - 1] == "O":
                        neighbors += 1
                    if matrix[row - 1][column + 1] == "O":
                        neighbors += 1
                    if matrix[row][column - 1] == "O":
                        neighbors += 1
                    if matrix[row][column + 1] == "O":
                        neighbors += 1

                elif column == len(matrix[row]) - 1:
                    if matrix[row - 1][column] == "O":
                        neighbors += 1
                    if matrix[row - 1][column - 1] == "O":
                        neighbors += 1
                    if matrix[row][column - 1] == "O":
                        neighbors += 1

            if neighbors > 3:
                newBoard[row][column] = "-"
            elif neighbors < 2:
                newBoard[row][column] = "-"
            elif neighbors == 3:
                newBoard[row][column] = "O"
            else:
                newBoard[row][column] = matrix[row][column]
            
    return newBoard



        
printBoard(board)

print("Conway's Game of Life: ")

while True:
    sleep(0.5)
    answer = input("Would you like to continue? y/n: ")
    while answer not in ["y", "n", "5"]:
        answer = input("Choose y or n: ")
    if answer == 'n':
        break
    
    elif answer == "5":
        for i in range(5):
            board = newGeneration(board)
            printBoard(board)
            print("")
            sleep(0.5)
    else:
        board = newGeneration(board)
        printBoard(board)

