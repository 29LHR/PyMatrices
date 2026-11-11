from tkinter import Tk, Toplevel, Label, Entry, Button, Frame, Menu
from typing import Union
from pyMatrices import numMatrix, unitSquare, identity, multiply
lazy import matplotlib.pyplot as plt

class numMatrixGUI():
    def __init__(self, root : Union[Tk, Toplevel, Frame], matrix : numMatrix, name : str):
        self.__root = Frame(root)
        self.__matrix = matrix
        self.__name = name
        self.__createGUI()
    
    def __createGUI(self)-> None:
        def plot():
            self.__matrix.plot(self.__name,"#7C0101",'o')
            
        frame = self.__root
        title = Label(frame, text=self.__name, anchor='center')
        title.grid(column=0, row=0, columnspan=self.__matrix.width +2)
        plotBtn = Button(frame, text='Plot', anchor='center', command=plot)
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
            
    
    def pack(self)-> None:
        self.__root.pack()
    
    def grid(self, row=0, column=0, columnspan=1, rowspan=1)-> None:
        self.__root.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

class createMatrixMenu:
    def __init__(self, root: Union[Tk, Toplevel], height: int, width: int) -> None:
        self.__super = root
        self.__root = Toplevel(self.__super)
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
        self.__matrixGUI = numMatrixGUI(self.__super,self.__matrix,name=self.__name.get())

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
        
        #Styling Stuff
        self.__root.title('Matrix Calculator')
        self.__root.geometry('400x400')
        
        #Create a Matrix Button
        self.__createToolbar()
        
        #Show Graph
        plt.legend()
        graphBtn = Button(self.__root, text='Show Plots', command=plt.show)
        graphBtn.pack()
        
        matrix = numMatrixGUI(self.__root, numMatrix([[1,0],[0,1]]), 'My First Matrix')
        matrix.pack()
        
    def close(self):
        self.__root.destroy()
        
    def __createToolbar(self):
        def createMatrix(height: int, width: int):
            createMatrixMenu(self.__root, height, width)
        
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
        
        createMenu.add_command(label="Create Unit Square", command=lambda : numMatrixGUI(self.__root, unitSquare(), name="Unit Square"), accelerator='Control+N')
        self.__root.bind_all('<Control-n>', lambda c : numMatrixGUI(self.__root, unitSquare(), name="Unit Square"))
        createMenu.add_command(label="Create Identity Matrix", command=lambda : numMatrixGUI(self.__root, identity(), name="Identity"), accelerator='Control+Shift+N')
        self.__root.bind_all('<Control-N>', lambda c : numMatrixGUI(self.__root, identity(), name="Identity"))
        
        createMenu.add_separator()
        #Custom Matrix Creation Magic
        
        #Plot Menu
        plotMenu = Menu(menu, tearoff=0)
        
        plotMenu.add_command(label="Show Plots", command=plt.show, accelerator="Cmd+P")
        self.__root.bind_all('<Command-p>', lambda c : plt.show())        
        
        menu.add_cascade(label='File', menu=fileMenu)
        menu.add_cascade(label='Create', menu=createMenu)
        menu.add_cascade(label="Plot", menu=plotMenu)
        root.config(menu=menu)
            

if __name__ == "__main__":
    root = Tk()
    app = gui(root)
    root.mainloop()