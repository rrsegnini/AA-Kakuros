import random

#print (random.randint(0,9))

def crearMatriz():
    n=7
    matrix = []
    fila_nueva = []
    for i in range(0,n):
        
        for j in range(0,n):
            fila_nueva += [[]]                   
            #print (random.randint(0,9))
        matrix += [fila_nueva]
        fila_nueva = []





    i=0 #filas
    j=0 #columnas
    while i != n:
        j=0
        #i=0
        while j != n:
            if j == 0 or i == 0:
                matrix[i][j].insert(0, 0)
                matrix[i][j].insert(1, 0)
            else:
                top = random.randint(0,n)
                bottom = random.randint(0,n)
                matrix[i][j].insert(0, top)
                matrix[i][j].insert(1, bottom)
            j+=1
        i+=1
        
    print (matrix)

def sumaAleatoria(n):
    lista_numeros = [1,2,3,4,5,6,7,8,9]
    num = random.randint(0,n)
    for n in range(0,n):
        
        num = random.choice(lista_numeros)
        print(num)
        lista_numeros.remove(num)
        #print (lista_numeros[num])



        


#PRUEBAS PRUEBAS Y PRUEBAS

import random



'''
CONSTANTS DECLARATION
'''

BLACK_SPACE = -25
BLANK_SPACE = 0

# print (random.randint(0,9))

def crearMatriz():
    n = 7
    matrix = []
    fila_nueva = []
    for i in range(0, n):

        for j in range(0, n):
            fila_nueva += [[]]
            # print (random.randint(0,9))
        matrix += [fila_nueva]
        fila_nueva = []

    i = 0  # filas
    j = 0  # columnas
    while i != n:
        j = 0
        # i=0
        while j != n:
            if j == 0 or i == 0:
                matrix[i][j].insert(0, 0)
                matrix[i][j].insert(1, 0)
            else:
                top = random.randint(0, n)
                bottom = random.randint(0, n)
                matrix[i][j].insert(0, top)
                matrix[i][j].insert(1, bottom)
            j += 1
        i += 1


    print(matrix)


def createEmptyMatrix():
    mLength = random.randint(10,20)
    newMatrix = []
    for x in range(mLength):
        newList = []
        newMatrix.append(newList)
        for y in range(mLength):
            newList.append(0)
            '''
            randomNumber = random.randint(0, 20)
            if randomNumber == 3:
                newList.append([random.randint(0,45),random.randint(0,45)])
            else:
                newList.append(0)
            '''

    return newMatrix




def printMatrix(_matrix):
    matrixLength = len(_matrix)
    for x in range(matrixLength):
        print(_matrix[x],"\n")




def sumaAleatoria(n):
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = random.randint(0, n)
    for n in range(0, n):
        num = random.choice(lista_numeros)
        print(num)
        lista_numeros.remove(num)
        # print (lista_numeros[num])


def getNum():
    num = random.randint(0,45)
    return num
'''
kakuroExample = [[0,0,[3,0],[4,0],0],
                 [0,[5,4],-1,-1,0],
                 [[0,7],-1,-1,-1,0],
                 [0,-1,0,0,0],
                 [0,0,0,0,0]]

kakuroExampleSolved = [[0,0,[3,0],[4,0],0],
                 [0,[5,4],1,3,0],
                 [[0,7],4,2,1,0],
                 [0,1,0,0,0],
                 [0,0,0,0,0]]

'''

def getSum(array,row,column,arraylength,down): #position is an array of two elements
    sum = 0
    if down:
        while row <= arraylength-1 and array[row][column] != 0 \
                and array[row][column] != BLANK_SPACE and not isinstance(array[row][column],list):
            sum += array[row][column]
            row += 1
    else:
        while column <= arraylength-1 and array[row][column] != 0 \
                and array[row][column] != BLANK_SPACE and not isinstance(array[row][column],list):
            sum += array[row][column]
            column += 1

    return sum



