# PyMatrices

A python module designed to do matrix calculations

# Requirements

- Python 3.15.0 or Newer

## Imported Modules

- Matplotlib

# Classes

## Matrix

The Matrix class is the parent of all other classes. It sets out all of the key functions and creates every key variable in using matrices.

### Methods

- _values(rows : bool)->list_: Returns a list of all values in a Matrix so they can be used in calculations. It can return the Matrix in rows (True) or columns (False).

- _printMatrix()->None_: Prints the matrix in a human viewable format rather than as a list - with '|' characters representing the side brackets. This is also used when printing using the built in print() function or the str() functiion.

### Public Variables

- height: The number of rows in the matrix
- width: The number of columns in the matrix

## intMatrix

A child of the **Matrix** class which can only contain number values within its matrix.

### Methods

- All the methods of the **Matrix** class
- _plot(label, color, marker)->None_: Adds the points of the matrix to a scatter plot (which is plotted directly onto plt without a subplot) using matplotlib.

### Public Variables

- All of the public variables of the **Matrix** class

# Arithmetic Functions

- _multiply(**A**: intMatrix, **B**: intMatrix)->intMatrix_: returns **AB**
