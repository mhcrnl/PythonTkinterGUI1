#!/usr/bin/env python -tt
'''
File: fereastrasimplamenu.py
Autor: Mihai Cornel
Email: mhcrnl@gmail.com
Este o fereastra simpla realizata intr-o clasa Python
Ultima modificare: septembrie 2014
'''
from Tkinter import *
import sys

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
        # meniu cu un singur item, selectand exit parasim fereastra
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        #adaugam un menubar cu Menu
        fileMenu = Menu(menubar)
        #Adaugam meniul File cu Exit/new
        fileMenu.add_command(label="Exit", command=self.onExit)
        fileMenu.add_command(label="New")
        menubar.add_cascade(label="File", menu=fileMenu)

        menubar.add_cascade(label="Edit", menu=fileMenu)

        menubar.add_cascade(label="Format")

        menubar.add_cascade(label="Run")

        menubar.add_cascade(label="Option")

        menubar.add_cascade(label="Windows")

        menubar.add_cascade(label="Help")

    def onExit(self):
        self.parent.quit()

def main():
    root = Tk()
    root.geometry("450x450+300+300")
    app = FereastraSimpla(root) # Instanta clasei noastre
    root.mainloop()

if __name__ == '__main__':
    main()

    
        
