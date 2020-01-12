import tkinter

window = tkinter.Tk()
window.title("Command Function")

def clicked():
    tkinter.Label(window,text="GUI with tkinter!!!").pack()

tkinter.Button(window,text="Click Me!",command=clicked).pack()

window.mainloop()
