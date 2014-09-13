#!/usr/bin/env python
'''
File: fereastrasimpla.py
Autor: Mihai Cornel
Email: mhcrnl@gmail.com
Este o fereastra simpla realizata intr-o clasa Python
Ultima modificare: septembrie 2014
'''
from Tkinter import *

class FereastraSimpla(Frame):
    '''
Aceasta este clasa in care scriem codul
'''
    def __init__(self, parent):
        """
In constructorul clasei apelam constructorul clasei mostenitoare Frame.
Parametrul backgraund specifica culoarea ferestrei.
"""
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        '''
Delegam crearea ferestrei in metoda initUI()
'''
        self.parent.title("Fereastra Simpla")
        self.pack(fill=BOTH, expand=1)

def main():
    root = Tk()
    root.geometry("250x250+300+300")
    app = FereastraSimpla(root) # Instanta clasei noastre
    root.mainloop()

if __name__ == '__main__':
    main()

    
        
