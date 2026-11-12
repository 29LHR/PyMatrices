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

## numMatrix

A child of the **Matrix** class which can only contain number values within its matrix.

### Methods

- All the methods of the **Matrix** class
- _plot(label, color, marker)->None_: Adds the points of the matrix to a scatter plot (which is plotted directly onto plt without a subplot) using matplotlib.

### Public Variables

- All of the public variables of the **Matrix** class

# Arithmetic Functions

- _multiply(**A**: intMatrix, **B**: intMatrix)->intMatrix_: returns **AB**

# Example GUI

A matrix calculator. View all of the classes and functions of pyMatrices in a user orientated app.

# Classes

## numMatrixGUI
The numMatrixGUI displays pyMatrices' **numMatrix** in the root gui.

### Methods

- _plot()_: Calls the numMatrix's _plot()_ method
- _\_\_createGUI()_: Creates the Labels needed to display the matrix as well as a plot button and puts them in a frame and packs it to the root
- _getMatrix()_: Returns the Matrix
- _pack()_: Uses the tkinter _pack_ method to pack the Frame
- _grid()_: Uses the tkinter _grid_ method to plot the Frame on a grid

### Public Variables

- name: The name of the matrix being displayed

## createMatrixMenu:

Creates a toplevel which has the inputs in which one can register a matrix with teh application

### Methods

- _\_\_createMatrix()_: Creates a numMatrixGUI in the root
- _\_\_createInputs()_: Creates all of the Entry widgets needed to create a matrix of specified dimensions

### Public Variables

- dims: The dimensions of the Matrix it's creating in a set

## gui

Creates the base gui of the application.

### Methods

- _multiplyCmd()_: Calls the _multiplyGUI()_ method from a button or keybind command
- _multiplyGUI()_: Creates the GUI for the _multiply_ function of the pyMatrices library
- _\_\_createButtons()_: Creates the Buttons used at the top of the screen to perform operations
- _showPlots()_: plots a legend and then shows using _plt.show()_ from matplotlib
- _close()_: destroys the application
- _root_: returns the root of the application
- _\_\_createToolbar()_: Creates the menus and commands in the toolbar used for the application

### Public Variables

- matrices: A list of all matrices that are being displayed

# Coming Soon...

- More arithmetic functions
- Custom matrices in the GUI
- Scroll frames instead of really tall GUI

# AI Notice

No Artificial Intelligence was used in creating this repository.
