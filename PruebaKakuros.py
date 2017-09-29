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
        while row <= arraylength and array[row][column] != 0 \
                and array[row][column] != BLANK_SPACE and not isinstance(array[row][column],list):
            sum += array[row][column]
            row += 1
    else:
        while column <= arraylength and array[row][column] != 0 \
                and array[row][column] != -BLANK_SPACE and not isinstance(array[row][column],list):
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
            return kakuroM[contRow][contCol][0]
        elif kakuroM[contRow][contCol] == 0:
            return BLACK_SPACE #-10
        contCol -= 1
    return BLACK_SPACE



def numberRepeated(number,kakuroM,position):
    contRow = position[0]
    contCol = position[1]
    while contRow >= 0:
        if not isinstance(kakuroM[contRow][contCol], list):
            if(kakuroM[contRow][contCol]) == number:
                return True
        else:
            break


    contRow = position[0]
    contCol = position[1]
    while contCol >= 0:
        if not isinstance(kakuroM[contRow][contCol], list):
            if(kakuroM[contRow][contCol]) == number:
                return True
        else:
            break

    contRow = position[0]
    contCol = position[1]
    while contCol <= len(kakuroM):
        if not isinstance(kakuroM[contRow][contCol], list):
            if(kakuroM[contRow][contCol]) == number:
                return True
        else:
            break
        contCol += 1

    contRow = position[0]
    contCol = position[1]
    while contRow <= 0:
        if not isinstance(kakuroM[contRow][contCol], list):
            if(kakuroM[contRow][contCol]) == number:
                return True
        else:
            break
        contRow += 1




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
                    #revisa las sumas
                    if (getSum(array,i+1,j,arrayL,True)) != array[i][j][0]:
                        return False
                if array[i][j][1] != 0:
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
    for i in range(len(values)-1):
        value =  values[i]
        if value < num:
            nvalues.append(value)

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
            if kakuro[row][column] == -1:
                return [row,column]
            column += 1
        row += 1


def noEmptySpaces(array):
    arrayL = len(array)
    for i in range(arrayL):
        for j in range(arrayL):
            if not isinstance(array[i][j], list) and array[i][j] == BLANK_SPACE:
                return False

    return True

def getNewValues(num1,num2,values):
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if num1 != -25 and num2 != -25:
        values2 = changeValues(num1, values)
        values3 = changeValues(num2, values2)
    elif num1 == -25 and num2 != -25:
        values3 = changeValues(num2, values)
    else:
        values3 = values

    return values3


def isValueUseful(sum,spaces,value):
    #returns True if these values can be used
    values = [1,2,3,4,5,6,7,8,9]
    index = values.index(value)
    values = values[index:]
    num = sum
    for i in range(spaces-1):
        if(i >= len(values)):
            return False
        num = num - values[i]

    if num in values:
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

'''
FALTA ARREGLARLE LA "PODA" porque dejo de servir con esta nueva version

'''
def solve(kakuro,position):
    #printMatrix(kakuro)
    #print("MATRIZZ")
    if isKakuroSolved(kakuro):
        return True
    elif noEmptySpaces(kakuro):
        return False
    else:
        #position = getPosition(kakuro)
        position = getNextPosition(kakuro,position)
        row = position[0]
        column = position[1]
        if kakuro[row][column] == BLANK_SPACE:
            num1 = getNumberLeft(kakuro,position)
            num2 = getNumberUp(kakuro,position)

            values = getNewValues(num1,num2,[1,2,3,4,5,6,7,8,9]) #solo quita si digamos es 5 el numero
            #deja del 1 al 4. Pero si el numero al que se tiene que llegar es
            #22, esta funcion no hace nada. retorna la misma lista del [1...9]
            valuesUsed = []
            cont = 0
            spaces2theRight = 9
            spacesDown = 9
            while len(valuesUsed) != len(values):
                #randomValue = random.choice(values)
                value = values[cont]
                #el number repeated es el mas importante (revisa si no se esta repitiendo el numero)
                if not numberRepeated(value, kakuro, position):
                    if num1 != 0:
                        num1 = getNewSum(kakuro,position,num1,True)
                        spaces2theRight = getSpaces(kakuro,position,True)
                    if num2 != 0:
                        num2 = getNewSum(kakuro, position, num2, False)
                        spacesDown = getSpaces(kakuro,position,False)


                    if isValueUseful(num1,spaces2theRight,value) and isValueUseful(num2,spacesDown,value):
                        kakuro[row][column] = value
                        valuesUsed.append(value)
                        if solve(kakuro,position):
                            return True
                        else:
                            kakuro[row][column] = BLANK_SPACE

                    if value not in valuesUsed:
                        valuesUsed.append(value)
                elif value not in valuesUsed:
                        valuesUsed.append(value)
                cont += 1

        return False




def solveBruteForce(kakuro,position):
    #printMatrix(kakuro)
    #print("MATRIZZ")
    if isKakuroSolved(kakuro):
        return True
    elif noEmptySpaces(kakuro):
        return False
    else:
        #position = getPosition(kakuro)
        position = getNextPosition(kakuro,position)
        row = position[0]
        column = position[1]
        if kakuro[row][column] == BLANK_SPACE:
            num1 = getNumberLeft(kakuro,position)
            num2 = getNumberUp(kakuro,position)

            values = getNewValues(num1,num2,[1,2,3,4,5,6,7,8,9]) #solo quita si digamos es 5 el numero
            #deja del 1 al 4. Pero si el numero al que se tiene que llegar es
            #22, esta funcion no hace nada. retorna la misma lista del [1...9]
            valuesUsed = []
            cont = 0
            while len(valuesUsed) != len(values):
                #randomValue = random.choice(values)
                value = values[cont]
                #el number repeated es el mas importante (revisa si no se esta repitiendo el numero)
                if not numberRepeated(value, kakuro, position):
                    kakuro[row][column] = value
                    valuesUsed.append(value)
                    if solveBruteForce(kakuro,position):
                        return True
                    else:
                        kakuro[row][column] = BLANK_SPACE

                elif value not in valuesUsed:
                        valuesUsed.append(value)
                cont += 1

        return False






#printMatrix(createEmptyMatrix())

#if solveK(kakuroExample,10):
#    print("HOLA")


#arrayPrueba = [[0,45],1,2,3,4,5,6,7,8,9]
#print (getSum(arrayPrueba,0,1,len(arrayPrueba),False))

#print(getNumberUp(kakuroExample,[1,2]))
#print(getNumberLeft(kakuroExample,[1,2]))



#if isKakuroSolved(kakuroExampleSolved):
#    print("HOLAAAAAAA")
print(getSpaces(kakuroExample,[1,2],True))
if (solveBruteForce(kakuroExample,[0,0])):
    print("solucionado")

def decision(probability):
    r = random.random()
    return r < probability



#kakuro = generateKakuro(10)
#printMatrix(kakuro)
##values = [1,2,3,4,5,6,7,8,9]
#print(len(values))
#print(values[2:])
#print(isValueUseful(17,2,8))