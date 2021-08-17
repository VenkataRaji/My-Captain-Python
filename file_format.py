"""Printing the type of file based on the extension used in saving the file

eg:
ip-- name.py
op--it is a python file"""

#input the file name along with the extension as a string
file=input("Input the Filename:")

#it is a python file if it has .py extension
if ".py" in file:
    print("The extension of the file is : 'python'")
else:
    print("File type cannot be identified")
