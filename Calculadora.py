import tkinter as tk
 
def click(key):
    global oper
    if key == '=':
        
        if '/' in txtDisplay.get() and '.' not in txtDisplay.get():
            txtDisplay.insert(tk.END, ".0")
        
        str1 = "-+0123456789."

        if txtDisplay.get()[0] not in str1:
            txtDisplay.insert(tk.END, "Error" + str1)
        
        try:
            resp = eval(txtDisplay.get())
            txtDisplay.insert(tk.END, " = " + str(resp))
        except:
            txtDisplay.insert(tk.END, "Error!")
    elif key == 'C':
        txtDisplay.delete(0, tk.END)


        if '=' in oper:
            ix = oper.find('=')
            oper = oper[ix+2:]
        app.title('M=' + oper)

    else:

        if '=' in txtDisplay.get():
            txtDisplay.delete(0, tk.END)
        txtDisplay.insert(tk.END, key)
 
app = tk.Tk()
app.title("calculadora")
 
btn_list = [
'7',  '8',  '9',  '*',  'C',
'4',  '5',  '6',  '/',  ' ',
'1',  '2',  '3',  '-',  ' ',
'0',  '.',  '=',  '+',   ]
 
#usamos la funcion loop para crear los botones
r = 1
c = 0
for b in btn_list:
    rel = 'ridge'
    cmd = lambda x=b: click(x)
    tk.Button(app,padx=10,pady=10,font=10,text=b,width=5,bd=3,relief=rel,command=cmd).grid(row=r,column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1
 
txtDisplay = tk.Entry(app, width=40, bg="Sky blue",bd=5,font=20)
txtDisplay.grid(row=0, column=0, columnspan=5)
 
app.mainloop()
