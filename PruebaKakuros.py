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


sumaAleatoria(4)
        


#PRUEBAS PRUEBAS Y PRUEBAS

import random



'''
CONSTANTS DECLARATION
'''

BLACK_SPACE = -25

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

#crearMatriz()

kakuroExample = [[0,0,[3,0],[4,0],0],
                 [0,[5,4],-1,-1,0],
                 [[0,7],-1,-1,-1,0],
                 [0,-1,0,0,0],
                 [0,0,0,0,0]]


def getSum(array,row,column,arraylength,down): #position is an array of two elements
    sum = 0
    if down:
        while row <= arraylength and array[row][column] != 0 and not isinstance(array[row][column]):
            sum += array[row][column]
            row += 1
    else:
        while column <= arraylength and array[row][column] != 0 and not isinstance(array[row][column]):
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


def getValues(kakuroM,position):
    sumNumUp = getNumberUp(kakuroM,position)
    sumNumLeft = getNumberLeft(kakuroM,position)
    valuesDictionary = {3:{1,2},4:{1,3},5:[1,2,3,4]}

    if sumNumLeft != BLACK_SPACE and sumNumUp != BLACK_SPACE:
        #quiere decir que es una interseccion,por esta razon hay menos posibilidades de colocar un numero ahi



        x = 10



'''

def solve(_kakuro,position ): #position is an array with to elements, i,j.
    if not kakuroSolved(_kakuro):
        return True
    else:

        values = [calculate possible legal values for that field]
        for value in values:
            kakuro[position] = value
            solve(_kakuro)
        kakuro[position]
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


def getSum(array,row,column,arraylength,down): #position is an array of two elements
    sum = 0
    if down:
        while row <= arraylength and array[row][column] != 0 \
                and array[row][column] != -1 and not isinstance(array[row][column],list):
            sum += array[row][column]
            row += 1
    else:
        while column <= arraylength and array[row][column] != 0 \
                and array[row][column] != -1 and not isinstance(array[row][column],list):
            sum += array[row][column]
            column += 1

    return sum


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


if isKakuroSolved(kakuroExampleSolved):
    print("KAKURO SOLUCIONADO")


