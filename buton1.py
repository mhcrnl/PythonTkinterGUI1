import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def apelMesaj():
    tkMessageBox.showinfo("Salut Python", "Salut România!")

b = Tkinter.Button(top, text="Salut", command=apelMesaj)
b.pack()

top.mainloop()
top.destroy()