def getNumberUp(kakuroM,position):  #returns an integer, moves up to get the number

    contRow = position[0]
    contCol = position[1]
    while contRow >= 0:
        if isinstance(kakuroM[contRow][contCol],list):
            return kakuroM[contRow][contCol][0]
        elif kakuroM[contRow][contCol] == 0:
            return BLACK_SPACE #-10
        contRow -= 1
    return BLACK_SPACE

def getNumberLeft(kakuroM,position): #returns an integer, moves left

    contRow = position[0]
    contCol = position[1]
    while contCol >= 0:
        if isinstance(kakuroM[contRow][contCol],list):
            return kakuroM[contRow][contCol][1]
        elif kakuroM[contRow][contCol] == 0:
            return BLACK_SPACE #-10
        contCol -= 1
    return BLACK_SPACE



def numberRepeated(number,kakuroM,position):
    contRow = position[0]
    contCol = position[1]
    while contRow >= 0:
        if not isinstance(kakuroM[contRow][contCol], list) or (kakuroM[contRow][contCol]) == 0:
            if(kakuroM[contRow][contCol]) == number:
                return True
        else:
            break

        contRow -= 1

    contRow = position[0]
    contCol = position[1]
    while contCol >= 0:
        if not isinstance(kakuroM[contRow][contCol], list) or (kakuroM[contRow][contCol]) == 0:
            if(kakuroM[contRow][contCol]) == number:
                return True
        else:
            break
        contCol -= 1
    '''


    contRow = position[0]
    contCol = position[1]
    while contCol < len(kakuroM):
        if not isinstance(kakuroM[contRow][contCol], list) or (kakuroM[contRow][contCol]) == 0 :
            if(kakuroM[contRow][contCol]) == number:
                return True
        else:
            break
        contCol += 1

    contRow = position[0]
    contCol = position[1]
    while contRow < len(kakuroM):
        if not isinstance(kakuroM[contRow][contCol], list) or (kakuroM[contRow][contCol]) == 0:
            if(kakuroM[contRow][contCol]) == number:
                return True
        else:
            break
        contRow += 1
    '''

    return False


'''
La funcion que revisa si esta solucionado, es simplemente encontrar un array con 2 elementos.
Revisar si para ekl primero la suma da el numero que es y si no es falso. LISTO

'''
def isKakuroSolved(array):
    arrayL = len(array)
    for i in range(arrayL):
        for j in range(arrayL):
            if isinstance(array[i][j],list):
                if array[i][j][0] != 0:

                    ss = array[i][j]
                    st = array[i+1][j]
                    if array[i+1][j] == -1:
                        return False
                    #revisa las sumas
                    if (getSum(array,i+1,j,arrayL,True)) != array[i][j][0]:
                        return False
                if array[i][j][1] != 0:
                    if array[i][j+1] == -1:
                        return False
                    if (getSum(array,i,j+1,arrayL,False)) != array[i][j][1]:
                        return False

    return True


'''

def solve(_kakuro, _position, _options ): #position is an array with to elements, i,j.
                                        #options is an array of the remaining numbers,
                                        #if one is eliminated in the _kauro, then its added back to the 
                                        #options array
    if isKakuroSolved(_kakuro):
        return True
    else:
        values = [calculate possible legal values for that field]
        valuesN = [1,2,3,4,5,6,7,8,9]
        for value in valuesN:
            kakuro[position] = value
            solve(_kakuro)
        kakuro[position]
'''

def changeValues(num,values):
    if (num == 0):
        return values
    nvalues = []
    for i in range(len(values)):
        value =  values[i]
        if value < num:
            nvalues.append(value)
        else:
            break

    return nvalues

def getPosition(kakuro):
    while True:
        row = random.randint(0, len(kakuro)-1)
        column = random.randint(0, len(kakuro)-1)
        if not isinstance(kakuro[row][column],list) and kakuro[row][column] == BLANK_SPACE:
            return [row,column]

def getNextPosition(kakuro,position):
    row = position[0]
    column = position[1]
    length = len(kakuro)
    while row < length:
        if (column) == length:
            column = 0
        while column < length:
            value = kakuro[row][column]
            if kakuro[row][column] == -1:
                return [row,column]
            column += 1
        row += 1


