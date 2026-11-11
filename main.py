from tkinter import Tk, Label, Entry, Button, Frame
from typing import Any
from pyMatrices import numMatrix, multiply

class numMatrixGUI():
    def __init__(self, root : Tk, matrix : numMatrix):
        self.__root = Frame(root)
        self.__matrix = matrix
        self.__createGUI()
    
    def __createGUI(self):
        pass
    
    def pack(self):
        self.__root.pack()
    
    def grid(self, row=0, column=0, columnspan=1, rowspan=1):
            self.__root.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)

        
class gui:
    def __init__(self, root: Tk):
        self.__root = root
        
        #Styling Stuff
        self.__root.title('Matrix Calculator')
        self.__root.geometry('400x400')
        
        matrix = numMatrixGUI(self.__root, numMatrix([[1,0],[0,1]]))
        matrix.pack()
        
    def mainloop(self)->None:
        self.__root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = gui(root)
    root.mainloop()