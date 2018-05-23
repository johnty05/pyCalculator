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
        self.eq=False
        tmp=text_box.get()
        tmp2=str(num)
        if self.newNumber=True:
            self.curr=tmp2
            self.newNumber=False
        else:
            if tmp2=='.':
                if tmp2 in tmp:
                    return
            self.curr=tmp+tmp2
        self.display(self.curr)
        
    def calTotal(self):
        self.eq = True
        self.curr = float(self.curr)
        # We convert the data type to float
        if self.operator_pend == True:
            self.doSum()
        else:
            self.total = float(text_box.get())
    
        