#working better
def getNextPosition2(kakuro):
    for i in range(len(kakuro)):
        for j in range(len(kakuro)):
            if kakuro[i][j] == -1:
                return [i,j]




def noEmptySpaces(array):
    arrayL = len(array)
    for i in range(arrayL):
        for j in range(arrayL):
            if not isinstance(array[i][j], list) and array[i][j] == BLANK_SPACE:
                return False

    return True


def deleteRepeatedValues(kakuroM,values,position):
    row = position[0]
    column = position[1]
    while row >= 0:
        if not isinstance(kakuroM[row][column], list) or (kakuroM[row][column]) != 0 or \
                        (kakuroM[row][column]) != BLANK_SPACE:
            value = (kakuroM[row][column])
            if value in values:
                values.remove(value)
        else:
            break

        row -= 1

    row = position[0]
    column = position[1]
    while column >= 0:
        if not isinstance(kakuroM[row][column], list) or (kakuroM[row][column]) != 0 or \
                        (kakuroM[row][column]) != BLANK_SPACE:
            value = (kakuroM[row][column])
            if value in values:
                values.remove(value)
        else:
            break
        column -= 1

    return values



#works better
def deleteRepeatedValues2(kakuroM,values,position):
    newValues = []
    for i in range(len(values)):
        if not numberRepeated(values[i],kakuroM,position):
            newValues.append(values[i])
    return newValues


def getNewValues(num1,num2,values,position,kakuro):
    if num1 != -25 and num2 != -25:
        values2 = changeValues(num1, values)
        values3 = changeValues(num2, values2)
    elif num1 == -25 and num2 != -25:
        values3 = changeValues(num2, values)
    else:
        values3 = values


    newValues = deleteRepeatedValues2(kakuro,values3,position)
    values = reviewNewSums(num1, num2, kakuro, position, newValues)
    return values


def isValueUseful(sum,spaces,value):
    #returns True if these values can be used
    if (sum/2) == value:
        return False
    values = [1,2,3,4,5,6,7,8,9]
    index = values.index(value)
    values = values[index:]
    num = sum
    for i in range(spaces-1):
        if(i >= len(values)):
            return False
        num = num - values[i]
    if num <= 9:
        return True
    return False

'''
Esta funcion, por ejemplo. Toma la suma y le resta todas las posiciones que hayan hasta la izquierda o la derecha
si es TRUE busca a la izquierda si es FALSE busca hacia arriba
Entonces digamos si se tiene que llegar a 17 y se tiene un 1,2 a la par
esta funcion retorna 14, lo cual es 17 - (1+2) 
'''
def getNewSum(array,position,sum,left):
    contRow = position[0]
    contCol = position[1]
    newSum = sum
    if left:
        contCol -= 1
        while contCol >= 0 and not isinstance(array[contRow][contCol],list) \
                and array[contRow][contCol] != 0:
            newSum -= array[contRow][contCol]
            contCol -= 1
    else:
        contRow -= 1
        while contRow >= 0 and not isinstance(array[contRow][contCol],list) \
                and array[contRow][contCol] != 0:
            newSum -= array[contRow][contCol]
            contRow -= 1

    return newSum

def getSpaces(array,position,right):
    contRow = position[0]
    contCol = position[1]
    spaces = 0
    length = len(array)
    if right:
        while contCol < length and array[contRow][contCol] == BLANK_SPACE:
            spaces += 1
            contCol += 1
    else:
        while contRow < length and array[contRow][contCol] == BLANK_SPACE:
            spaces += 1
            contRow += 1
    return spaces


def getSpaces4getValues(array,position,right):
    contRow = position[0]
    contCol = position[1]
    spaces = 0
    length = len(array)
    if right:
        while contCol < length and array[contRow][contCol] != 0 and not isinstance(array[contRow][contCol],list):
            spaces += 1
            contCol += 1
    else:
        while contRow < length and array[contRow][contCol] != 0 and not isinstance(array[contRow][contCol],list):
            spaces += 1
            contRow += 1
    return spaces




