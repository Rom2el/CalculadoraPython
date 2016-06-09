from tkinter import *
 
import sys

 

 
app = Tk()
app.title("Calculadora")


	
#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(50,50))
vp.columnconfigure(1, weight=2)
vp.rowconfigure(1, weight=2)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=7, row=1)

def botones():
	num =0
	for i in [1,3,5]:
		for j in [1,3,5]:
			num=num+1
			boton = Button(vp, text=num, command=hacer_click)
			boton.grid(column=j, row=i)



botones()

app.mainloop()
