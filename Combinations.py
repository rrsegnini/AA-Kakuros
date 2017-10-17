from PruebaKakuros import *
from CombinationsDictionary import CombinationsDic
import itertools
#getPermutations itertools.permutations([1, 2, 3])








def getSumPosition(kakuro):
    for i in range(len(kakuro)):
        for j in range(len(kakuro)):
            if isinstance(kakuro[i][j],list) and kakuro[i][j][1] != 0:
                #get number of spaces to the left
                complete = False
                leftSpaces = getSpaces4getValues(kakuro,[i,j+1],True)
                for k in range(leftSpaces):
                    if kakuro[i][j+k+1] == -1:
                        break
                    else:
                        complete = True
                if not complete:
                    return [i,j],True
            if isinstance(kakuro[i][j],list) and kakuro[i][j][0] != 0:
                #get number of spaces to the left
                complete = False
                downSpaces = getSpaces4getValues(kakuro,[i+1,j],False)
                for k in range(downSpaces):
                    if kakuro[i+k+1][j] == -1:
                        break
                    else:
                        complete = True
                if not complete:
                    return [i,j],False



#





def getValuesInSpaces(_kakuro,_position,_left):
    usedValues = []
    row = _position[0]
    column = _position[1]
    if _left:
        leftSpces = getSpaces4getValues(_kakuro,_position,True)
        for i in range(leftSpces):
            value = _kakuro[row][column+i]
            if _kakuro[row][column + i] != -1:
                usedValues.append(_kakuro[row][column+i])
                #usedValues.append([_kakuro[row][column+i],[i]])
    else:
        downSpaces = getSpaces4getValues(_kakuro, _position, False)
        for i in range(downSpaces):
            if _kakuro[row + i][column] != -1:
                usedValues.append(_kakuro[row + i][column])

    return usedValues

def deletedNonUsableCombs(_combinationsList,_usedValues):
    newCombs = list(_combinationsList)
    for combination in _combinationsList:
        for value in _usedValues:
            if value not in combination:
                newCombs.remove(combination)
                break
    return newCombs


def getCombination(sum,spaces):
    combinatios = CombinationsDic[spaces][sum]
    combinations2 = combinatios[:]
    return combinations2


def getNumberLeftAndPosition(kakuroM,position): #returns an integer, moves left

    contRow = position[0]
    contCol = position[1]
    while contCol >= 0:
        if isinstance(kakuroM[contRow][contCol],list):
            return kakuroM[contRow][contCol][1],[contRow,contCol]
        elif kakuroM[contRow][contCol] == 0:
            return BLACK_SPACE #-10
        contCol -= 1
    return BLACK_SPACE,[contRow,contCol]


def getNextPosition(kakuro,position,right):
    row = position[0]
    column = position[1]
    if right:
        c = 0
        while c < len(kakuro):
            leftSum,location = getNumberLeft(kakuro, [row + c + 1, column])
            if leftSum != -25:
                return location,True
            c += 1

    else:
        c = 0
        while c < len(kakuro):
            upSum, location = getNumberUp(kakuro, [row, column + c + 1])
            if upSum != -25:
                return location,False
            c+=1