def getLowestValue(_sum,_spaces):
    values = [1,2,3,4,5,6,7,8,9]
    while True:
        sum = _sum
        for i in range(_spaces-1):
            sum -= values[i]

        if sum <= 9:
            return values
        else:
            values.remove(values[0])



def getHighestValue(_sum,_spaces):
    if _sum == BLACK_SPACE:
        return _sum
    sum = _sum
    values = [1,2,3,4,5,6,7,8,9]
    for i in range(_spaces-1):
        sum -= values[i]

    return sum

def removeHigherValues(_value,_values):
    if _value == BLACK_SPACE:
        return _values

    newValues = []
    for i in range(len(_values)):
        if _values[i] <= _value:
            newValues.append(_values[i])
        else:
            break
    return newValues


def getIntersection(list1, list2):
    return list(set(list1).intersection(set(list2)))


def reviewNewSums(sum1,sum2,kakuro,position,values):
    if sum1 == -BLACK_SPACE and sum2 == -BLACK_SPACE: return values
    if sum1 != -BLACK_SPACE: sum1 = getNewSum(kakuro, position, sum1, True)
    if sum2 != -BLACK_SPACE: sum2 = getNewSum(kakuro, position, sum2, False)

    spacesRight = getSpaces(kakuro,position,True)
    spacesDown = getSpaces(kakuro,position,False)

    if spacesRight == 1 or spacesDown == 1:
        if sum1 == BLACK_SPACE:
            minValue = sum2
        elif sum2 == BLACK_SPACE:
            minValue = sum1
        else:
            minValue = min(sum1,sum2)
        if minValue not in values:
            values = []
        else:
            values = [minValue]
        return values

    sum1Highest = getHighestValue(sum1,spacesRight)
    sum2Highest = getHighestValue(sum2,spacesDown)
    valuesL1 = removeHigherValues(sum1Highest,values)
    valuesL2 = removeHigherValues(sum2Highest,values)

    values = getIntersection(valuesL1,valuesL2)

    return values


    # AGREGAR UNA FUNCION QUE TOME LA NUEVA SUMA Y OBTENGA LOS VALORES MAS ALTOS QUE PUEDE TOMAR
    # DESPUES DE TOMAR ESTOS VALORES,



def getValues(_kakuro,_position,leftSum,upSum):
    contRow = _position[0]
    contCol = _position[1]

    spacesSumUp = BLACK_SPACE
    spacesSumLeft = BLACK_SPACE

    while contRow >= 0:
        if isinstance(_kakuro[contRow][contCol], list):
            spacesSumUp = getSpaces4getValues(_kakuro,[contRow+1,contCol],False)
            break
        elif _kakuro[contRow][contCol] == 0:
            spacesSumUp = BLACK_SPACE  # -10
            break
        contRow -= 1



    contRow = _position[0]
    contCol = _position[1]
    while contCol >= 0:
        if isinstance(_kakuro[contRow][contCol], list):
            spacesSumLeft = getSpaces4getValues(_kakuro,[contRow,contCol+1],True)
            break
        elif _kakuro[contRow][contCol] == 0:
            spacesSumLeft = BLACK_SPACE  # -10
            break
        contCol -= 1


    if spacesSumUp != BLACK_SPACE and spacesSumLeft == BLACK_SPACE:
        values = superDictionary[spacesSumUp][upSum]

    elif spacesSumUp == BLACK_SPACE and spacesSumLeft != BLACK_SPACE:
        values = superDictionary[spacesSumLeft][leftSum]

    else:
        values1 = superDictionary[spacesSumUp][upSum]
        values2 = superDictionary[spacesSumLeft][leftSum]
        values = getIntersection(values1,values2)
    return values


