import tkinter as tk
# GLOBAL EXPR
expression = ""
# Implement Press event
def press(val):
    global expression
    expression += str(val)
    equation.set(expression)

# Implement Clear event
def clear():
    global expression
    expression = ''
    equation.set('')

# Implement Press Equal
def eqPress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set('error')
        expression = ''


# Cretae UI
gui = tk.Tk()
# window bg color
gui.configure(background='light green')

# window title
gui.title('Simple Calculator')

# window bg size
gui.geometry('370x280')

equation = tk.StringVar()
expr_field = tk.Entry(gui, textvariable=equation)

# expression as monitor
equation.set('Enter your expression')
expr_field.grid(columnspan=4, ipadx=90)

# ROW 2
# Cretea Python Button grid
b1 = tk.Button(gui, text='1', fg='red', bg='black',
               command=lambda: press(1), height=3, width=10)
b1.grid(row=2, column=0)

# Cretea Python Button grid
b2 = tk.Button(gui, text='2', fg='red', bg='black',
               command=lambda: press(2), height=3, width=10)
b2.grid(row=2, column=1)

# Cretea Python Button grid
b3 = tk.Button(gui, text='3', fg='red', bg='black',
               command=lambda: press(3), height=3, width=10)
b3.grid(row=2, column=2)

# Cretea Python Button grid
b4 = tk.Button(gui, text='4', fg='red', bg='black',
               command=lambda: press(4), height=3, width=10)
b4.grid(row=2, column=3)

# ROW 3
# Cretea Python Button grid
b5 = tk.Button(gui, text='5', fg='red', bg='black',
               command=lambda: press(5), height=3, width=10)
b5.grid(row=3, column=0)

# Cretea Python Button grid
b6 = tk.Button(gui, text='6', fg='red', bg='black',
               command=lambda: press(6), height=3, width=10)
b6.grid(row=3, column=1)

# Cretea Python Button grid
b7 = tk.Button(gui, text='7', fg='red', bg='black',
               command=lambda: press(7), height=3, width=10)
b7.grid(row=3, column=2)

# Cretea Python Button grid
b8 = tk.Button(gui, text='8', fg='red', bg='black',
               command=lambda: press(8), height=3, width=10)
b8.grid(row=3, column=3)

# ROW 4
# Cretea Python Button grid
b9 = tk.Button(gui, text='9', fg='red', bg='black',
               command=lambda: press(9), height=3, width=10)
b9.grid(row=4, column=0)

# Cretea Python Button grid
b0 = tk.Button(gui, text='0', fg='red', bg='black',
               command=lambda: press(0), height=3, width=10)
b0.grid(row=4, column=1)

# Cretea Python Button grid
bplus = tk.Button(gui, text='+', fg='red', bg='black',
                  command=lambda: press('+'), height=3, width=10)
bplus.grid(row=4, column=2)

# Cretea Python Button grid
bminus = tk.Button(gui, text='-', fg='red', bg='black',
                   command=lambda: press('-'), height=3, width=10)
bminus.grid(row=4, column=3)

# ROW 5
# Cretea Python Button grid
bmul = tk.Button(gui, text='x', fg='red', bg='black',
                 command=lambda: press('*'), height=3, width=10)
bmul.grid(row=5, column=0)

# Cretea Python Button grid
bdiv = tk.Button(gui, text='/', fg='red', bg='black',
                 command=lambda: press('/'), height=3, width=10)
bdiv.grid(row=5, column=1)

# Cretea Python Button grid
beq = tk.Button(gui, text='=', fg='red', bg='black',
                command=eqPress, height=3, width=10)
beq.grid(row=5, column=2)

# Cretea Python Button grid
bdot = tk.Button(gui, text='.', fg='red', bg='black',
                 command=lambda: press('.'), height=3, width=10)
bdot.grid(row=5, column=3)

# ROW 6

# Cretea Python Button grid
bback = tk.Button(gui, text='Clear', fg='red', bg='black',
                  command=clear, height=3, width=10)
bback.grid(row=6, column=0)

# Cretea Python Button grid
bpow = tk.Button(gui, text='', fg='red', bg='black', state="disabled", height=3, width=10)
bpow.grid(row=6, column=1)

# Cretea Python Button grid
bsqrt = tk.Button(gui, text='', fg='red', bg='black', state="disabled", height=3, width=10)
bsqrt.grid(row=6, column=2)

# Cretea Python Button grid
bfact = tk.Button(gui, text='', fg='red', bg='black', state="disabled", height=3, width=10)

bfact.grid(row=6, column=3)

gui.resizable(width=False, height=False)

gui.mainloop()