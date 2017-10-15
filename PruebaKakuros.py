
import random
from KakuroGenerator import *
#from NewSolver import *
import datetime
timesFinished = 0

CombinationsDic = {2:{3:[[1,2]],
                      4:[[1,3]],
                      5:[[1,4],[2,3]],
                      6:[[1,5],[2,4]],
                      7:[[1,6],[2,5],[3,4]],
                      8:[[1,7],[2,6],[3,5]],
                      9:[[1,8],[2,7],[3,6],[4,5]],
                      10:[[1,9],[2,8],[3,7],[4,6]],
                      11:[[2,9],[3,8],[4,7],[5,6]],
                      12:[[3,9],[4,8],[5,7]],
                      13:[[4,9],[5,8],[6,7]],
                      14:[[5,9],[6,8]],
                      15:[[6,9],[7,8]],
                      16:[[7,9]],
                      17:[[8,9]]},

                   3: {6:[[1,2,3]],
                       7:[[1,2,4]],
                       8:[[1,2,3],[1,3,4]],
                       9:[[1,2,6],[1,3,5],[2,3,4]],
                       10:[[1,2,7],[1,3,6],[1,4,5],[2,3,5]],
                       11:[[1,2,8],[1,3,7],[1,4,6],[2,3,6],[2,4,5]],
                       12:[[1,2,9],[1,3,8],[1,4,7],[1,5,6],[2,3,7],[2,4,6],[3,4,5]],
                       13:[[1,3,9],[1,4,8],[1,5,7],[2,3,8],[2,4,7],[2,5,6],[3,4,6]],
                       14:[[1,4,9],[1,5,8],[1,6,7],[2,3,9],[2,4,8],[2,5,7],[3,4,7],[3,5,6]],
                       15:[[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]],
                       16:[[1,6,9],[1,7,8],[2,5,9],[2,6,8],[3,4,9],[3,5,8],[3,6,7],[4,5,7]],
                       17:[[1,7,9],[2,6,9],[2,7,8],[3,5,9],[3,6,8],[4,5,8],[4,6,7]],
                       18:[[1,8,9],[2,7,9],[3,6,9],[3,7,8],[4,5,9],[4,6,8],[5,6,7]],
                       19:[[2,8,9],[3,7,9],[4,6,9],[4,7,8],[5,6,8]],
                       20:[[3,8,9],[4,7,9],[5,6,9],[5,7,8]],
                       21:[[4,8,9],[5,7,9],[6,7,8]],
                       22:[[5,8,9],[6,7,9]],
                       23:[[6,8,9]],
                       24:[[7,8,9]]},

                   4: {10:[[1,2,3,4]],
                       11:[[1,2,3,5]],
                       12:[[1,2,3,6],[1,2,4,5]],
                       13:[[1,2,3,7],[1,2,4,6],[1,2,4,5]],
                       14:[[1,2,3,8],[1,2,4,7],[1,2,5,6],[1,3,4,6],[2,3,4,5]],
                       15:[[1,2,3,9],[1,2,4,8],[1,2,5,7],[1,3,4,7],[1,3,5,6],[2,3,4,6]],
                       16:[[1,2,4,9],[1,2,5,8],[1,2,6,7],[1,2,4,8],[1,3,5,7],[1,4,5,6],[2,3,4,7],[2,3,5,6]],
                       17:[[1,2,5,9],[1,2,6,8],[1,3,4,9],[1,3,5,8],[1,3,6,7],[1,4,5,7],[2,3,4,8],[2,3,5,7],[2,4,5,6]],
                       18:[[1,2,6,9],[1,2,7,8],[1,3,5,9],[1,3,6,8],[1,4,5,8],[1,4,6,7],[2,3,4,9],[2,3,5,8],[2,3,6,7],[2,4,5,7],[3,4,5,6]],
                       19:[[1,2,7,9],[1,3,6,9],[1,3,7,8],[1,4,5,9],[1,4,6,8],[1,5,6,7],[2,3,5,9],[2,3,6,8],[2,4,5,8],[2,4,6,7],[3,4,5,7]],
                       20:[[1,2,8,9],[1,3,7,9],[1,4,6,9],[1,4,7,8],[1,5,6,8],[2,3,6,9],[2,3,7,8],[2,4,5,9],[2,4,6,8],[2,5,6,7],[3,4,5,8],[3,4,6,7]],
                       21:[[1,3,8,9],[1,4,7,9],[1,5,6,9],[1,5,7,8],[2,3,7,9],[2,4,6,9],[2,4,7,8],[2,5,6,8],[3,4,5,9],[3,4,6,8],[3,5,6,7]],
                       22:[[1,4,8,9],[1,5,7,9],[1,6,7,8],[2,3,8,9],[2,4,7,9],[2,5,6,9],[2,5,7,8],[3,4,6,9],[3,4,7,8],[3,5,6,8],[4,5,6,7]],
                       23:[[1,5,8,9],[1,6,7,9],[2,4,8,9],[2,5,7,9],[2,6,7,8],[3,4,7,9],[3,5,6,9],[3,5,7,8],[4,5,6,8]],
                       24:[[1,6,8,9],[2,5,8,9],[2,6,7,9],[3,4,8,9],[3,5,7,9],[3,6,7,8],[4,5,6,9],[4,5,7,8]],
                       25:[[1,7,8,9],[2,6,8,9],[3,5,8,9],[3,6,7,9],[4,5,7,9],[4,6,7,8]],
                       26:[[2,7,8,9],[3,6,8,9],[4,5,8,9],[4,6,7,9],[5,6,7,8]],
                       27:[[3,7,8,9],[4,6,8,9],[5,6,7,9]],
                       28:[[4,7,8,9],[5,6,8,9]],
                       29:[[5,7,8,9]],
                       30:[[6,7,8,9]]},

                   5: {15:[[1,2,3,4,5]],
                       16:[[1,2,3,4,6]],
                       17:[[1,2,3,4,7],[1,2,3,5,6]],
                       18:[[1,2,3,4,8],[1,2,3,5,7],[1,2,4,5,6]],
                       19:[[1,2,3,4,9],[1,2,3,5,8],[1,2,3,6,7],[1,2,4,5,7],[1,3,4,5,6]],
                       20:[[1,2,3,5,9],[1,2,3,6,8],[1,2,4,5,8],[1,2,4,6,7],[1,3,4,5,7],[2,3,4,5,6]],
                       21:[[1,2,3,6,9],[1,2,3,7,8],[1,2,4,5,9],[1,2,4,6,8],[1,2,5,6,7],[1,3,4,5,8],[1,3,4,6,7],[2,3,4,5,7]],
                       22:[[1,2,3,7,9],[1,2,4,6,9],[1,2,4,7,8],[1,2,5,6,8],[1,3,4,5,9],[1,3,4,6,8],[1,3,5,6,7],[2,3,4,5,8],[2,3,4,6,7]],
                       23:[[1,2,3,8,9],[1,2,4,7,9],[1,2,5,6,9],[1,2,5,7,8],[1,3,4,6,9],[1,3,4,7,8],[1,3,5,6,8],[1,4,5,6,7],[2,3,4,5,9],[2,3,4,6,8],[2,3,5,6,7]],
                       24:[[1,2,4,8,9],[1,2,5,7,9],[1,2,6,7,8],[1,3,4,7,9],[1,3,5,6,9],[1,3,5,7,8],[1,4,5,6,8],[2,3,4,6,9],[2,3,4,7,8],[2,3,5,6,8],[2,4,5,6,7]],
                       25:[[1,2,5,8,9],[1,2,6,7,9],[1,3,4,8,9],[1,3,5,7,9],[1,3,6,7,8],[1,4,5,6,9],[1,4,5,7,8],[2,3,4,7,9],[2,3,5,6,9],[2,3,5,7,8],[2,4,5,6,8],[3,4,5,6,7]],
                       26:[[1,2,6,8,9],[1,3,5,8,9],[1,3,6,7,9],[1,4,5,7,9],[1,4,6,7,8],[2,3,4,8,9],[2,3,5,7,9],[2,3,6,7,8],[2,4,5,6,9],[2,4,5,7,8],[3,4,5,6,8]],
                       27:[[1,2,7,8,9],[1,3,6,8,9],[1,4,5,8,9],[1,4,6,7,9],[1,5,6,7,8],[2,3,5,8,9],[2,3,6,7,9],[2,4,5,7,9],[2,4,6,7,8],[3,4,5,6,9],[3,4,5,7,8]],
                       28:[[1,3,7,8,9],[1,4,6,8,9],[1,5,6,7,9],[2,3,6,8,9],[2,4,5,8,9],[2,4,6,7,9],[2,5,6,7,8],[3,4,5,7,9],[3,4,6,7,8]],
                       29:[[1,4,7,8,9],[1,5,6,8,9],[2,3,7,8,9],[2,4,6,8,9],[2,5,6,7,9],[3,4,5,8,9],[3,4,6,7,9],[3,5,6,7,8]],
                       30:[[1,5,7,8,9],[2,4,7,8,9],[2,5,6,8,9],[3,4,6,8,9],[3,5,6,7,9],[4,5,6,7,8]],
                       31:[[1,6,7,8,9],[2,5,7,8,9],[3,4,7,8,9],[3,5,6,8,9],[4,5,6,7,9]],
                       32:[[2,6,7,8,9],[3,5,7,8,9],[4,5,6,8,9]],
                       33:[[3,6,7,8,9],[4,5,7,8,9]],
                       34:[[4,6,7,8,9]],
                       35:[[5,6,7,8,9]]},

                   6: {21:[[1,2,3,4,5,6]],
                       22:[[1,2,3,4,5,7]],
                       23:[[1,2,3,4,5,8],[1,2,3,4,6,7]],
                       24:[[1,2,3,4,5,9],[1,2,3,4,6,8],[1,2,3,5,6,7]],
                       25:[[1,2,3,4,6,9],[1,2,3,4,7,8],[1,2,3,5,6,8],[1,2,4,5,6,7]],
                       26:[[1,2,3,4,7,9],[1,2,3,5,6,9],[1,2,3,5,7,8],[1,2,4,5,6,8],[1,3,4,5,6,7]],
                       27:[[1,2,3,4,8,9],[1,2,3,5,7,9],[1,2,3,6,7,8],[1,2,4,5,6,9],[1,2,4,5,7,8],[1,3,4,5,6,8],[2,3,4,5,6,7]],
                       28:[[1,2,3,5,8,9],[1,2,3,6,7,9],[1,2,4,5,7,9],[1,2,4,6,7,8],[1,3,4,5,6,9],[1,3,4,5,7,8],[2,3,4,5,6,8]],
                       29:[[1,2,3,6,8,9],[1,2,4,5,8,9],[1,2,4,6,7,9],[1,2,5,6,7,8],[1,3,4,5,7,9],[1,3,4,6,7,8],[2,3,4,5,6,9],[2,3,4,5,7,8]],
                       30:[[1,2,3,7,8,9],[1,2,4,6,8,9],[1,2,5,6,7,9],[1,3,4,5,8,9],[1,3,4,6,7,9],[1,3,5,6,7,8],[2,3,4,5,7,9],[2,3,4,6,7,8]],
                       31:[[1,2,4,7,8,9],[1,2,5,6,8,9],[1,3,4,6,8,9],[1,3,5,6,7,9],[1,4,5,6,7,8],[2,3,4,5,8,9],[2,3,4,6,7,9],[2,3,5,6,7,8]],
                       32:[[1,2,5,7,8,9],[1,3,4,7,8,9],[1,3,5,6,8,9],[1,4,5,6,7,9],[2,3,4,6,8,9],[2,3,5,6,7,9],[2,4,5,6,7,8]],
                       33:[[1,2,6,7,8,9],[1,3,5,7,8,9],[1,4,5,6,8,9],[2,3,4,7,8,9],[2,3,5,6,8,9],[2,4,5,6,7,9],[3,4,5,6,7,8]],
                       34:[[1,3,6,7,8,9],[1,4,5,7,8,9],[2,3,5,7,8,9],[2,4,5,6,8,9],[3,4,5,6,7,9]],
                       35:[[1,4,6,7,8,9],[2,3,6,7,8,9],[2,4,5,7,8,9],[3,4,5,6,8,9]],
                       36:[[1,5,6,7,8,9],[2,4,6,7,8,9],[3,4,5,7,8,9]],
                       37:[[2,5,6,7,8,9],[3,4,6,7,8,9]],
                       38:[[3,5,6,7,8,9]],
                       39:[[4,5,6,7,8,9]]},

                   7: {28:[[1,2,3,4,5,6,7]],
                       29:[[1,2,3,4,5,6,8]],
                       30:[[1,2,3,4,5,6,9],[1,2,3,4,5,7,8]],
                       31:[[1,2,3,4,5,7,9],[1,2,3,4,6,7,8]],
                       32:[[1,2,3,4,5,8,9],[1,2,3,4,6,7,9],[1,2,3,5,6,7,8]],
                       33:[[1,2,3,4,6,8,9],[1,2,3,5,6,7,9],[1,2,4,5,6,7,8]],
                       34:[[1,2,3,4,7,8,9],[1,2,3,5,6,8,9],[1,2,4,5,6,7,9],[1,3,4,5,6,7,8]],
                       35:[[1,2,3,5,7,8,9],[1,2,4,5,6,8,9],[1,3,4,5,6,7,9],[2,3,4,5,6,7,8]],
                       36:[[1,2,3,6,7,8,9],[1,2,4,5,7,8,9],[1,3,4,5,6,8,9],[2,3,4,5,6,7,9]],
                       37:[[1,2,4,6,7,8,9],[1,3,4,5,7,8,9],[2,3,4,5,6,8,9]],
                       38:[[1,2,5,6,7,8,9],[1,3,4,6,7,8,9],[2,3,4,5,7,8,9]],
                       39:[[1,3,5,6,7,8,9],[2,3,4,6,7,8,9]],
                       40:[[1,4,5,6,7,8,9],[2,3,5,6,7,8,9]],
                       41:[[2,4,5,6,7,8,9]],
                       42:[[3,4,5,6,7,8,9]]},

                   8: {36:[[1,2,3,4,5,6,7,8]],
                       37:[[1,2,3,4,5,6,7,9]],
                       38:[[1,2,3,4,5,6,8,9]],
                       39:[[1,2,3,4,5,7,8,9]],
                       40:[[1,2,3,4,6,7,8,9]],
                       41:[[1,2,3,5,6,7,8,9]],
                       42:[[1,2,4,5,6,7,8,9]],
                       43:[[1,3,4,5,6,7,8,9]],
                       44:[[2,3,4,5,6,7,8,9]]},

                   9: {45:[[1,2,3,4,5,6,7,8,9]]}}