def solveKakuro(kakuro):

    #printMatrix(kakuro)
    #print("--------------------------\n------------------\n--------------------------")
    #print("--------------------------\n------------------\n--------------------------")

    if noEmptySpaces(kakuro):
        if isKakuroSolved(kakuro):
            return True
        else:
            return False
    else:
        position = getNextPosition2(kakuro)
        row = position[0]
        column = position[1]
        num1 = getNumberLeft(kakuro,position)
        num2 = getNumberUp(kakuro,position)
        # nueva funcion, lo que hace es que se va al diccionario y obtiene las cosas
        values = getValues(kakuro, position, num1, num2)
        values = getNewValues(num1,num2,values,position,kakuro)
        if values == []:
            return False
        for i in range(len(values)):
            value = values[i]
            kakuro[row][column] = value
            if solveKakuro(kakuro):
                return True
            else:
                kakuro[row][column] = BLANK_SPACE

        return False

#gets random value
def solveKakuro2(kakuro):
    if noEmptySpaces(kakuro):
        if isKakuroSolved(kakuro):
            return True
        else:
            return False
    else:
        position = getNextPosition2(kakuro)
        row = position[0]
        column = position[1]
        num1 = getNumberLeft(kakuro,position)
        num2 = getNumberUp(kakuro,position)
        #nueva funcion, lo que hace es que se va al diccionario y obtiene las cosas
        values = getValues(kakuro,position,num1,num2)
        values = getNewValues(num1,num2,values,position,kakuro)
        if values == []:
            return False
        length = len(values)
        while length != 0:
            randomValue = random.choice(values)
            values.remove(randomValue)
            kakuro[row][column] = randomValue
            if solveKakuro2(kakuro):
                return True
            else:
                kakuro[row][column] = BLANK_SPACE
            length -= 1

        return False






kakuro20x20 = [[0,0,0,0,0,0,0,0,0,0,0,[3,0],[4,0],[23,0],[7,0],0,0,0,[4,0],[17,0]],
               [0,0,0,0,0,0,0,0,0,0,[0,13],-1,-1,-1,-1,0,[11,0],[16,11],-1,-1],
               [0,[17,0],[16,0],[13,0],0,0,0,0,0,0,[0,15],-1,-1,-1,-1,[23,20],-1,-1,-1,-1],
               [[0,17],-1,-1,-1,0,[6,0],[23,0],[17,0],0,0,[16,0],[4,0],[3,26],-1,-1,-1,-1,-1,[34,0],[4,0]],
               [[0,20],-1,-1,-1,[4,20],-1,-1,-1,[7,0],[0,12],-1,-1,-1,[17,0],[0,13],-1,-1,[16,5],-1,-1],
               [0,0,[0,31],-1,-1,-1,-1,-1,-1,[24,19],-1,-1,-1,-1,[11,28],-1,-1,-1,-1,-1],
               [0,[17,0],[6,0],[0,12],-1,-1,-1,[23,11],-1,-1,0,[7,0],[17,14],-1,-1,[22,0],[0,15],-1,-1,[3,0]],
               [[0,9],-1,-1,0,0,[38,0],[4,15],-1,-1,-1,[4,13],-1,-1,[17,5],-1,-1,0,[10,11],-1,-1],
               [[0,11],-1,-1,[11,0],[0,13],-1,-1,-1,[0,35],-1,-1,-1,-1,-1,-1,-1,[16,12],-1,-1,-1],
               [0,[0,5],-1,-1,[3,16],-1,-1,-1,0,[0,4],-1,-1,[0,27],-1,-1,-1,-1,-1,0,0],
               [0,0,[0,12],-1,-1,-1,[10,0],[4,0],0,[22,0],[4,0],0,0,[23,0],[4,11],-1,-1,-1,[6,0],0],
               [0,[17,0],[22,22],-1,-1,-1,-1,-1,[16,9],-1,-1,[23,0],[0,9],-1,-1,-1,[0,3],-1,-1,[17,0]],
               [[0,14],-1,-1,-1,[0,34],-1,-1,-1,-1,-1,-1,-1,[6,16],-1,-1,-1,0,[0,11],-1,-1],
               [[0,15],-1,-1,[16,0],[0,9],-1,-1,[17,16],-1,-1,[0,17],-1,-1,-1,[24,0],[6,0],[3,0],[0,10],-1,-1],
               [0,[4,13],-1,-1,[29,0],[7,12],-1,-1,[3,0],[16,0],[4,11],-1,-1,[16,12],-1,-1,-1,[21,0],0,0],
               [[0,20],-1,-1,-1,-1,-1,[0,21],-1,-1,-1,-1,[0,25],-1,-1,-1,-1,-1,-1,[4,0],[16,0]],
               [[0,4],-1,-1,[4,12],-1,-1,[9,0],[23,10],-1,-1,-1,0,[0,17],-1,-1,-1,[0,18],-1,-1,-1],
               [0,[3,0],[4,24],-1,-1,-1,-1,-1,[4,0],[17,0],0,0,0,0,0,0,[0,19],-1,-1,-1],
               [[0,15],-1,-1,-1,-1,[0,20],-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0],
               [[0,4],-1,-1,0,0,[0,19],-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,0]]






