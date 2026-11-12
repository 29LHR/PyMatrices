from tkinter import Tk, Toplevel, Label, Entry, Button, Frame, Menu, ttk, messagebox
from typing import Union
from pyMatrices import numMatrix, unitSquare, identity, multiply, IncompatibleMatrixError
lazy import matplotlib.pyplot as plt
lazy import random as r

class numMatrixGUI():
    def __init__(self, root : Union[Tk, Toplevel, Frame], super : gui, matrix : numMatrix, name : str):
        self.__root = Frame(root)
        self.__matrix = matrix
        self.name = name
        
        super.matrices.append(self)
        super.mVals.append(name)
        super.m1['values'] = super.mVals
        super.m2['values'] = super.mVals
        
        self.__createGUI()
    
    def plot(self):
        options = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        color = f'#{r.choice(options)}{r.choice(options)}{r.choice(options)}{r.choice(options)}{r.choice(options)}{r.choice(options)}'
        self.__matrix.plot(self.name,color,'o')
                
    def __createGUI(self)-> None:
        frame = self.__root
        title = Label(frame, text=self.name, anchor='center')
        title.grid(column=0, row=0, columnspan=self.__matrix.width +2)
        plotBtn = Button(frame, text='Plot', anchor='center', command=self.plot)
        plotBtn.grid(column=0, row=self.__matrix.height+2, columnspan=self.__matrix.width +2)
        
        vals = self.__matrix.values()
        labels = []
        for row in range(len(vals)):
            labRow = []
            labRow.append(Label(frame, text='|'))
            labRow[-1].grid(row=row+1, column=0)
            for i in range(self.__matrix.width):
                labRow.append(Label(frame, text=str(vals[row][i])))
                labRow[-1].grid(row=row+1, column=i+1)
                
            labRow.append(Label(frame, text='|'))
            labRow[-1].grid(row=row+1, column=len(labRow)-1)
            labels.append(labRow)
        
        frame.pack()
            
    def getMatrix(self)->numMatrix:
        return self.__matrix
    
    def pack(self)-> None:
        self.__root.pack()
    
    def grid(self, row=0, column=0, columnspan=1, rowspan=1)-> None:
        self.__root.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

class createMatrixMenu:
    def __init__(self, root: gui, height: int, width: int) -> None:
        self.__super = root
        self.__superRoot = self.__super.root
        self.__root = Toplevel(self.__superRoot)
        self.__root.geometry("200x200")
        self.__root.title('New Matrix')
        
        self.dims = (width, height)
        self.__createInputs()
    
    def __createMatrix(self):
        self.__matrix = []
        for row in range(self.dims[1]):
            rowNums = []
            for col in range(self.dims[0]):
                rowNums.append(int(self.__inputs[row][col].get()))
            self.__matrix.append(rowNums)
        
        self.__matrix = numMatrix(self.__matrix)
        GUI = numMatrixGUI(self.__super.root, self.__super, self.__matrix, self.__name.get())

    def __createInputs(self):
        nameFrame = Frame(self.__root)
        self.__name = Entry(nameFrame, width=10)
        nameLbl = Label(nameFrame, text='Name:', anchor='center')
        self.__name.grid(row=0, column=1); nameLbl.grid(row=0, column=0)
        nameFrame.pack()
        
        frame = Frame(self.__root)
        self.__inputs = []
        for row in range(self.dims[1]):
            rowInp = []
            for col in range(self.dims[0]):
                rowInp.append(Entry(frame, width=1))
                rowInp[-1].grid(row=row, column=col)
            self.__inputs.append(rowInp)
        
        frame.pack()
        
        createBtn = Button(self.__root, text='Create', command=self.__createMatrix)
        createBtn.pack()
            
     
