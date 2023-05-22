
"""
File I/O, or file input/output, allows your programs to read and write data to files on the hard drive. This exercise covers just the basics of writing text to a file with Python code and then reading the text from the file you just created. 
File I/O is an important technique because it allows your programs to save data so that work isn’t lost when the program closes.

Exercise Description

You will write three functions for this exercise. First, write a writeToFile() function with two parameters for the filename of the file and the text to write into the file. Second, write an appendToFile() function, which is identical to writeToFile() except that the file opens in append mode instead of write mode. 
Finally, write a readFromFile() function with one parameter for the filename to open. 
This function returns the full text contents of the file as a string.
"""

def writeToFile(filename, text):
    with open(filename, "r") as fileObj:
        filename.write(text)

 
def appendToFile(filename, text):
    with open(filename, "a") as fileObj:
        filename.write(text)

 
def readFromFile(filename):
    with open(filename) as fileObj:
        return filename.read()