'''
MEGA DICTIONARY
'''

masterDictionary = {2:{3:[[1,2]],4:[[1,3]],5:[[1,4],[2,3]],6:[[1,5],[2,4]]},3:{},4:{},5:{},6:{},7:{},8:{},9:{}}

superDictionary = {2:{3:[1,2],4:[1,3],5:[1,2,3,4],6:[1,2,4,5],7:[1,2,3,4,5,6],8:[1,2,3,5,6,7],9:[1,2,3,4,5,6,7,8,9],
                      10:[1,2,3,4,6,7,8,9],11:[2,3,4,5,6,7,8,9],12:[3,4,5,7,8,9],13:[4,5,6,7,8,9],14:[5,6,8,9],15:[6,7,8,9],
                      16:[7,9],17:[8,9]},
                   3:{6:[1,2,3],7:[1,2,4],8:[1,2,3,4,5],9:[1,2,3,4,5,6],10:[1,2,3,4,5,6,7],11:[1,2,3,4,5,6,7,8,9],
                      12:[1,2,3,4,5,6,7,8,9],13:[1,2,3,4,5,6,7,8,9],14:[1,2,3,4,5,6,7,8,9],15:[1,2,3,4,5,6,7,8,9],
                      16:[1,2,3,4,5,6,7,8,9],17:[1,2,3,4,5,6,7,8,9],18:[1,2,3,4,5,6,7,8,9],19:[2,3,4,5,6,7,8,9],
                      20:[3,4,5,6,7,8,9],21:[4,5,6,7,8,9],22:[5,6,7,8,9],23:[6,8,9],24:[7,8,9]},
                   4:{10:[1,2,3,4],11:[1,2,3,5],12:[1,2,3,4,5,6],13:[1,2,3,4,5,6,7],14:[1,2,3,4,5,6,7,8],15:[1,2,3,4,5,6,7,8,9],
                      16:[1,2,3,4,5,6,7,8,9],16:[1,2,3,4,5,6,7,8,9],17:[1,2,3,4,5,6,7,8,9],18:[1,2,3,4,5,6,7,8,9],19:[1,2,3,4,5,6,7,8,9],
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

'''
CONSTANTS DECLARATION
'''

BLACK_SPACE = -25
BLANK_SPACE = -1



# print (random.randint(0,9))






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

kakuroExampleSolved = [[0,0,[3,0],[4,0],0],
                 [0,[5,4],1,3,0],
                 [[0,7],4,2,1,0],
                 [0,1,0,0,0],
                 [0,0,0,0,0]]



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

            values = getNewValues(num1,num2,[1,2,3,4,5,6,7,8,9],position,kakuro) #solo quita si digamos es 5 el numero
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

            values = getNewValues(num1,num2,[1,2,3,4,5,6,7,8,9],position,kakuro) #solo quita si digamos es 5 el numero
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
#print(getSpaces(kakuroExample,[1,2],True))

#if (solveBruteForce(kakuroExample,[0,0])):
#    print("solucionado")

#if (solve(kakuroExample,[0,0])):
#    print("solucionado")




def decision(probability):
    r = random.random()
    return r < probability



#kakuro = generateKakuro(10)
#printMatrix(kakuro)
##values = [1,2,3,4,5,6,7,8,9]
#print(len(values))
#print(values[2:])
#print(isValueUseful(17,2,8))
################################################
################################################
################################################
################################################
################################################
################################################
################################################
################################################
################################################

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
    if sum1 == BLACK_SPACE and sum2 == BLACK_SPACE: return values
    if sum1 != BLACK_SPACE: sum1 = getNewSum(kakuro, position, sum1, True)
    if sum2 != BLACK_SPACE: sum2 = getNewSum(kakuro, position, sum2, False)

    spacesRight = getSpaces(kakuro,position,True)
    spacesDown = getSpaces(kakuro,position,False)
    if spacesDown == 1 and sum2 == BLACK_SPACE:
        spacesDown = 0
    if spacesRight == 1 and sum1 == BLACK_SPACE:
        spacesRight = 0
    if spacesRight == 1 or spacesDown == 1:
        if sum1 == BLACK_SPACE and sum2 != BLACK_SPACE:
            minValue = sum2
        elif sum2 == BLACK_SPACE and sum1 != BLACK_SPACE:
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
        if isinstance(_kakuro[contRow][contCol], list) and _kakuro[contRow][contCol][0] != 0:
            spacesSumUp = getSpaces4getValues(_kakuro,[contRow+1,contCol],False)
            break
        elif _kakuro[contRow][contCol] == 0:
            spacesSumUp = BLACK_SPACE  # -10
            break
        contRow -= 1



    contRow = _position[0]
    contCol = _position[1]
    while contCol >= 0:
        if isinstance(_kakuro[contRow][contCol], list) and _kakuro[contRow][contCol][1] != 0:
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
    elif leftSum == 0:
        values = superDictionary[spacesSumUp][upSum]
    elif upSum == 0:
        values = superDictionary[spacesSumLeft][leftSum]
    else:
        values1 = superDictionary[spacesSumUp][upSum]
        values2 = superDictionary[spacesSumLeft][leftSum]
        values = getIntersection(values1,values2)
    return values



def solveKakuro(kakuro):
    if noEmptySpaces(kakuro):
        if isKakuroSolved(kakuro):
            return True
        else:
            return False
    else:
        position = getNextPosition2(kakuro)
        # position == [19,10] or position == [16,10] or kakuro[1][9] == 8
        row = position[0]
        column = position[1]
        num1 = getNumberLeft(kakuro, position)
        if num1 == 0: num1 = -25
        num2 = getNumberUp(kakuro, position)
        if num2 == 0: num2 = -25
        values = getValues(kakuro, position, num1, num2)
        # values = getValuesList(num1,num2,kakuro,position)
        #values = getIntersection(getValues(kakuro,position,num1,num2),getValuesList(num1,num2,kakuro,position))
        #values = getNewValues(num1, num2, sorted(values), position, kakuro)
        values = deleteRepeatedValues2(kakuro,getIntersection(getValues(kakuro,position,num1,num2),getValuesList(num1,num2,kakuro,position)),position)
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

def substractVal(kakuro,position,sum,left):
    newSum = 0
    newSpaces = 0
    spaces = 0
    if left:
        contRow = position[0]
        contCol = position[1]
        while contCol >= 0:
            if isinstance(kakuro[contRow][contCol], list):
                spaces = getSpaces4getValues(kakuro, [contRow, contCol + 1], True)
                break
            contCol -= 1
        contCol += 1

        for i in range(spaces):
            if kakuro[contRow][contCol + i] != -1:
                newSpaces += 1
                newSum += kakuro[contRow][contCol + i]
        newSum = sum - newSum
        newSpaces = spaces - newSpaces

    else:
        contRow = position[0]
        contCol = position[1]
        while contRow >= 0:
            if isinstance(kakuro[contRow][contCol], list):
                spaces = getSpaces4getValues(kakuro, [contRow + 1, contCol], False)
                break
            contRow -= 1
        contRow += 1

        for i in range(spaces):
            if kakuro[contRow + i][contCol] != -1:
                newSpaces += 1
                newSum += kakuro[contRow + i][contCol]
        newSum = sum - newSum
        newSpaces = spaces - newSpaces


    return newSum,newSpaces


def getValuesList(leftSum,upSum,kakuro,position):
    sumUp,spacesUp = substractVal(kakuro,position,upSum,False)
    sumLeft, spacesLeft = substractVal(kakuro, position, leftSum, True)

    valuesUp = list(range(1, 10))
    valuesLeft = list(range(1, 10))


    if sumUp != -25:
        if spacesUp == 1:
            return [min(sumLeft,sumUp)]
        try:
            combU = CombinationsDic[spacesUp][sumUp]
        except KeyError:
            return []
        valuesLeft = []
        for combination in combU:
            for value in combination:
                valuesLeft.append(value)
    if sumLeft != -25:
        if spacesLeft == 1:
            return [min(sumLeft,sumUp)]

        try:
            combL = CombinationsDic[spacesLeft][sumLeft]
        except KeyError:
            return []
        valuesUp = []
        for combination in combL:
            for value in combination:
                valuesUp.append(value)

    return getIntersection(valuesLeft,valuesUp)

def solveKakuro2(kakuro):
    #kakuro[12][1] == 9 and kakuro[12][2] == 4 and kakuro[12][3] == 1 and kakuro[12][5] == 6 and kakuro[12][13] == 9 and kakuro[12][14] == 3 and kakuro[12][15] == 4 and kakuro[12][18] == 3 and kakuro[13][2] == 7 and kakuro[13][9] == 9 and kakuro[13][11] == 6 and kakuro[13][12] == 3 and kakuro[14][2] == 6 and kakuro[14][3] == 7 and kakuro[14][11] == 9 and kakuro[14][12] == 2 and kakuro[14][14] == 9 and kakuro[14][15] == 2 and kakuro[15][1] == 3 and kakuro[15][2] == 2 and kakuro[15][3] == 9 and kakuro[15][7] == 8 and kakuro[15][8] ==1 and kakuro[15][13] == 7 and kakuro[15][14] ==8 and kakuro[15][16] == 2
    if noEmptySpaces(kakuro):
        if isKakuroSolved(kakuro):
            return True
        else:
            return False
    else:
        position = getNextPosition2(kakuro)
        #position == [19,10] or position == [16,10] or kakuro[1][9] == 8
        row = position[0]
        column = position[1]
        num1 = getNumberLeft(kakuro,position)
        if num1 == 0: num1 = -25
        num2 = getNumberUp(kakuro,position)
        if num2 == 0: num2= -25
        values = getValues(kakuro,position,num1,num2)
        #values = getValuesList(num1,num2,kakuro,position)
        #values = getIntersection(getValues(kakuro,position,num1,num2),getValuesList(num1,num2,kakuro,position))
        values = getNewValues(num1,num2,sorted(values),position,kakuro)
        #values = deleteRepeatedValues2(kakuro,values,position)
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





def createEmptyMatrix(size):
    mLength = size
    newMatrix = []
    for x in range(mLength):
        newList = []
        newMatrix.append(newList)
        for y in range(mLength):
            newList.append(0)

    return newMatrix


def createUpSums(_kakuro):
    values = list(range(1, 10))
    for i in range(len(_kakuro)):
        for j in range(len(_kakuro)):
            position = 1
            enquiry_sum = 0
            if ((i+position) < len(_kakuro)) and _kakuro[i+position][j] in values:
                while _kakuro[i+position][j] in values:
                    enquiry_sum += _kakuro[i+position][j]
                    position += 1
            if isinstance(_kakuro[i][j],list):
                _kakuro[i][j][0] = enquiry_sum
            else:
                _kakuro[i][j] = [enquiry_sum,0]




def createKakuro(_size):

    kakuroBoard = createEmptyMatrix(_size)
    for i in range(1, _size - 1):  # let first and last row without data
    # ...
        pointer = 1

        while pointer + 2 < _size:
            enquiry_sum = 0
            enquiry_start = random.randrange(pointer, _size - 2)
            enquiry_size = random.randrange(2, _size - enquiry_start)
            list_values = list(range(1, 10))

            for j in range(enquiry_start, enquiry_start + enquiry_size):
                # ... checks horizontal values
                exclude = []
                check = 1
                while kakuroBoard[i - check][j]== 0 and check < _size:
                    if list_values.count(kakuroBoard[i - check][j]):
                        list_values.remove(kakuroBoard[i - check][j])
                        exclude.append(kakuroBoard[i - check][j])
                    check += 1

                # ... no values to assign
                if len(list_values) == 0:
                    break

                # ...
                kakuroBoard[i][j] = (random.choice(list_values))
                list_values.remove(kakuroBoard[i][j])
                enquiry_sum += kakuroBoard[i][j]

                # ... reintegrated values
                if len(exclude) > 0:
                    list_values.extend(exclude)

            kakuroBoard[i][enquiry_start - 1] = [0,(enquiry_sum)]

            # ...
            pointer += enquiry_start + enquiry_size + 1

    createUpSums(kakuroBoard)

    '''for j in range(1, _size):
        counter = 1
        enquiry_sum = 0
        for i in range(1, _size):
            if kakuroBoard[i][j] != 0 and not isinstance(kakuroBoard[i][j],list):
                counter += 1
                enquiry_sum += kakuroBoard[i][j]
            else:
                if counter > 2 and isinstance(kakuroBoard[i - counter][j],list):
                    kakuroBoard[i - counter][j][0] = enquiry_sum
                counter = 1
                enquiry_sum = 0
    '''

    return kakuroBoard



def unSolveKakuro(_kakuro):
    for i in range (len(_kakuro)):
        for j in range (len(_kakuro)):
            if _kakuro[i][j] in [1,2,3,4,5,6,7,8,9]:
                _kakuro[i][j] = -1


#print(kakuro20x20[0][5],kakuro20x20[1][5],kakuro20x20[2][5],kakuro20x20[3][5],kakuro20x20[4][5])

#if (solveKakuro2(kakuro20x20)):
#    print("solucionado")


kakuroHard = [[0,0,[7,0],[17,0],0,0,0,0,0,[17,0],[28,0],0,0,0,[3,0],[4,0],[16,0],0,[7,0],[23,0]],
              [0,[16,13],-1,-1,[4,0],0,[23,0],[4,0],[16,11],-1,-1,0,0,[0,10],-1,-1,-1,[24,13],-1,-1],
              [[0,20],-1,-1,-1,-1,[19,30],-1,-1,-1,-1,-1,[4,0],0,[0,29],-1,-1,-1,-1,-1,-1],
              [[0,10],-1,-1,[0,27],-1,-1,-1,-1,-1,[3,5],-1,-1,0,[16,0],[3,0],0,[23,18],-1,-1,-1],
              [0,0,0,0,[29,14],-1,-1,0,[23,14],-1,-1,-1,[8,10],-1,-1,[6,16],-1,-1,0,0],
              [0,0,0,[0,10],-1,-1,0,[4,14],-1,-1,-1,[6,24],-1,-1,-1,-1,-1,[39,0],[6,0],0],
              [0,0,[8,0],[44,9],-1,-1,[0,12],-1,-1,[30,0],[0,4],-1,-1,0,[3,12],-1,-1,-1,-1,0],
              [0,[0,14],-1,-1,-1,0,[0,16],-1,-1,-1,[16,3],-1,-1,[4,3],-1,-1,[7,6],-1,-1,0],
              [0,[0,20],-1,-1,-1,0,0,0,[7,20],-1,-1,-1,[24,4],-1,-1,[0,6],-1,-1,-1,0],
              [0,[0,12],-1,-1,[24,0],0,0,[0,15],-1,-1,-1,[29,10],-1,-1,0,[0,9],-1,-1,0,0],
              [0,0,[0,12],-1,-1,0,0,[16,13],-1,-1,[3,17],-1,-1,0,0,[0,11],-1,-1,[6,0],0],
              [0,0,[6,11],-1,-1,0,[3,10],-1,-1,[23,14],-1,-1,-1,0,0,0,[30,10],-1,-1,0],
              [0,[0,19],-1,-1,-1,[7,9],-1,-1,[17,18],-1,-1,-1,[12,0],[16,0],0,[0,10],-1,-1,-1,0],
              [0,[0,5],-1,-1,[24,3],-1,-1,[0,13],-1,-1,[0,18],-1,-1,-1,0,[30,18],-1,-1,-1,0],
              [0,[0,14],-1,-1,-1,-1,[16,0],[4,17],-1,-1,[35,0],[17,8],-1,-1,[0,14],-1,-1,0,0,0],
              [0,0,0,[7,24],-1,-1,-1,-1,-1,[4,23],-1,-1,-1,0,[7,13],-1,-1,0,0,0],
              [0,[23,0],[6,8],-1,-1,[0,10],-1,-1,[0,19],-1,-1,-1,[17,0],[4,10],-1,-1,[3,0],0,[23,0],[3,0]],
              [[0,13],-1,-1,-1,[16,0],[3,0],[17,0],0,[0,10],-1,-1,[4,26],-1,-1,-1,-1,-1,[16,7],-1,-1],
              [[0,28],-1,-1,-1,-1,-1,-1,0,0,[0,19],-1,-1,-1,-1,-1,[0,20],-1,-1,-1,-1],
              [[0,11],-1,-1,[0,19],-1,-1,-1,0,0,[0,9],-1,-1,0,0,0,0,[0,16],-1,-1,0]]

kakuroTest = [[0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,[17,0],0],
              [0,0,0,0,0,0,0,0,0,-1,0],
              [[0,45],-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0]
              ]

#kakuroo = KBoard(10)
#kakuroo.initialize()
#kakuroo.print()
#kakuroBOARD = convertirKakuro(kakuroo)
print(datetime.datetime.now().time())
if solveKakuro(kakuroHard):
    print("Solucionado")
    print(datetime.datetime.now().time())
    #print(getLowestValue(30,5))


#