from tkinter import Tk, Toplevel, Label, Entry, Button, Frame, Menu
from typing import Union
from pyMatrices import numMatrix, multiply

class numMatrixGUI():
    def __init__(self, root : Union[Tk, Toplevel, Frame], matrix : numMatrix, name : str):
        self.__root = Frame(root)
        self.__matrix = matrix
        self.__name = name
        self.__createGUI()
    
    def __createGUI(self)-> None:
        frame = self.__root
        
        title = Label(frame, text=self.__name, anchor='center')
        title.grid(column=0, row=0, columnspan=self.__matrix.width +2)
        
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
        self.__root = Toplevel(root)
        self.__createInputs()
        self.dims = (width, height)
        
    def __createInputs(self):
        nameFrame = Frame(self.__root)
        name = Entry(nameFrame)
        nameLbl = Label(nameFrame, text='Name:', anchor='center')
        name.grid(row=0, column=1); nameLbl.grid(row=0, column=0)
        nameFrame.pack()
        
        frame = Frame(self.__root)
        inputs = []
        for row in range(self.dims[0]):
            rowInp = []
            for col in range(self.dims[1]):
                rowInp.append(Entry(frame))
                rowInp[-1].grid(row=row, col=0)
            inputs.append(rowInp)
            
     
class gui:
    def __init__(self, root: Union[Tk, Toplevel]):
        self.__root = root
        
        #Styling Stuff
        self.__root.title('Matrix Calculator')
        self.__root.geometry('400x400')
        
        #Create a Matrix Button
        self.__createToolbar()
        
        matrix = numMatrixGUI(self.__root, numMatrix([[1,0],[0,1]]), 'My First Matrix')
        matrix.pack()
        
    def __createToolbar(self):
        def createMatrix():
            print('Creating a matrix magic')
        
        menu = Menu(self.__root)
        
        #Create Menu
        createMenu = Menu(menu, tearoff=0)
        createMenu.add_command(label='New Matrix', command=createMatrix)
        
        menu.add_cascade(label='Create', menu=createMenu)
        root.config(menu=menu)
            

if __name__ == "__main__":
    root = Tk()
    app = gui(root)
    root.mainloop()