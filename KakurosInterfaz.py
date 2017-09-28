from tkinter import *
from PruebaKakuros import * 
large_font = ('Verdana',50)

class Application(Frame):



    def createWidgets(self):
        self.createGraphicKakuro()
        

    def createGraphicKakuro(self):
        photoBLACK = PhotoImage(file="BLACK.png")
        photoSLASH = PhotoImage(file="SLASH.png")
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
        cont = 0
        placeX = 50
        placeY=50
        v = StringVar()
        listaCASILLAS=[]
        for i in range(0, len(kakuroExample)):
            placeX = 0
            for j in range(0, len(kakuroExample[0])):

                if kakuroExample[i][j] == 0:
                    labelCASILLA = Label(image=photoBLACK)
                    labelCASILLA.image = photoBLACK
                    labelCASILLA.place(x=placeX, y=placeY)
                elif isinstance(kakuroExample[i][j], list):
                    labelCASILLA = Label(image=photoSLASH)
                    labelCASILLA.image = photoSLASH
                    labelCASILLA.place(x=placeX, y=placeY)
                    if kakuroExample[i][j][0] != 0:
                        labelNUM = Label(text=str(kakuroExample[i][j][0]), font=("Helvetica", 13), fg="white", bg="black")
                        labelNUM.place(x=placeX+20, y=placeY+50)
                    if kakuroExample[i][j][1] != 0:
                        labelNUM = Label(text=kakuroExample[i][j][1], font=("Helvetica", 13), fg="white", bg="black")
                        labelNUM.place(x=placeX+52, y=placeY+20)
                else:
                    self.CASILLA = Entry(width=2,font=large_font, justify=CENTER)#, textvariable=v)
                    listaCASILLAS+=[self.CASILLA]
                    self.CASILLA.place(x=placeX, y=placeY)
                placeX+=90
            placeY+=85

        self.verificarButton = Button(text="Verificar solución", font=("Helvetica", 13),
                                      command=lambda:self.verificarSolucion(listaCASILLAS,kakuroExample))
        self.verificarButton.place(x=10, y=placeY+10)
        
        
        self.resolverButton = Button(text="Resolver (backtracking)", font=("Helvetica", 13))
        self.resolverButton.place(x=200, y=placeY+10)
        update()
        
    def verificarSolucion(self, listaCASILLAS, kakuro):
        #s = v.get()
        listaSOLUCIONES=[]
        for i in range(0, len(listaCASILLAS)):
            listaSOLUCIONES+=[listaCASILLAS[i].get()]
            #print(listaCASILLAS[i].get())
        cont = 0  
        for x in range(0, len(kakuro)):
            for y in range(0, len(kakuro[0])):
                if kakuro[x][y] == -1:
                    kakuro[x][y] = int(listaSOLUCIONES[cont])
                    cont+=1
        print(kakuroExampleSolved)
        print(kakuro)
        if kakuro == kakuroExampleSolved:
            print("SON IGUALES")
        if isKakuroSolved(kakuro):
            print("YES")
        else:
            print("NOP")
                    
     
    '''
    La funcion que revisa si esta solucionado, es simplemente encontrar un array con 2 elementos.
    Revisar si para ekl primero la suma da el numero que es y si no es falso. LISTO

    '''
    '''  
    def isKakuroSolved(self, array):
        arrayL = len(array)
        for i in range(arrayL):
            for j in range(arrayL):
                if isinstance(array[i][j],list):
                    if array[i][j][0] != 0:
                        #revisa las sumas
                        if (getSum(array,i+1,j,arrayL,True)) != array[i][j][0]:
                            print ("Nop")
                            return False
                    if array[i][j][1] != 0:
                        if (getSum(array,i,j+1,arrayL,False)) != array[i][j][1]:
                            print ("Nop")
                            return False
        print ("Yes")
        return True
    '''  
        
    def __init__(self, master=None):
        #frame = Frame(width=768, height=576, bg="", colormap="new")
        #frame.pack()

        Frame.__init__(self, master,width=600, height=600)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
