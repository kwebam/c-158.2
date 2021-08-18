from tkinter import *
root = Tk()
root.title("Geometry Error")
try :
    root.geometry("600")
except :
    print("Bad Geometry Error, only 1 Dimention is Passed in Geometry except two")


root.mainloop()