from tkinter import *
import tkinter as tk
from tkinter import messagebox
import winsound
import json


from PruebaKakuros import *
import PruebaKakurosThreads as PKT
#from PruebaKakurosThreads import *
from NewGenerator import *


#from PruebaKakurosHilos import *


from KakuroGenerator import *
import copy
import time
import os
import threading

large_font = ('Verdana',30)
NTR = ('Times New Roman', 12)


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
        #print(len(kaks[1]))

        self.mainWindow()
        #nueva = self.new_window()
        #w = Scale(nueva, from_=10, to=20)
        #w.pack()


        
        
        #self.createGraphicKakuro(nueva,kakuroExample)
    def mainWindow(self):

        
        #canvas.create_image(150, 150)
        root.after(0, self.update, 0)
        
        photo = PhotoImage(file = 'Pics/KakuroMain3.png')
        generarBTN = PhotoImage(file = 'Pics/generarBTN2.png')
        
        lbl = Label(image = photo,highlightthickness=0, borderwidth=0)
        lbl.image = photo #keeping a reference in this line
        lbl.grid(row=1, column=0)

        root.config(bg="black")
        
        w = Scale( from_=10, to=20, orient=HORIZONTAL, bg="black", width=30,sliderlength=50,
                   troughcolor= "Gray10",fg="DeepPink2", highlightcolor="red",highlightthickness=0,borderwidth=0)
        w.grid(row=2, column=0)

        gen = Button(text="Generar kakuro",highlightthickness=0,borderwidth=0, image=generarBTN,command=lambda: self.createKakuro(w.get()))
        gen.grid(row=3, column=0)
        gen.image = generarBTN


        Label(text="Kakuros de ejemplo:", bg="black",fg="DeepPink4",
                             font=("Helvetica", 12)).grid(row=4,column=0)
        global kakuroList
        kakuroList = Listbox(bg="black", fg="DeepPink4", width=30,height=5,
                             font=("Helvetica", 12))
        kakuroList.grid(row=5, column=0)
        '''
        file = open("savedKakuros.txt", "w")
        file.write(str(kakuro10x10))
        file.write("$")
        file.write(str(kakuro20x20))
        '''

        exmpls = self.updateExampleList(kakuroList)
        
       #k = exmpls[kakuroList.curselection()[0]]
        gen2 = Button(text="Generar ejemplo", highlightthickness=0, borderwidth=0, image=generarBTN,
            command=lambda: self.createKakuroExample(json.loads(exmpls[kakuroList.curselection()[0]])))
        gen2.grid(row=6, column=0)
        #gen2.image = generarBTN
        
    def updateExampleList(self, kakuroList):
        file = open("savedKakuros.txt", "r")
        #print (file.readlines()[0].split("$"))
        exmpls=file.readlines()[0].split("$")
        
        for i in exmpls:
            print(i)
            if i != '':
                kakuroList.insert(END, str(len(json.loads(i))).rjust(32))
        #if file.readlines():
            #exmpls=
            #file.readlines()[0].split("$")
            #print (exmpls)
 
            #for i in exmpls:
                #print(i)
                #kakuroList.insert(END, str(len(json.loads(i))).rjust(32))
        
        file.close()
        return exmpls
    def saveKakuroKernel(self, kak):
        saveKakuro(kak)
        kakuroList.delete(0, END)
        self.mainWindow()
        #self.updateExampleList(kakuroList)
        
    def new_window(self):
        self.newWindow = Toplevel(root)
        self.canvas = tk.Canvas(self.newWindow, borderwidth=0, background="black")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self.newWindow, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        
        
        self.frame.pack( fill="both", expand=True,anchor='center')
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True,anchor='center')
        self.canvas.create_window((10,10), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
       
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        
        #self.main_frame = Frame()
        #self.frame.place(in_=self.newWindow, anchor="c", relx=.50, rely=.50)
        #self.newFrame = Frame(self.newWindow)
        
        return self.frame

    def createKakuroExample(self,kak):
        self.new_window()
        #k = readyKaks[kak.curselection()[0]]
        #print(kak.curselection()[0])
        self.createGraphicKakuro(self.frame, kak)

    def createKakuro(self, size):
        try:
            #print("Trying...")
            newKakuro = KBoard(size)
            newKakuro.initialize()
            newKakuro.print()

            #solve(kakuro)
        except Exception as e:
            print(e)
            
        
        self.new_window()
        
        newKakuro = self.convertirKakuro(newKakuro)
        #newKakuro = createBoard(size)
        #hideSolution(newKakuro)
        #newKakuro = kakuro20x20
        self.resetKakuro(newKakuro)
        self.createGraphicKakuro(self.frame,newKakuro)
        

    def createGraphicKakuro(self,newWin, kakuroPorDesplegar):

        verificarBTN = PhotoImage(file = 'Pics/verificarBTN.png')
        resolverBTN = PhotoImage(file = 'Pics/resolverBTN.png')
        if (len(kakuroPorDesplegar)*100<screen_width) and len(kakuroPorDesplegar)*65 < screen_height:
            newWin.config(width=len(kakuroPorDesplegar)*100, height=len(kakuroPorDesplegar)*5, bg="black")
            self.canvas.configure(width=len(kakuroPorDesplegar)*100, height=len(kakuroPorDesplegar)*80)
        else:
            newWin.config(width=screen_width-200, height=screen_width-800, bg="black")
            self.canvas.configure(width=screen_width-600, height=screen_width-800)
            
        #scrollbar = Scrollbar(newWin)
        #scrollbar.pack(side=RIGHT, fill=Y)
        #newWin = self.new_window()
        photoBLACK = PhotoImage(file="Pics/BLACKsmall4.png")
        photoSLASH = PhotoImage(file="Pics/SLASHsmall.png")
        
        contX = 0
        contY = 0
        placeX = photoBLACK.width()
        placeY=photoBLACK.width()
        v = StringVar()
        listaCASILLAS=[]
        aProxy = []  
        self.variablesEntry = []

        
        for i in range(0, len(kakuroPorDesplegar)):
            placeX = 35*len(kakuroPorDesplegar)/4
            contX = 0
            for j in range(0, len(kakuroPorDesplegar[0])):

                if kakuroPorDesplegar[i][j] == 0:
                    labelCASILLA = Label(newWin,image=photoBLACK,highlightthickness=0, borderwidth=0)
                    labelCASILLA.image = photoBLACK
                    labelCASILLA.grid(row=contY, column=contX)
                    #labelCASILLA.place(x=placeX, y=placeY)
                elif isinstance(kakuroPorDesplegar[i][j], list):
                    labelCASILLA = Label(newWin,image=photoSLASH,highlightthickness=0, borderwidth=0)
                    labelCASILLA.image = photoSLASH
                    labelCASILLA.grid(row=contY, column=contX)
                    #labelCASILLA.place(x=placeX, y=placeY)
                    if kakuroPorDesplegar[i][j][0] != 0:
                        labelNUM = Label(newWin,text=str(kakuroPorDesplegar[i][j][0]),
                                         font=("Helvetica", 12), fg="white", bg="black",
                                         anchor=E, borderwidth=0,highlightthickness=0)
                        #labelNUM.place(x=placeX+8, y=placeY+25)
                        labelNUM.grid(row=contY, column=contX, sticky=SW)
                    if kakuroPorDesplegar[i][j][1] != 0:
                        labelNUM = Label(newWin,text=kakuroPorDesplegar[i][j][1],
                                         font=("Helvetica", 12), fg="white", bg="black",
                                         anchor=W, borderwidth=0,highlightthickness=0)
                        labelNUM.grid(row=contY, column=contX, sticky=NE)
                        #labelNUM.place(x=placeX+30, y=placeY+8)
                        
                else:
                    
                    sizeVars = len(self.variablesEntry)
                    self.variablesEntry.append(StringVar())
                    self.variablesEntry[sizeVars].trace("w", lambda name, index,
                            mode, var=self.variablesEntry[sizeVars], sizeVars=sizeVars:
                              self.entryupdate(var, sizeVars,listaCASILLAS))
                    
                    
                    #v = StringVar()
                    #v.trace("w", lambda *args:self.callback(v))
                    self.CASILLA = Entry(newWin,width=2,font=large_font,
                                         justify=CENTER, textvariable = self.variablesEntry[sizeVars])
                    listaCASILLAS+=[self.CASILLA]
                    
                    self.variablesEntry[sizeVars].trace("w", lambda name, index,
                            mode, var=self.variablesEntry[sizeVars], sizeVars=sizeVars:
                              self.entryupdate(var, sizeVars, listaCASILLAS))
                    
                    #self.CASILLA.place(x=placeX, y=placeY)
                    self.CASILLA.grid(row=contY, column=contX)
                    if kakuroPorDesplegar[i][j] != -1:
                        #print (kakuroPorDesplegar[i][j])
                        self.variablesEntry[-1].set(kakuroPorDesplegar[i][j])
                        
                placeX+=photoBLACK.width()+2
                contX+=1
            placeY+=photoBLACK.width()+2
            contY+=1


        self.verificarButton = Button(newWin,text="Verificar solución", font=("Helvetica", 13), image=verificarBTN,
                                      command=lambda:self.verificarSolucion(self.variablesEntry,kakuroPorDesplegar)
                                      ,highlightthickness=0,borderwidth=1)
        self.verificarButton.image = verificarBTN
        #self.verificarButton.place(x=10, y=placeY+10)
        self.verificarButton.grid(row=0, column=contX, sticky=N+W+S+E)
        
        
        self.resolverButton = Button(newWin,text="Resolver \n(backtracking)", font=("Helvetica", 13), image=resolverBTN,
                                      command=lambda:self.solucionarKakuro(self.variablesEntry,kakuroPorDesplegar,
                                                                           newWin, threadScale.get(), forksScale.get())
                                     ,highlightthickness=0,borderwidth=1)
        self.resolverButton.image=resolverBTN
        #self.resolverButton.place(x=200, y=placeY+10)
        self.resolverButton.grid(row=1, column=contX, sticky=N+W+S+E)

        threadScale = Scale(newWin, from_=0, to=1000, label="Hilos",
                            orient=HORIZONTAL, bg="black", width=15, sliderlength=50,
                  troughcolor="Gray10", fg="DeepPink2", highlightcolor="red", highlightthickness=0, borderwidth=0)
        threadScale.grid(row=2, column=contX)

        forksScale = Scale(newWin, from_=0, to=20, label="Forks",
                            orient=HORIZONTAL, bg="black", width=15, sliderlength=50,
                            troughcolor="Gray10", fg="DeepPink2", highlightcolor="red", highlightthickness=0,
                            borderwidth=0)
        forksScale.grid(row=4, column=contX)

        self.guardarButton = Button(newWin,text="Guardar \nkakuro", font=("Helvetica", 13),# image=resolverBTN,
                                      command=lambda:self.saveKakuroKernel(kakuroPorDesplegar)
                                     ,highlightthickness=0,borderwidth=1)
        #self.resolverButton.image=resolverBTN
        self.guardarButton.grid(row=5, column=contX, sticky=N+W+S+E)
   
    def convertirKakuro(self,kakuroPorDesplegar):
        kakuro2 = []
        filaKakuro2 = []

        
        for i in range(0, kakuroPorDesplegar.len()):
            for j in range(0, kakuroPorDesplegar.len()):
                
                if kakuroPorDesplegar.board[i][j].getType() == KCell.CELL_HEADER:

                    filaKakuro2 += [[kakuroPorDesplegar.board[i][j].header[0],
                                     kakuroPorDesplegar.board[i][j].header[1]]]                
                elif kakuroPorDesplegar.board[i][j].getType() == KCell.CELL_DATA:                    
                    filaKakuro2.append(-1)
                else:
                    filaKakuro2.append(0)
   

            kakuro2 += [filaKakuro2]
            filaKakuro2=[]
        return (kakuro2)

    def resetKakuro(self,kakuroPorDesplegar):
        kakuro2 = []
        filaKakuro2 = []

        
        for i in range(0, len(kakuroPorDesplegar)):
            for j in range(0, len(kakuroPorDesplegar)):
                
                if kakuroPorDesplegar[i][j] != 0 and not isinstance(kakuroPorDesplegar[i][j], list):
                    kakuroPorDesplegar[i][j] = -1

   

            #kakuro2 += [filaKakuro2]
            #filaKakuro2=[]
        #return (kakuro2)
        
    def solucionarKakuro(self, listaCASILLAS, kakuro, _newWin, numThreads, numForks):
        listaSOLUCIONES=[]
        copiaKakuroOriginal = copy.deepcopy(kakuro)

        PKT.setGlobalThreads(numThreads)
        if numThreads != 0:
            if PKT.solveKakuro(kakuro):
                print("Solucionado con hilos")
        elif numForks != 0:
            print ("Forks")
        else:
            if solveKakuro(kakuro):
                print("Solucionado")
 
        self.createGraphicKakuro(_newWin,kakuro)

    def verificarSolucion(self, listaCASILLAS, kakuro):

        listaSOLUCIONES=[]
        copiaKakuroOriginal = copy.deepcopy(kakuro)

        cont = 0  
        for x in range(0, len(kakuro)):
            for y in range(0, len(kakuro[0])):
                if kakuro[x][y] != 0 and not isinstance(kakuro[x][y], list):
                #if kakuro[x][y] == -1:
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
                    

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def update(self,ind):
        #print(ind)
        
        frame = frames[ind]
        if ind<45:
            ind += 1
        else:
            ind=0
        #label.configure(image=frame)
        canvas.create_image(250, 140, image=frame)
        root.after(100, self.update, ind)
            
    def __init__(self, master=None):


        self.frame=tk.Frame.__init__(self, root)
        #self.frame.place(in_=self.main_frame, anchor="c", relx=.50, rely=.50)
        
        
        self.createWidgets()

root = Tk()
frames = [PhotoImage(file='Pics/background-gif-9.gif',format = 'gif -index %i' %(i)) for i in range(46)]
canvas = Canvas( bg="black", width=500, height=250,highlightthickness=0,borderwidth=0)
canvas.grid(column=0, row=0)
        
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
app = Application(master=root)
app.mainloop()
root.destroy()