class gui:
    def __init__(self, root: Union[Tk, Toplevel]):
        self.__root = root
        self.matrices = []
        
        #Styling Stuff
        self.__root.title('Matrix Calculator')
        self.__root.geometry('500x400')
        
        #GUI Functions
        self.__createButtons()
        self.__createToolbar()
    
    def multiplyCmd(self):
        m1 = self.matrices[self.mVals.index(self.m1.get())]
        m2 = self.matrices[self.mVals.index(self.m2.get())]
        self.multiplyGUI(m1.getMatrix(), m2.getMatrix(), f'{self.m1.get()} x {self.m2.get()}')
        
    def __createButtons(self):
        buttonFrame = Frame(self.__root)
        #Show Graph Button
        graphBtn = Button(buttonFrame, text='Show Plots', command=self.showPlots)
        graphBtn.grid(row=0, column=0)
        
        multiplyBtn = Button(buttonFrame, text='Multiply', command=self.multiplyCmd)
        self.m1 = ttk.Combobox(buttonFrame, state='readonly', width=10)
        self.mVals = [matrix.name for matrix in self.matrices]
        self.m1['values'] = self.mVals
        self.m2 = ttk.Combobox(buttonFrame, state='readonly', width=10)
        self.m2['values'] = self.mVals
        
        multiplyBtn.grid(row=0, column=1)
        self.m1.grid(row=0, column=2)
        self.m2.grid(row=0, column=3)
        
        buttonFrame.pack()
        
        #Line
        line = Label(self.__root, text="--------------------------------------------------------")
        line.pack()
    
    def showPlots(self):
        plt.legend()
        plt.show()
        
    def plotAll(self):
        for matrix in self.matrices:
            matrix.plot()
        
    def multiplyGUI(self, m1 : numMatrix, m2 : numMatrix, name : str):
        print('Printing multiplied matrix')
        try:
            matrix = numMatrixGUI(self.__root, self, multiply(m1, m2), name)
            matrix.pack()
        except IncompatibleMatrixError:
            error = messagebox.showwarning('Incompatible Matrices', 'The matrices need to have similar dimensions in order to multiply. E.g. A 2x2 multiplied by a 2x4.')
    
    def close(self):
        self.__root.destroy()
    
    @property
    def root(self):
        return self.__root
        
    def __createToolbar(self):
        def createMatrix(height: int, width: int):
            createMatrixMenu(self, height, width)
        
        menu = Menu(self.__root)
        
        #File Menu
        fileMenu = Menu(menu, tearoff=0)
        
        fileMenu.add_command(label='Close', command=lambda : self.close(), accelerator='Cmd+W')
        self.__root.bind_all('<Command-w>', lambda c : self.close())
        
        #Create Menu
        createMenu = Menu(menu, tearoff=1)
        
        createMenu.add_command(label='New 2x2 Matrix', command=lambda : createMatrix(2,2), accelerator='Cmd+N')
        self.__root.bind_all('<Command-n>', lambda c : createMatrix(2,2))
        createMenu.add_command(label='New 2x1 Matrix', command=lambda : createMatrix(2,1), accelerator="Cmd+Shift+N")
        self.__root.bind_all('<Command-N>', lambda c : createMatrix(2,1))
        createMenu.add_command(label='New 2x4 Matrix', command=lambda : createMatrix(2,4), accelerator="Alt+N")
        self.__root.bind_all('<Alt-n>', lambda c : createMatrix(2,4))
        
        createMenu.add_separator()
        
        createMenu.add_command(label="Create Unit Square", command=lambda : numMatrixGUI(self.__root, self, unitSquare(), name="Unit Square"), accelerator='Control+N')
        self.__root.bind_all('<Control-n>', lambda c : numMatrixGUI(self.__root, self, unitSquare(), name="Unit Square"))
        createMenu.add_command(label="Create Identity Matrix", command=lambda : numMatrixGUI(self.__root, self, identity(), name="Identity"), accelerator='Control+Shift+N')
        self.__root.bind_all('<Control-N>', lambda c : numMatrixGUI(self.__root, self, identity(), name="Identity"))
        
        createMenu.add_separator()
        #Custom Matrix Creation Magic
        
        #Plot Menu
        plotMenu = Menu(menu, tearoff=0)
        
        plotMenu.add_command(label="Plot All", command=self.plotAll, accelerator="Cmd+P")
        self.__root.bind_all('<Command-p>', lambda c : self.plotAll())
        plotMenu.add_command(label="Show Plots", command=self.showPlots, accelerator="Control+P")
        self.__root.bind_all('<Control-p>', lambda c : self.showPlots())     
        
        menu.add_cascade(label='File', menu=fileMenu)
        menu.add_cascade(label='Create', menu=createMenu)
        menu.add_cascade(label="Plot", menu=plotMenu)
        root.config(menu=menu)
            

if __name__ == "__main__":
    root = Tk()
    app = gui(root)
    root.mainloop()