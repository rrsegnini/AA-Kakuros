import random



def createBoard(size):
    values = list(range(1, 10))
    board = []

    for i in range(1,size+1):
        newRow = [0,]
        for j in range(1,size):
            if values == []:
                newRow.append(0)
                values = list(range(1, 10))
            else:
                newElement = random.choice(values)
                newRow.append(newElement)
                values.remove(newElement)
        board.append(newRow)
    print(board)
    deleteRepeated(board)
    
    return board

def deleteRepeated(board):
    for i in range(len(board)):
        for j in range(len(board)):
            for i2 in range(i+1,len(board)):
                #for j2 in range(len(board)):
                if board[i][j] == board[i2][j]:
                    board[i2][j]=0

    setSums(board)

def setSums(board):
    contX = len(board)-1
    contY = contX
    while contX >= 0:
        bothSums = [0,0]
        sum = 0
        contY=len(board)-1
        while contY >= 0:
            if board[contX][contY] == 0:
                if sum != 0:
                    bothSums = [0, 0]
                    bothSums[1] = sum
                    board[contX][contY]=bothSums
                    sum=0
                    print ("Cool")
            else:
                sum += board[contX][contY]
            contY-=1

        contX-=1
    printB(board)
def hideSolution(board):
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if board[i][j] != 0 and not isinstance(board[i][j], list):
                board[i][j] = -1
    




















    
def printB(board):
    for i in board:
        print(i)


