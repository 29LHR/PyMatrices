lazy import matplotlib.pyplot as plt

#Custom Error Messages  
class IncompatibleMatrixError(Exception):
    def __init__(self) -> None:
        super().__init__("The transforming matrix's width needs to be the same as the original matrix's height")

class Matrix:
    def __init__(self, vals : list):
        self.width = len(vals[0])
        self.height = len(vals)
        print(f"Creating a {self.height}x{self.width} Matrix")
        
        self._rows = vals.copy()
        self._cols = [[] for i in range(self.width)]
        for i in range(len(self._rows)):
            for j in range(len(self._rows[i])):
                self._cols[j].append(self._rows[i][j])

    def values(self, rows=True)->list:
        if rows:
            return self._rows.copy()
        else:
            return self._cols.copy()
        
    def printMatrix(self):
        rows = []
        for row in self._rows:
            List = []
            List.append("|")
            for col in row:
                List.append(str(col))
            
            List.append('|')
            rows.append(" ".join(List))
            
        printStr = "\n".join(rows)
        return printStr

    def __str__(self):
        return self.printMatrix()

class intMatrix(Matrix):
    def __init__(self, vals : list):
        super().__init__(vals)
    
    def plot(self, label, color, marker):
        x = [col[0] for col in self._cols]
        y = [col[1] for col in self._cols]
        plt.scatter(x,y, label=label, color=color, marker=marker)
        plt.plot(x,y, color=color)
        
        xA = x[1:]; yA = y[1:]
        xA.append(x[0]); yA.append(y[0])
        plt.plot(xA, yA, color=color)

#Defaults intMatrices    
class unitSquare(intMatrix):
    def __init__(self):
        super().__init__([[0,1,1,0],[0,0,1,1]])
class identity(intMatrix):
    def __init__(self):
        super().__init__([[1,0], [0,1]])
        
#Arithmetic Functions
def multiply(A : intMatrix, B : intMatrix)-> intMatrix:
    def multiplyPts(a: list, b: list):
        num = 0
        for i in range(len(a)):
            num += a[i]*b[i]
        return num
    
    if A.width != B.height:
        raise IncompatibleMatrixError()

    #Check they are not the identity matrix
    if type(A) == identity:
        return B
    elif type(B) == identity:
        return A
    
    aRows = A.values(True)
    bCols = B.values(False)
    valsC = []
    
    for row in range(A.height):
        apdList = []
        for col in range(B.width):
            #[0][0] aRows[0] * bCols[0]
            #[0][1] aRows[0] * bCols[1]
            #[1][0] aRows[1] * bCols[0]
            #[1][1] aRows[1] * bCols[1]
            num = multiplyPts(aRows[row], bCols[col])
            apdList.append(num)
            print(f"{aRows[row]}x{bCols[col]} = {num}")
            
        valsC.append(apdList)
    
    return intMatrix(valsC)
    