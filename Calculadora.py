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



app.mainloop()
