#!/usr/bin/env python -tt
'''
File: fereastrasimplamenu.py
Autor: Mihai Cornel
Email: mhcrnl@gmail.com
Este o fereastra simpla realizata intr-o clasa Python
Ultima modificare: septembrie 2014
Resurse web:
http://sandbox.mc.edu/friendly_python/lab5.html
'''

import sys
from Tkinter import *
import tkMessageBox

class C2F(Frame):
	#celsiusEntry = Entry
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()
		
	def initUI(self):
		self.parent.title("Convertor Celsius/Fahrenheit")
		self.pack(fill=BOTH, expand=YES)
		# Meniul superior cu File>Exit si Help>About 
		menuBar= Menu(self.parent)
		self.parent.config(menu=menuBar)
		fileMenu= Menu(menuBar)
		fileMenu.add_command(label="Exit", command = self.onExit)
		menuBar.add_cascade(label="File", menu=fileMenu)
		
		fileMenuA=Menu(menuBar)
		fileMenuA.add_command(label="About", command=self.About)
		menuBar.add_cascade(label="Help", menu=fileMenuA)
		# Adaugare butoane http://effbot.org/tkinterbook/grid.htm
		"""
		Label(self.parent, text="First").grid(row=0, column =0)
		Label(self.parent, text="First").grid(row=1, column = 0)
		"""
		labelframe = LabelFrame(self.parent, text="Celsius/Fahrenheit")
		labelframe.pack(fill="both", expand="yes")
		left = Label(labelframe, text="Celsius")
		left.grid(row=0, column=0)
		Label(labelframe, text="Fahrenheit").grid(row=1, column =0)
		
		global celsiusEntry
		celsiusEntry=Entry(labelframe, bd=5)
		celsiusEntry.grid(row=0, column=1)
		
		global fahrenheitEntry
		fahrenheitEntry=Entry(labelframe, bd=5)
		fahrenheitEntry.grid(row=1, column=1)
		
		calcButon = Button(labelframe, text="Calculeaza", command=self.Calculeaza)
		calcButon.grid(row=1, column=2)
		
	def onExit(self):
		self.parent.quit()
		
	def About(self):
		tkMessageBox.showinfo("Salut", "Program conversie Celsius in Fahrenheit")	
		
	def Calculeaza(self):
		cgrade =celsiusEntry.get()
		fahrenheitEntry.delete(0, END)
		if cgrade == ' ':
			fahrenheitEntry.configure(text = ' ')
		else:
			
			cgrade=float(cgrade)
			global fgrade
			fgrade=9.0/5.0 *(cgrade+32)
			fahrenheitEntry.insert(0,fgrade)
			fahrenheitEntry.configure(text=str(fgrade))
			print cgrade, fgrade, fahrenheitEntry.get()
def main():
	root= Tk()
	root.geometry("350x350+300+300")
	app= C2F(root)
	#Label(root, text="First").grid(row=0, column =0)
	root.mainloop()
	
if __name__ == "__main__":
	main()	
			
