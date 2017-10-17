from Combinations import *
from CombinationsDictionary import CombinationsDic
timesNoEmptySpaces = 0
BLACK_SPACE = -25
#is we are doing down in the main function then left has to be True. And viceversa
def usedNumber(number, kakuroM, position):
    contRow = position[0] -1
    contCol = position[1]
    while contRow >= 0:
        if not isinstance(kakuroM[contRow][contCol], list) and (kakuroM[contRow][contCol]) != 0:
            if (kakuroM[contRow][contCol]) == number:
                return True
        else:
            break

        contRow -= 1

    contRow = position[0]
    contCol = position[1] -1
    while contCol >= 0:
        if not isinstance(kakuroM[contRow][contCol], list) and (kakuroM[contRow][contCol]) != 0:
            if (kakuroM[contRow][contCol]) == number:
                return True
        else:
            break
        contCol -= 1

    contRow = position[0]
    contCol = position[1] + 1
    while contCol < len(kakuroM):
        if not isinstance(kakuroM[contRow][contCol], list) and (kakuroM[contRow][contCol]) != 0:# and (kakuroM[contRow][contCol]) != -1 :
            if (kakuroM[contRow][contCol]) == number:
                return True
        else:
            break
        contCol += 1

    contRow = position[0] + 1
    contCol = position[1]
    while contRow < len(kakuroM):
        if not isinstance(kakuroM[contRow][contCol], list) and (kakuroM[contRow][contCol]) != 0:# and (kakuroM[contRow][contCol]) != -1 :
            if (kakuroM[contRow][contCol]) == number:
                return True
        else:
            break
        contRow += 1

    return False


def usablePermutation(permutation,kakuro,position,horizontal):
    '''
    ACA ESTA EL ERROR ACA ACA ACA!!!!!!!!!!!!!!!!!!!!!!!
    :param permutation:
    :param kakuro:
    :param position:
    :param horizontal:
    :return:
    '''
    row = position[0]
    column = position[1]
    for i in range(len(permutation)):
        if horizontal:
            if usedNumber(permutation[i], kakuro,[row,column+i]):
                return False

        else:
            if usedNumber(permutation[i], kakuro,[row+i,column]):
                return False
            #si va hacia abajo, obtiene
    return True



def getStartingPosition(kakuro):
    lessPos = None
    lessSpaces = 10
    left = None
    for i in range(len(kakuro)):
        for j in range(len(kakuro)):
            if isinstance(kakuro[i][j],list) and kakuro[i][j][1] != 0:
                leftSpaces = getSpaces4getValues(kakuro,[i,j+1],True)
                completed = sumCompleted(kakuro,[i,j],True,leftSpaces)
                if leftSpaces < lessSpaces and not completed:
                    lessSpaces = leftSpaces
                    lessPos = [i,j]
                    left = True
            if isinstance(kakuro[i][j],list) and kakuro[i][j][0] != 0:
                downSpaces = getSpaces4getValues(kakuro,[i+1,j],False)
                completed = sumCompleted(kakuro, [i, j], False, downSpaces)
                if downSpaces < lessSpaces and not completed:
                    lessSpaces = downSpaces
                    lessPos = [i,j]
                    left = False

    return lessPos,left,lessSpaces

def getNonUsableValues(_kakuro,_position,_left):
    usedValues = []
    row = _position[0]
    column = _position[1]
    if _left:
        leftSpces = getSpaces4getValues(_kakuro, _position, True)
        for i in range(leftSpces):
            if _kakuro[row][column + i + 1] != -1:
                usedValues.append([_kakuro[row][column + i + 1], [i + 1]])
    else:
        downSpaces = getSpaces4getValues(_kakuro, _position, False)
        for i in range(downSpaces):
            if _kakuro[row + i + 1][column] != -1:
                usedValues.append([_kakuro[row + i + 1][column], [i + 1]])

    return usedValues

def clearPosition(usedPositions,kakuro):
    for x in range(len(usedPositions)):
        r = usedPositions[x][0]
        c = usedPositions[x][1]
        kakuro[r][c] = -1

