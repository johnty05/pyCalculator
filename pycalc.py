# using of tkinter for GUI in Python Programming
from tkinter import *
import math

# tkinter is one of the tools/libraries used for working with GUI in Python
# to learn more about tkinter refer the following link https://docs.python.org/2/library/tkinter.html

class Calculator():
    def __init__(self):
        self.total=0
        self.curr=""
        self.newNumber=True
        self.operator_pend=False
        self.operator=""
        self.eq=False
    
    # We defined a class Calculator and linked the attributes with the object.
    
    def number_press(self,num):
        
