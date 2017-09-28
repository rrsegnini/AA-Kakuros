from tkinter import *
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
                    elif kakuroExample[i][j][1] != 0:
                        labelNUM = Label(text=kakuroExample[i][j][1], font=("Helvetica", 13), fg="white", bg="black")
                        labelNUM.place(x=placeX+52, y=placeY+20)
                else:
                    self.CASILLA = Entry(width=2,font=large_font, justify=CENTER, textvariable=v)
                    self.CASILLA.place(x=placeX, y=placeY)
                placeX+=90
            placeY+=85

        self.verificarButton = Button(text="Verificar solución", font=("Helvetica", 13),
                                      command=lambda:self.verificarSolucion())
        self.verificarButton.place(x=10, y=placeY+10)
        
        
        self.resolverButton = Button(text="Resolver (backtracking)", font=("Helvetica", 13))
        self.resolverButton.place(x=200, y=placeY+10)
        
    def verificarSolucion(self):
        s = v.get()
        print(s)
        
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