kakuro10x10 = [[0,0,[45,0],[16,0],0,0,0,[3,0],[45,0],0],
                [0,[0,17],-1,-1,0,0,[0,7],-1,-1,0],
               [0,[17,8],-1,-1,[34,0],[17,0],[16,9],-1,-1,[4,0]],
               [[0,11],-1,-1,[0,18],-1,-1,-1,[4,5],-1,-1],
               [[0,14],-1,-1,[4,29],-1,-1,-1,-1,-1,-1],
               [0,[4,14],-1,-1,-1,[17,10],-1,-1,-1,[4,0]],
               [[0,27],-1,-1,-1,-1,-1,-1,[0,10],-1,-1],
               [[0,4],-1,-1,[17,20],-1,-1,-1,[3,7],-1,-1],
               [0,[0,12],-1,-1,0,0,[0,9],-1,-1,0],
               [0,[0,16],-1,-1,0,0,[0,3],-1,-1,0]]

kakuroExample = [[0,0,[3,0],[4,0],0],
                 [0,[5,4],-1,-1,0],
                 [[0,7],-1,-1,-1,0],
                 [0,-1,0,0,0],
                 [0,0,0,0,0]]

kakuroExampleSolved = [[0,0,[3,0],[4,0],0],
                 [0,[5,4],1,3,0],
                 [[0,7],4,2,1,0],
                 [0,1,0,0,0],
                 [0,0,0,0,0]]