'''
def solveKK(kakuro,position):
    if noEmptySpaces(kakuro):
        if isKakuroSolved(kakuro): return True
        else: return False
    else:
        position,left = getSumPosition(kakuro)
        row = position[0]
        column = position[1]
        if left: sum = getNumberLeft(kakuro, position)
        else: sum = getNumberUp(kakuro, position)
        if left: column +=1
        else: row += 1
        spaces = getSpaces4getValues(kakuro,[row,column],left)
        listOfUsedValues = getValuesInSpaces(kakuro, position)
        combinationsList = getCombination(sum,spaces)
        combinationsList = deletedNonUsableCombs(combinationsList,listOfUsedValues)
        for i in range(len(combinationsList)):
            combination = combinationsList[i]
            permutations = [list(row) for row in itertools.permutations(combination)]
            for j in range(len(permutations)):
                permutation = permutations[j]
                positionsUsed = []
                for k in range(spaces):
                    if left:
                        if kakuro[row][column + k]!= -1:
                            positionsUsed.append([row,column+k])
                            if kakuro[row][column + k] not in permutation or permutation[k] != kakuro[row][column + k]:
                                return False
                            else:
                                continue
                        else:
                            kakuro[row][column + k] = permutation[k]
                    else:
                        if kakuro[row + k][column] != -1:
                            if kakuro[row + k][column] not in permutation or permutation[k] != kakuro[row + k][column]:
                                return False
                            else:
                                continue
                        else:
                            kakuro[row + k][column] = permutation[k]
                            
                
                if solveKK(kakuro,position):
                    return True
                for x in range(len(positionsUsed)):
                    r = positionsUsed[x][0]
                    c = positionsUsed[x][1]
                    kakuro[r][c] = -1

        return False

'''
def getStartingPos(kakuro):
    lessPos = [0,0]
    lessSpaces = 9
    left = True
    for i in range(len(kakuro)):
        for j in range(len(kakuro)):
            if isinstance(kakuro[i][j],list) and kakuro[i][j][1] != 0:
                leftSpaces = getSpaces4getValues(kakuro,[i,j+1],True)
                if leftSpaces < lessSpaces:
                    lessSpaces = leftSpaces
                    lessPos = [i,j]
                    left = True

            if isinstance(kakuro[i][j],list) and kakuro[i][j][0] != 0:
                downSpaces = getSpaces4getValues(kakuro,[i+1,j],False)
                if downSpaces < lessSpaces:
                    lessSpaces = downSpaces
                    lessPos = [i,j]
                    left = False

    return lessPos,left


def sumCompleted(kakuro,position,left,spaces):
    complete = True
    if left:
        for k in range(spaces):
            if kakuro[position[0]][position[1] + k + 1] == -1:
                complete = False
                break

    else:
        for k in range(spaces):
            if kakuro[position[0] + k + 1][position[1]] == -1:
                complete = False
                break


    return complete



def solveKK(kakuro,position,left):
    if noEmptySpaces(kakuro):
        if isKakuroSolved(kakuro): return True
        else: return False
    else:

        if position == None:
            position,left = getSumPosition(kakuro)
        row = position[0]
        column = position[1]
        if left: sum = getNumberLeft(kakuro, position)
        else: sum = getNumberUp(kakuro, position)
        if left: column +=1
        else: row += 1
        spaces = getSpaces4getValues(kakuro,[row,column],left)
        #listOfUsedValues = getValuesInSpaces(kakuro, position)
        combinationsList = getCombination(sum,spaces)
        #combinationsList = deletedNonUsableCombs(combinationsList,listOfUsedValues)
        for i in range(len(combinationsList)):
            combination = combinationsList[i]
            permutations = [list(row) for row in itertools.permutations(combination)]
            for j in range(len(permutations)):
                permutation = permutations[j]
                positionsUsed = []
                for k in range(spaces):
                    if left:
                        if kakuro[row][column + k]!= -1:
                            positionsUsed.append([row,column+k])
                            if kakuro[row][column + k] not in permutation or permutation[k] != kakuro[row][column + k]:
                                return False
                            else:
                                continue
                        else:
                            kakuro[row][column + k] = permutation[k]
                    else:
                        if kakuro[row + k][column] != -1:
                            if kakuro[row + k][column] not in permutation or permutation[k] != kakuro[row + k][column]:
                                return False
                            else:
                                continue
                        else:
                            kakuro[row + k][column] = permutation[k]

                position, left = getNextPosition(kakuro, position)
                if solveKK(kakuro,position):
                    return True
                for x in range(len(positionsUsed)):
                    r = positionsUsed[x][0]
                    c = positionsUsed[x][1]
                    kakuro[r][c] = -1

        return False


#position,left = getStartingPos(kakuro20x20)
#print(position,left)

#solveKK(kakuroExample,position,left)
#printMatrix((kakuroExample))




