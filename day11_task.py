#Calculator

import tkinter as tk
expr=""
app=tk.Tk()
app.title('Calculator')
app.geometry('300x320')
app.resizable(0,0)
    
result=tk.Variable(app)
tk.Entry(app, textvariable=result, width=42).place(x=18,y=40)


def press(num):
    global expr
    expr= expr+num
    result.set(expr)
    
def clear():
    global expr
    expr=""
    result.set(expr)

def total():
    global expr
    result.set(eval(expr))
    expr=""
    

tk.Button(app, text='Clear', width = 10, height=1, command=lambda: clear()).place(x=18,y=5)
tk.Button(app, text='7', width = 5, height=2, command=lambda: press('7')).place(x=18,y=80)
tk.Button(app, text='8', width = 5, height=2, command=lambda: press('8')).place(x=88,y=80)
tk.Button(app, text='9', width = 5, height=2, command=lambda: press('9')).place(x=160,y=80)
tk.Button(app, text='+', width = 5, height=2, command=lambda: press('+')).place(x=231,y=80)
tk.Button(app, text='4', width = 5, height=2, command=lambda: press('4')).place(x=18,y=140)
tk.Button(app, text='5', width = 5, height=2, command=lambda: press('5')).place(x=88,y=140)
tk.Button(app, text='6', width = 5, height=2, command=lambda: press('6')).place(x=160,y=140)
tk.Button(app, text='-', width = 5, height=2, command=lambda: press('-')).place(x=231,y=140)
tk.Button(app, text='1', width = 5, height=2, command=lambda: press('1')).place(x=18,y=200)
tk.Button(app, text='2', width = 5, height=2, command=lambda: press('2')).place(x=88,y=200)
tk.Button(app, text='3', width = 5, height=2, command=lambda: press('3')).place(x=160,y=200)
tk.Button(app, text='*', width = 5, height=2, command=lambda: press('*')).place(x=231,y=200)
tk.Button(app, text='.', width = 5, height=2, command=lambda: press('.')).place(x=18,y=260)
tk.Button(app, text='0', width = 5, height=2, command=lambda: press('0')).place(x=88,y=260)
tk.Button(app, text='=', width = 5, height=2, command=lambda: total()).place(x=160,y=260)
tk.Button(app, text='/', width = 5, height=2, command=lambda: press('/')).place(x=231,y=260)

app.mainloop()
