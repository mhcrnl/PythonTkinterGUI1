#!/usr/bin/env python
'''
File: fereastrabutoane.py
Autor: Mihai Cornel
Email: mhcrnl@gmail.com
Este o fereastra simpla realizata intr-o clasa Python
Ultima modificare: septembrie 2014
'''
from Tkinter import *
class App:
    def __init__ (self, master):
        frame=Frame(master)
        frame.pack()
        self.button=Button(frame, text="Inchide", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        self.button1=Button(frame, text="Salut", command=self.say_hi)
        self.button1.pack(side=LEFT)
    def say_hi(self):
        print "Salut! Tuturor."

root=Tk()
app=App(root)
root.mainloop()
        
    
