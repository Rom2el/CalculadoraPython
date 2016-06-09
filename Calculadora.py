from tkinter import * 
import sys

def limpiar():
	txtDisplay.delete(0,END)
	return
def llenar():
	
	return

app = Tk()
frame= Frame(app)
frame.pack()

app.title("Calculadora")

num1= StringVar()

txtDisplay = Entry(frame,textvariable = num1, bd=20,insertwidth=1, font =30)
txtDisplay.pack(side=TOP)

frame0 = Frame (app)
frame0.pack(side = TOP)
boton1= Button(frame0,padx=16,pady=16,bd=8,text=1,fg="black",command=llenar)
boton1.pack(side=LEFT)
boton2= Button(frame0,padx=16,pady=16,bd=8,text=2,fg="black")
boton2.pack(side=LEFT)
boton3= Button(frame0,padx=16,pady=16,bd=8,text=3,fg="black")
boton3.pack(side=LEFT)
boton4= Button(frame0,padx=16,pady=16,bd=8,text="+",fg="black")
boton4.pack(side=LEFT)

frame1=Frame(app)
frame1.pack(side=TOP)
boton5= Button(frame1,padx=16,pady=16,bd=8,text=4,fg="black")
boton5.pack(side=LEFT)
boton6= Button(frame1,padx=16,pady=16,bd=8,text=5,fg="black")
boton6.pack(side=LEFT)
boton7= Button(frame1,padx=16,pady=16,bd=8,text=6,fg="black")
boton7.pack(side=LEFT)
boton8= Button(frame1,padx=16,pady=16,bd=8,text="-",fg="black")
boton8.pack(side=LEFT)

frame2 = Frame (app)
frame2.pack(side = TOP)
boton1= Button(frame2,padx=16,pady=16,bd=8,text=7,fg="black")
boton1.pack(side=LEFT)
boton2= Button(frame2,padx=16,pady=16,bd=8,text=8,fg="black")
boton2.pack(side=LEFT)
boton3= Button(frame2,padx=16,pady=16,bd=8,text=9,fg="black")
boton3.pack(side=LEFT)
boton4= Button(frame2,padx=16,pady=16,bd=8,text="/",fg="black")
boton4.pack(side=LEFT)

frame3=Frame(app)
frame3.pack(side=TOP)
boton1= Button(frame3,padx=16,pady=16,bd=8,text="C",fg="black",command = limpiar)
boton1.pack(side=LEFT)
boton2= Button(frame3,padx=16,pady=16,bd=8,text=0,fg="black")
boton2.pack(side=LEFT)
boton3= Button(frame3,padx=16,pady=16,bd=8,text="=",fg="black")
boton3.pack(side=LEFT)
boton4= Button(frame3,padx=16,pady=16,bd=8,text="*",fg="black")
boton4.pack(side=LEFT)

app.mainloop()
