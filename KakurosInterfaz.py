from tkinter import *
from tkinter import messagebox
import winsound
from PruebaKakuros import *
import copy
large_font = ('Verdana',50)

class Application(Frame):

    def callback(self,v,  *args):
        
        print (v.get(), " asfasf")
        
    def entryupdate(self, sv, i, casillas):
        try:
            if int(sv.get()) > 9:
                casillas[i].config(bg="red")
            elif int(sv.get()) > 0 and int(sv.get()) < 9:
                casillas[i].config(bg="white")
        except ValueError:
            if sv.get() == '':
                casillas[i].config(bg="white")
            else:
                #casillas[i].config(bg="red", text='')
                #winsound.Beep(1000, 100)
                sv.set('')
                #"Incorrecto",
                #"Valor inválido"
                #)
                #print ("Valor inválido")
            
            

    def createWidgets(self):
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

        kaks = [[0,[16,0],[4,0],[6,0],0,0,[4,0],[16,0],0,0,0,0,[30,0],[4,0],0,0,0,0,[23,0],[4,0]],
                [[0,13],-1,-1,-1,0,[7,8],-1,-1,0,0,0,[0,8],-1,-1,[4,0],0,0,[0,10],-1,-1],
                [[0,10],-1,-1,-1,[24,16],-1,-1,-1],
                [0,[16,0],[4,0],[6,0],0,0,[4,0],[16,0],0,0,0,0,[30,0],[4,0],0,0,0,0,[23,0],[4,0]]]
        print(len(kaks[1]))

        if self.mainWindow():
            print ("asfa")
        #nueva = self.new_window()
        #w = Scale(nueva, from_=10, to=20)
        #w.pack()

        
        
        #self.createGraphicKakuro(nueva,kakuroExample)
    def mainWindow(self):
        Label(text="Kakuros",font=("Helvetica", 13)).pack()
        Label(text="Creado por Roberto Rojas Segnini y Daniel Alvarado Bonilla").pack()
        Label(text="Seleccione el tamaño del kakuro").pack()
        
        
        w = Scale( from_=10, to=20, orient=HORIZONTAL)
        w.pack()

        Button(text="Generar kakuro", command=lambda: self.createKakuro(w.get())).pack()
        
    def new_window(self):
        self.newWindow = Toplevel(root)
        #self.newFrame = Frame(self.newWindow)
        
        return self.newWindow
    def createKakuro(self, size):
        newKak = crearMatriz(size)
        nueva = self.new_window()
        self.createGraphicKakuro(nueva,newKak) 
        
    def createGraphicKakuro(self,newWin, kakuroPorDesplegar):
        newWin.config(width=len(kakuroPorDesplegar)*100, height=len(kakuroPorDesplegar)*100)
        #newWin = self.new_window()
        photoBLACK = PhotoImage(file="BLACK.png")
        photoSLASH = PhotoImage(file="SLASH.png")
        
        cont = 0
        placeX = 50
        placeY=50
        v = StringVar()
        listaCASILLAS=[]
        aProxy = []  
        self.variablesEntry = []

        kakuroExampleSolved = [[0,0,[3,0],[4,0],0],
                         [0,[5,4],1,3,0],
                         [[0,7],4,2,1,0],
                         [0,1,0,0,0],
                         [0,0,0,0,0]]
        
        for i in range(0, len(kakuroPorDesplegar)):
            placeX = 0
            for j in range(0, len(kakuroPorDesplegar[0])):

                if kakuroPorDesplegar[i][j] == 0:
                    labelCASILLA = Label(newWin,image=photoBLACK)
                    labelCASILLA.image = photoBLACK
                    labelCASILLA.place(x=placeX, y=placeY)
                elif isinstance(kakuroPorDesplegar[i][j], list):
                    labelCASILLA = Label(newWin,image=photoSLASH)
                    labelCASILLA.image = photoSLASH
                    labelCASILLA.place(x=placeX, y=placeY)
                    if kakuroPorDesplegar[i][j][0] != 0:
                        labelNUM = Label(newWin,text=str(kakuroPorDesplegar[i][j][0]), font=("Helvetica", 13), fg="white", bg="black")
                        labelNUM.place(x=placeX+20, y=placeY+50)
                    if kakuroPorDesplegar[i][j][1] != 0:
                        labelNUM = Label(newWin,text=kakuroPorDesplegar[i][j][1], font=("Helvetica", 13), fg="white", bg="black")
                        labelNUM.place(x=placeX+52, y=placeY+20)
                        
                else:
                    
                    sizeVars = len(self.variablesEntry)
                    self.variablesEntry.append(StringVar())
                    self.variablesEntry[sizeVars].trace("w", lambda name, index, mode, var=self.variablesEntry[sizeVars], sizeVars=sizeVars:
                              self.entryupdate(var, sizeVars,listaCASILLAS))
                    
                    
                    #v = StringVar()
                    #v.trace("w", lambda *args:self.callback(v))
                    self.CASILLA = Entry(newWin,width=2,font=large_font, justify=CENTER, textvariable = self.variablesEntry[sizeVars])
                    listaCASILLAS+=[self.CASILLA]
                    
                    self.variablesEntry[sizeVars].trace("w", lambda name, index, mode, var=self.variablesEntry[sizeVars], sizeVars=sizeVars:
                              self.entryupdate(var, sizeVars, listaCASILLAS))
                    
                    self.CASILLA.place(x=placeX, y=placeY)
                    if kakuroPorDesplegar[i][j] != -1:
                        #print (kakuroPorDesplegar[i][j])
                        self.variablesEntry[-1].set(kakuroPorDesplegar[i][j])
                        
                placeX+=90
            placeY+=85

        #self.verificarButton = Button(text="Verificar solución", font=("Helvetica", 13),
                                      #command=lambda:self.verificarSolucion(listaCASILLAS,kakuroExample))
        self.verificarButton = Button(newWin,text="Verificar solución", font=("Helvetica", 13),
                                      command=lambda:self.verificarSolucion(self.variablesEntry,kakuroPorDesplegar))
        self.verificarButton.place(x=10, y=placeY+10)
        
        
        self.resolverButton = Button(newWin,text="Resolver (backtracking)", font=("Helvetica", 13),
                                      command=lambda:self.solucionarKakuro(self.variablesEntry,kakuroExampleSolved, newWin))
        self.resolverButton.place(x=200, y=placeY+10)
        
    def solucionarKakuro(self, listaCASILLAS, kakuro, _newWin):
        listaSOLUCIONES=[]
        copiaKakuroOriginal = copy.deepcopy(kakuro)

        cont = 0  
        for x in range(0, len(kakuro)):
            for y in range(0, len(kakuro[0])):
                if kakuro[x][y] == -1:
                    listaCASILLAS[cont].set(kakuro[x][y])
                    cont+=1
        self.createGraphicKakuro(_newWin,kakuro)
        #print(copiaKakuroOriginal)
        
        #solveBruteForce(copiaKakuroOriginal, [0,0])
        
    def verificarSolucion(self, listaCASILLAS, kakuro):

        listaSOLUCIONES=[]
        copiaKakuroOriginal = copy.deepcopy(kakuro)

        cont = 0  
        for x in range(0, len(kakuro)):
            for y in range(0, len(kakuro[0])):
                if kakuro[x][y] == -1:
                    copiaKakuroOriginal[x][y] = int(listaCASILLAS[cont].get())
                    cont+=1
 
        print(copiaKakuroOriginal)
        
        if isKakuroSolved(copiaKakuroOriginal):
            messagebox.showinfo (
            "Felicidades",
            "Solución correcta"
            )
        else:
            messagebox.showerror (
            "Incorrecto",
            "Solución incorrecta"
            )
            print("NOP")
                    

        
    def __init__(self, master=None):
        Frame.__init__(self, master,width=600, height=600)
        #self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
