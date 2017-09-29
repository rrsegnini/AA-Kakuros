from tkinter import *
from PruebaKakuros import *
import copy
large_font = ('Verdana',50)

class Application(Frame):

    def callback(self,v,  *args):
        
        print (v.get(), " asfasf")
        
    def entryupdate(self, sv, i, casillas):
        if int(sv.get()) > 9:
            casillas[i].config(bg="red")
        elif int(sv.get()) > 0 and int(sv.get()) < 9:
            casillas[i].config(bg="white")
            

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
        aProxy = []  
        self.variablesEntry = []
        
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
                    sizeVars = len(self.variablesEntry)
                    self.variablesEntry.append(StringVar())
                    self.variablesEntry[sizeVars].trace("w", lambda name, index, mode, var=self.variablesEntry[sizeVars], sizeVars=sizeVars:
                              self.entryupdate(var, sizeVars,listaCASILLAS))
                    
                    
                    #v = StringVar()
                    #v.trace("w", lambda *args:self.callback(v))
                    self.CASILLA = Entry(width=2,font=large_font, justify=CENTER, textvariable = self.variablesEntry[sizeVars])
                    listaCASILLAS+=[self.CASILLA]
                    
                    self.variablesEntry[sizeVars].trace("w", lambda name, index, mode, var=self.variablesEntry[sizeVars], sizeVars=sizeVars:
                              self.entryupdate(var, sizeVars, listaCASILLAS))
                    
                    self.CASILLA.place(x=placeX, y=placeY)
                placeX+=90
            placeY+=85

        #self.verificarButton = Button(text="Verificar solución", font=("Helvetica", 13),
                                      #command=lambda:self.verificarSolucion(listaCASILLAS,kakuroExample))
        self.verificarButton = Button(text="Verificar solución", font=("Helvetica", 13),
                                      command=lambda:self.verificarSolucion(self.variablesEntry,kakuroExample))
        self.verificarButton.place(x=10, y=placeY+10)
        
        
        self.resolverButton = Button(text="Resolver (backtracking)", font=("Helvetica", 13))
        self.resolverButton.place(x=200, y=placeY+10)
        
     
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
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