superDictionary = {2:{3:[1,2],4:[1,3],5:[1,2,3,4],6:[1,2,4,5],7:[1,2,3,4,5,6],8:[1,2,3,5,6,7],9:[1,2,3,4,5,6,7,8,9],
                      10:[1,2,3,4,6,7,8,9],11:[2,3,4,5,6,7,8,9],12:[3,4,5,7,8,9],13:[4,5,6,7,8,9],14:[5,6,8,9],15:[6,7,8,9],
                      16:[7,9],17:[8,9]},
                   3:{6:[1,2,3],7:[1,2,4],8:[1,2,3,4,5],9:[1,2,3,4,5,6],10:[1,2,3,4,5,6,7],11:[1,2,3,4,5,6,7,8,9],
                      12:[1,2,3,4,5,6,7,8,9],13:[1,2,3,4,5,6,7,8,9],14:[1,2,3,4,5,6,7,8,9],15:[1,2,3,4,5,6,7,8,9],
                      16:[1,2,3,4,5,6,7,8,9],17:[1,2,3,4,5,6,7,8,9],18:[1,2,3,4,5,6,7,8,9],19:[2,3,4,5,6,7,8,9],
                      20:[3,4,5,6,7,8,9],21:[4,5,6,7,8,9],22:[5,6,7,8,9],23:[6,8,9],24:[7,8,9]},
                   4:{10:[1,2,3,4],11:[1,2,3,5],12:[1,2,3,4,5,6],13:[1,2,3,4,5,6,7],14:[1,2,3,4,5,6,7,8],15:[1,2,3,4,5,6,7,8,9],
                      15:[1,2,3,4,5,6,7,8,9],16:[1,2,3,4,5,6,7,8,9],17:[1,2,3,4,5,6,7,8,9],18:[1,2,3,4,5,6,7,8,9],19:[1,2,3,4,5,6,7,8,9],
                      20:[1,2,3,4,5,6,7,8,9],21:[1,2,3,4,5,6,7,8,9],22:[1,2,3,4,5,6,7,8,9],23:[1,2,3,4,5,6,7,8,9],24:[1,2,3,4,5,6,7,8,9],
                      25:[1,2,3,4,5,6,7,8,9],26:[2,3,4,5,6,7,8,9],27:[3,4,5,6,7,8,9],28:[4,5,6,7,8,9],29:[5,7,8,9],30:[6,7,8,9]},
                   5:{15:[1,2,3,4,5],16:[1,2,3,4,6],17:[1,2,3,4,5,6,7],18:[1,2,3,4,5,6,7,8],19:[1,2,3,4,5,6,7,8,9],20:[1,2,3,4,5,6,7,8,9],
                      21:[1,2,3,4,5,6,7,8,9],22:[1,2,3,4,5,6,7,8,9],23:[1,2,3,4,5,6,7,8,9],24:[1,2,3,4,5,6,7,8,9],25:[1,2,3,4,5,6,7,8,9],
                      26:[1,2,3,4,5,6,7,8,9],27:[1,2,3,4,5,6,7,8,9],28:[1,2,3,4,5,6,7,8,9],29:[1,2,3,4,5,6,7,8,9],30:[1,2,3,4,5,6,7,8,9],
                      31:[1,2,3,4,5,6,7,8,9],32:[2,3,4,5,6,7,8,9],33:[3,4,5,6,7,8,9],34:[4,6,7,8,9],35:[5,6,7,8,9]},
                   6:{21:[1,2,3,4,5,6],22:[1,2,3,4,5,7],23:[1,2,3,4,5,6,7,8],24:[1,2,3,4,5,6,7,8,9],25:[1,2,3,4,5,6,7,8,9],
                      26:[1,2,3,4,5,6,7,8,9],27:[1,2,3,4,5,6,7,8,9],28:[1,2,3,4,5,6,7,8,9],29:[1,2,3,4,5,6,7,8,9],30:[1,2,3,4,5,6,7,8,9],
                      31:[1,2,3,4,5,6,7,8,9],32:[1,2,3,4,5,6,7,8,9],33:[1,2,3,4,5,6,7,8,9],34:[1,2,3,4,5,6,7,8,9],35:[1,2,3,4,5,6,7,8,9],
                      36:[1,2,3,4,5,6,7,8,9],37:[1,2,3,4,5,6,7,8,9],38:[3,5,6,7,8,9],39:[4,5,6,7,8,9]},
                   7:{28:[1,2,3,4,5,6,7],29:[1,2,3,4,5,6,8],30:[1,2,3,4,5,6,7,8,9],31:[1,2,3,4,5,6,7,8,9],32:[1,2,3,4,5,6,7,8,9],33:[1,2,3,4,5,6,7,8,9],
                      34:[1,2,3,4,5,6,7,8,9],35:[1,2,3,4,5,6,7,8,9],36:[1,2,3,4,5,6,7,8,9],37:[1,2,3,4,5,6,7,8,9],38:[1,2,3,4,5,6,7,8,9],39:[1,2,3,4,5,6,7,8,9],
                      40:[1,2,3,4,5,6,7,8,9],41:[2,4,5,6,7,8,9],42:[3,4,5,6,7,8,9]},
                   8:{36:[1,2,3,4,5,6,7,8],37:[1,2,3,4,5,6,7,9],38:[1,2,3,4,5,6,8,9],39:[1,2,3,4,5,7,8,9],40:[1,2,3,4,6,7,8,9],
                      41:[1,2,3,5,6,7,8,9],42:[1,2,4,5,6,7,8,9],43:[1,3,4,5,6,7,8,9],44:[2,3,4,5,6,7,8,9]},
                   9:{45:[1,2,3,4,5,6,7,8,9]}}