def getSpacesAvailable(kakuro,position,spaces,left):
    #recibe la posicion del la fila o columna despues de que esta la suma
    #retorna el numero en el spacio que esta libre
    #por ejemplo [0,20],-1,7,9-1,0
    #20 tiene 4 spacios pero los libres son
    #el 0, y 3 (ya que es el spacio 1 y 4 libres)
    #entonces esta funcion retornaria 1 y 4
    row = position[0]
    column = position[1]
    availableSpaces = []
    if left:
        for i in range(spaces):
            if kakuro[row][column + i] == -1:
                availableSpaces.append(i)
    else:
        for i in range(spaces):
            if kakuro[row + i][column] == -1:
                availableSpaces.append(i)
    return availableSpaces



#TIENE QUE EXISTIR UNA FUNCION QUE ELIMINA LAS COMBINACIONES QUE NO TENGAN CIERTOS NUMEROS Y ADEMAS DE ESAS COMBINACIONES ELIMINAR
#LOS NUMEROS QUE YA EXISTEN Y PERMUTAR LOS RESTANTES

#TIENE QUE HABER UNA QUE REVISE Y NO DE UNA PERMUTACION QUE NO TENGA UN NUMERO VALIDO EN CIERTA POSICION PARA
#LA SUMA DE LA INTERSECCION
#POR EJEMPLO NO PONER UNA PERMUACION = [1,4,3]
#DONDE ESTA EL 4 ES UNA INTERSECCION PARA SUMAR UN 3
#ENTONCES SE DEBE DE SABER QUE ESA PERMUTACION NO ES UTILIZABLE
#PERO SI ESA COMBINACION
def getNewCombinations(combinationsList,usedValues):
    newCombinations = []
    for combination in combinationsList:
        c = []
        for value in combination:
            if value not in usedValues:
                c.append(value)
        newCombinations.append(c)
    return newCombinations

def getSumLeft(kakuroM,position): #returns an integer, moves left

    contRow = position[0]
    contCol = position[1]
    while contCol >= 0:
        if isinstance(kakuroM[contRow][contCol],list):
            spaces = getSpaces4getValues(kakuroM,[contRow,contCol+1],True)
            return kakuroM[contRow][contCol][1],spaces
        elif kakuroM[contRow][contCol] == 0:
            return BLACK_SPACE,0 #-10
        contCol -= 1
    return BLACK_SPACE,0

def getSumUp(kakuroM,position):  #returns an integer, moves up to get the number
    contRow = position[0]
    contCol = position[1]
    while contRow >= 0:
        if isinstance(kakuroM[contRow][contCol],list):
            spaces = getSpaces4getValues(kakuroM, [contRow + 1, contCol], False)
            return kakuroM[contRow][contCol][0],spaces
        elif kakuroM[contRow][contCol] == 0:
            return BLACK_SPACE,0 #-10
        contRow -= 1
    return BLACK_SPACE,0

def isValueSuitable(kakuro,position,left,value):
    row = position[0]
    column = position[1]
    if left:
        upSum,spacesU = getSumUp(kakuro,[row,column])
        if upSum != BLACK_SPACE:
            combinations = getCombination(upSum, spacesU)
            for combination in combinations:
                if value in combination:
                    return True
    else:
        # means it has to get the sum on the right
        leftSum,spacesL = getSumLeft(kakuro, [row,column])
        if leftSum != BLACK_SPACE:
            combinations = getCombination(leftSum,spacesL)
            for combination in combinations:
                if value in combination:
                    return True
    return False

