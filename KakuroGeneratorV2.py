import random


class KBoard():
    MIN_INQUIRY = 2

    def __init__(self, _size):
        if _size <= 1:
            raise Exception("Board has to be greater than 1")
        else:
            self.size = _size
            self.board = [[KCell() for x in range(self.size)] for y in range(_size)]

    def initialize(self, _data=None):
        ''' Initialize the board with the game '''
        if _data:
            ''' Usage of _data values to initialize the board '''
            pass
        else:
            ''' No data provided, then creates random game'''
            self.randomGame()
            self.print()
            self.randomGameY()

    def randomGame(self):
        for i in range(1, self.size - 1):  # let first and last row without data
            # ...
            pointer = 1

            while pointer + self.MIN_INQUIRY < self.size:
                enquiry_sum = 0
                enquiry_start = random.randrange(pointer, self.size - self.MIN_INQUIRY)
                enquiry_size = random.randrange(self.MIN_INQUIRY, self.size - enquiry_start)
                list_values = list(range(1, 10))

                for j in range(enquiry_start, enquiry_start + enquiry_size):
                    # ... checks horizontal values
                    exclude = []
                    check = 1
                    while self.board[i - check][j].getType() == KCell.CELL_DATA:
                        if list_values.count(self.board[i - check][j].getValue()):
                            list_values.remove(self.board[i - check][j].getValue())
                            exclude.append(self.board[i - check][j].getValue())
                        check += 1

                    # ... no values to assign
                    if len(list_values) == 0:
                        break

                    # ...
                    self.board[i][j].setValue(random.choice(list_values))
                    list_values.remove(self.board[i][j].getValue())
                    enquiry_sum += self.board[i][j].getValue()

                    # ... reintegrated values
                    if len(exclude) > 0:
                        list_values.extend(exclude)

                self.board[i][enquiry_start - 1].setHeader(enquiry_sum)

                # ...
                pointer += enquiry_start + enquiry_size + 1

        # ... complete the headers
        #self.print()
        #print('#############################################')
        for j in range(1, self.size):
            counter = 1
            enquiry_sum = 0
            for i in range(1, self.size):
                if self.board[i][j].getType() == KCell.CELL_DATA:
                    counter += 1
                    enquiry_sum += self.board[i][j].getValue()
                else:
                    if counter > 2:
                        self.board[i - counter][j].setHeader(enquiry_sum, KCell.CELL_RANGE_Y)
                    counter = 1
                    enquiry_sum = 0

    def randomGameY(self):

        for i in range(1, self.size - 1):  # let first and last row without data
            # ...
            pointer = 1
            contJ=0
            for j2 in range(0, self.size - 1):
                if pointer + self.MIN_INQUIRY < self.size:

                    enquiry_sum = 0
                    enquiry_start = random.randrange(pointer, self.size - self.MIN_INQUIRY)
                    enquiry_size = 0#random.randrange(self.MIN_INQUIRY, self.size - enquiry_start)
                    list_values = list(range(1, 10))
                    newValues=[]
                    if self.board[i][j2].getType() == KCell.CELL_HEADER:
                        if self.board[i][j2].header[0] == 0:
                            contI = i+1
                            while contI < self.size-1 and \
                                            self.board[contI][j2].getType() != KCell.CELL_HEADER and\
                                    self.board[contI][j2].getType() != KCell.CELL_DATA:
                                if self.board[contI][j2].getType() == KCell.CELL_DATA:
                                    newValues.append(self.board[contI][j2].getValue())
                                    print(newValues)
                                enquiry_size+=1
                                contI+=1
                            print(enquiry_size)
                            if enquiry_size>=2:
                                #enquiry_size = random.randrange(self.MIN_INQUIRY-1, enquiry_size)


                                for j in range(i+1, i+enquiry_size):
                                    # ... checks horizontal values
                                    exclude = []
                                    check = 1
                                    while self.board[j - check][j2].getType() == KCell.CELL_DATA:
                                        if list_values.count(self.board[j - check][j2].getValue()):
                                            list_values.remove(self.board[j - check][j2].getValue())
                                            exclude.append(self.board[j - check][j2].getValue())
                                        check += 1

                                    check = 1
                                    while self.board[j][j2-check].getType() == KCell.CELL_DATA:
                                        if list_values.count(self.board[j][j2-check].getValue()):
                                            list_values.remove(self.board[j][j2-check].getValue())
                                            exclude.append(self.board[j][j2-check].getValue())

                                        #if list_values.count(self.board[j - check][j2].getValue()):
                                        #    list_values.remove(self.board[j - check][j2].getValue())
                                        #    exclude.append(self.board[j][j2-check].getValue())
                                        check += 1


                                    # ... no values to assign
                                    if len(list_values) == 0:
                                        break

                                    #for element in newValues:
                                        #list_values.append(element)

                                    # ...
                                    if self.board[j][j2].getType() == KCell.CELL_UNSET:
                                        num = random.choice(list_values)
                                        newValues.append(num)
                                        self.board[j][j2].setValue(num)
                                        list_values.remove(self.board[j][j2].getValue())
                                        enquiry_sum += self.board[j][j2].getValue()

                                        # ... reintegrated values
                                        if len(exclude) > 0:
                                            list_values.extend(exclude)

                                        self.board[i][j2].setHeader(enquiry_sum,2)

                            # ...
                            pointer += enquiry_start + enquiry_size + 1

            # ... complete the headers
            #self.print()
            #print('#############################################')
            '''
            for j in range(1, self.size):
                counter = 1
                enquiry_sum = 0
                for i in range(1, self.size):
                    if self.board[i][j].getType() == KCell.CELL_DATA:
                        counter += 1
                        enquiry_sum += self.board[i][j].getValue()
                    else:
                        if counter > 2:
                            self.board[i - counter][j].setHeader(enquiry_sum, KCell.CELL_RANGE_Y)
                        counter = 1
                        enquiry_sum = 0
            '''
    def getNextUnsolvedLine(self):
        x = 0
        y = 0
        for x in range(self.size):
            for y in range(self.size):
                # ...looks for line to solve
                if self.board[x][y].getType() == KCell.CELL_HEADER:
                    # ... checks the references lines of the cell taking
                    #if self.board[x][y].getValue()[.] self.board[x][y+1].getValue()==0
                    pass

        return [x, y]

    def alreadySolved(self):
        return self.getNextUnsolvedLine() == [self.size - 1, self.size - 1]

    def print(self):
        for x in range(self.size):
            line = ""
            for y in range(self.size):
                if self.board[x][y].getType() == KCell.CELL_DATA:
                    line += " " + str(self.board[x][y]).zfill(self.size)
                elif self.board[x][y].getType() == KCell.CELL_HEADER:
                    line += " " + str(self.board[x][y]).rjust(self.size, "_")
                else:
                    line += " " + str(self.board[x][y]).ljust(self.size, "_")
                #line += " " + (str(self.board[x][y]).zfill(9) if self.board[x][y].getType() == KCell.CELL_DATA else str(self.board[x][y]))
            print(line)
    def len(self):
        return self.size

    def __len__(self):
        return self.size


class KCell():
    CELL_UNSET = 0
    CELL_DATA = 1
    CELL_HEADER = 2

    CELL_RANGE_X = 1
    CELL_RANGE_Y = 2

    def __init__(self):
        self.header = [0,0]
        self.value = None
        self.type = self.CELL_UNSET

    def setValue(self, _value):
        self.type = self.CELL_DATA
        self.value = _value

    def setHeader(self, _value, _range = CELL_RANGE_X):
        self.type = self.CELL_HEADER
        self.header[1 if _range == self.CELL_RANGE_X else 0] = _value

    def getValue(self):
        return int(self.value)

    def getType(self):
        return self.type

    def __str__(self):
        if self.type == self.CELL_DATA:
            return str(self.value)
        elif self.type == self.CELL_HEADER:
            return str(self.header)
        else:
            return "_"


try:
    print("Trying...")
    newKakuro = KBoard(20)
    newKakuro.initialize()
    newKakuro.print()

            #solve(kakuro)
except Exception as e:
    print(e)