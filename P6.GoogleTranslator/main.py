from tkinter import*
from tkinter import ttk

root=Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='orange')

lab_txt=Label(root,text="Translator",font=("Times New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

Sor_txt=Text(frame,font=("Time New Roman",20,"bold"),wrop=WORD)
Sor_txt.place(x=10,y=120,height=100,width=480)


root.mainloop()