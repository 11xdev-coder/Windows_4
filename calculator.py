from tkinter import *

memory = 0


def start_calc():
    def deletnum():
        notlength = len(string.get())
        length = notlength - 1
        string.delete(length)

    def deletall():
        string.delete(0, END)

    def answer():
        try:
            notanswer = string.get()
            answer = eval(str(notanswer))
            string.delete(0,END)
            string.insert(END, '%s' % (answer))
        except:
            string.delete(0, END)

    def addd():
        string.insert(END, '/')

    def addy():
        string.insert(END, '*')

    def addm():
        string.insert(END, '-')

    def addp():
        string.insert(END, '+')

    def add0():
        string.insert(END, 0)

    def add9():
        string.insert(END, 9)

    def add8():
        string.insert(END, 8)

    def add7():
        string.insert(END, 7)

    def add6():
        string.insert(END, 6)

    def add5():
        string.insert(END, 5)

    def add4():
        string.insert(END, 4)

    def add3():
        string.insert(END, 3)

    def add2():
        string.insert(END, 2)

    def add1():
        string.insert(END, 1)

    def add():
        global memory
        memory = str(string.get())
        label['text'] = 'Память: %s' % memory

    def MR():
        global memory
        string.insert(END, memory)

    def MC():
        global memory
        memory = 0
        label['text'] = 'Память: %s' % memory

    Calc = Toplevel()
    Calc.title('Калькулятор')
    label = Label(Calc, text='Память: %s' % (memory))
    string = Entry(Calc)
    mc = Button(Calc, text='MC', command=MC)
    mr = Button(Calc, text='MR', command=MR)
    madd = Button(Calc, text='M+', command=add)
    b1 = Button(Calc, text=1, command=add1)
    b2 = Button(Calc, text=2, command=add2)
    b3 = Button(Calc, text=3, command=add3)
    b4 = Button(Calc, text=4, command=add4)
    b5 = Button(Calc, text=5, command=add5)
    b6 = Button(Calc, text=6, command=add6)
    b7 = Button(Calc, text=7, command=add7)
    b8 = Button(Calc, text=8, command=add8)
    b9 = Button(Calc, text=9, command=add9)
    b0 = Button(Calc, text=0, command=add0)
    bmn = Button(Calc, text='-', command=addm)
    bp = Button(Calc, text='+', command=addp)
    bm = Button(Calc, text='-', command=addm)
    by = Button(Calc, text='*', command=addy)
    bd = Button(Calc, text='/', command=addd)
    br = Button(Calc, text='=', command=answer)
    back = Button(Calc, text='<<<', command=deletnum)
    all = Button(Calc, text='C', fg='red', command=deletall)
    menu = Menu(Calc)
    new_item6 = Menu(menu, tearoff=0)
    new_item6.add_command(label='Копировать', command=add)
    new_item6.add_command(label='Вставить', command=MR)
    menu.add_cascade(label='Редактирование', menu=new_item6)
    Calc.config(menu=menu)
    label.grid(row=0, column=0)
    string.grid(row=1, column=1, columnspan=4)
    mc.grid(row=2, column=0)
    mr.grid(row=3, column=0)
    madd.grid(row=4, column=0)
    b1.grid(row=2, column=1)
    b2.grid(row=3, column=1)
    b3.grid(row=4, column=1)
    b4.grid(row=2, column=2)
    b5.grid(row=3, column=2)
    b6.grid(row=4, column=2)
    b7.grid(row=2, column=3)
    b8.grid(row=3, column=3)
    b9.grid(row=4, column=3)
    b0.grid(row=5, column=2)
    bmn.grid(row=5, column=3)
    bp.grid(row=2, column=4)
    bm.grid(row=3, column=4)
    by.grid(row=4, column=4)
    bd.grid(row=5, column=4)
    br.grid(row=6, column=4)
    back.grid(row=2, column=5)
    all.grid(row=3, column=5)
    Calc.mainloop()
