from tkinter import *
from tkinter import ttk, messagebox 

GUI = Tk()
GUI.title('Program version 0.0')
GUI.geometry('500x300')
def  show():
    messagebox.showinfo('show box', 'hi! you get it')
    
B1 = ttk.Button(GUI,text = 'click', command = show)
B1.pack(ipadx = 30 , ipady = 30)


    

GUI.mainloop()