def solver(kakuro):
    global  timesNoEmptySpaces
    printMatrix(kakuro)
    print("+=+=+=+="*15)
    if noEmptySpaces(kakuro):
        timesNoEmptySpaces+= 1
        if isKakuroSolved(kakuro): return True
        else: return False
    else:
        position,left,spaces = getStartingPosition(kakuro)
        '''
        kakuro[1][3] == 9 and kakuro[2][3] ==7 and kakuro[1][7] == 1 and kakuro[2][7] == 2 and kakuro[1][2] == 8 and kakuro[1][8] == 6 and kakuro[2][2] == 1 and kakuro[2][3] == 7 and kakuro[3][1] == 9 and kakuro[4][1] == 8 and kakuro[3][5] == 8 and  kakuro[4][5] == 9 and kakuro[2][7] == 2 and kakuro[2][8] == 7
        '''
        row = position[0]
        column = position[1]
        if left: sum = getNumberLeft(kakuro, position)
        else: sum = getNumberUp(kakuro, position)
        if left: column +=1
        else: row += 1
        listOfUsedValues = getValuesInSpaces(kakuro,[row,column],left)
        combinationsList = getCombination(sum,spaces)
        #print("-")
        #print(CombinationsDic[2][17])
        combinationsList = deletedNonUsableCombs(combinationsList,listOfUsedValues)
        availableSpaces = getSpacesAvailable(kakuro,[row,column],spaces,left)
        combinationsList = getNewCombinations(combinationsList,listOfUsedValues)
        for i in range(len(combinationsList)):
            tryAnotherCombination = False
            combination = combinationsList[i]
            permutations = [list(row) for row in itertools.permutations(combination)]
            #aca se mete las nonusableValues y se eliminan las permutaciones que no lo tengan, o simplemente no se tilizan
            #crear la funcion usablepermutation que recibe la listas de valores que no se pueden utilizar en un punto y
            #no utiliza esa permutacion si se encuentra ese valor
            for j in range(len(permutations)):
                permutation = permutations[j]
                permutationUsed = True
                #ADD A FUNCTION TO KNOW IF YOU CAN USED A PERMUTATION
                #agregar una funcion que revisa,las sumas que esten a los aldos antes de poner el digito en dicha permutacion.
                #entonces si por ejemplo quiere poner un 5
                # en nu lugar que hay un 4, entonces la permutacion no es utliizable
                if not usablePermutation(permutation,kakuro,[row,column],left):
                    continue
                positionsUsed = []
                for k in range(len(availableSpaces)):
                    if left:
                        if kakuro[row][column + availableSpaces[k]]!= -1:
                            positionsUsed.append([row,column + availableSpaces[k]])
                            if kakuro[row][column + availableSpaces[k]] not in permutation or permutation[k] != kakuro[row][column + availableSpaces[k]]:
                                clearPosition(positionsUsed,kakuro)
                                tryAnotherCombination = True
                                break
                            else:
                                continue
                        else:
                            if not isValueSuitable(kakuro,[row,column + availableSpaces[k]],left,permutation[k]):
                                permutationUsed = False
                                break
                            kakuro[row][column + availableSpaces[k]] = permutation[k]
                            positionsUsed.append([row,column + availableSpaces[k]])
                    else:
                        if kakuro[row + availableSpaces[k]][column] != -1:
                            if kakuro[row + availableSpaces[k]][column] not in permutation or permutation[k] != kakuro[row + availableSpaces[k]][column]:
                                clearPosition(positionsUsed, kakuro)
                                tryAnotherCombination = True
                                break
                            else:
                                continue
                        else:
                            if not isValueSuitable(kakuro,[row + availableSpaces[k],column],left,permutation[k]):
                                permutationUsed = False
                                break
                            kakuro[row + availableSpaces[k]][column] = permutation[k]
                            positionsUsed.append([row + availableSpaces[k], column])
                if tryAnotherCombination:
                    break

                if permutationUsed and solver(kakuro):
                    return True
                clearPosition(positionsUsed,kakuro)

        return False



kakuro5x5 =     [[0,0,[3,0],[4,0],0],
                 [0,[5,4],1,-1,0],
                 [[0,7],4,2,-1,0],
                 [0,1,0,0,0],
                 [0,0,0,0,0]]

#combinationL = [[1,2,7],[1,3,6],[1,4,5]]
#print(getNewCombinations(combinationL,[1]))

#print(CombinationsDic[2][17])
#x = CombinationsDic[2][17]
#y  = list(x)
#y.remove([8,9])
#print(CombinationsDic[2][17])


#print(datetime.datetime.now().time())
if solver(kakuro10x10):
    printMatrix(kakuro10x10)
    #print(datetime.datetime.now().time())
    #print(timesNoEmptySpaces)

