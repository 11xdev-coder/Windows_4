from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import pyscreenshot as ImageGrab
from tkinter import colorchooser

name = 0
mode = 'pencil'
brush_size = 3
color = 'black'


def start_mspaint():

    def selectrubber():
        global mode
        global color
        color = 'white'
        mode = 'rubber'
        btnbrush['image'] = imgbrush
        btnpencil['image'] = imgpencil
        btnrubber['image'] = imgselectedrubber


    def selectbrush():
        global mode
        global color
        mode = 'brush'
        color = 'black'
        btnbrush['image'] = imgselectedbrush
        btnpencil['image'] = imgpencil
        btnrubber['image'] = imgrubber


    def selectpencil():
        global mode
        global brush_size
        global color
        brush_size = 3
        mode = 'pencil'
        color = 'black'
        btnbrush['image'] = imgbrush
        btnpencil['image'] = imgselectedpencil
        btnrubber['image'] = imgrubber

    def selectwidth():
        global brush_size
        global mode
        if mode == 'brush' or mode == 'rubber':
            def changeW(e):
                global brush_size
                brush_size = int(e)
                widthroot.destroy()
            widthroot = Tk()
            slider = Scale(widthroot,from_=1,to=100,orient=HORIZONTAL)
            slider.grid(row=0,column=1)
            okbtn = Button(widthroot,command=lambda: changeW(slider.get()),text='OK')
            okbtn.grid(row=0,column=0)
            widthroot.mainloop()
        else:
            messagebox.showinfo('Рисовалка','Что-бы изменить размер кисти, вам нужно выбрать не карандаш, а кисть')


    def paint(event):
        x1 = event.x + brush_size
        y1 = event.y + brush_size
        x2 = event.x - brush_size
        y2 = event.y - brush_size
        c.create_oval(x1,y1,x2,y2,fill=color,outline=color)

    def openfile():
        open_return = filedialog.askopenfile(initialdir='/',title="Открыть",filetypes=(('Portable Network Graphics','*.png'),('Graphics Interchange Format','*.gif'),('Joint Photographic Experts Group','*.jpeg')))
        img = Image.open(open_return.name)
        img.show()

    def savefile():
        path = filedialog.asksaveasfilename(initialdir='/',title="Сохранить",filetypes=(('Portable Network Graphics','*.png'),('Graphics Interchange Format','*.gif'),('Joint Photographic Experts Group','*.jpeg')))
        x1 = mspaintroot.winfo_rootx() + c.winfo_x()
        y1 = mspaintroot.winfo_rooty() + c.winfo_y()
        x2 = x1 + c.winfo_width()
        y2 = y1 + c.winfo_height()

        ImageGrab.grab().crop((x1,y1,x2,y2)).save(path)

    def changeC():
        global mode
        global color
        if mode != "rubber":
            color = colorchooser.askcolor()[-1]
        else:
            messagebox.showinfo('','Что-бы изменить цвет, Вам надо выбрать не ластик, а карандаш или же кисточку')

    mspaintroot = Toplevel()
    mspaintroot.wm_attributes("-topmost", 1)
    mspaintroot.title('Paint')
    menu = Menu(mspaintroot)
    ni1 = Menu(menu,tearoff=False)
    ni1.add_command(label='Новый',command=lambda: c.delete('all'))
    ni1.add_command(label='Открыть', command=openfile)
    ni1.add_command(label='сохранить', command=savefile)
    ni1.add_separator()
    menu.add_cascade(menu=ni1,label='Файл')
    ni2 = Menu(menu, tearoff=False)
    ni2.add_command(label='Очистить', command=lambda: c.delete('all'))
    menu.add_cascade(menu=ni2, label='Редактирование')
    ni3 = Menu(menu, tearoff=False)
    ni3.add_command(label='Ширина линий', command=selectwidth)
    menu.add_cascade(menu=ni3, label='Палитра')
    mspaintroot.config(menu=menu)
    imgpencil = PhotoImage(file='images/pencil.PNG')
    imgselectedpencil = PhotoImage(file="images/pencilsld.PNG")
    btnpencil = Button(mspaintroot,image=imgpencil,command=selectpencil)
    btnpencil.grid(row=0,column=0)
    imgbrush = PhotoImage(file='images/brush.PNG')
    imgselectedbrush = PhotoImage(file='images/brushsld.PNG')
    btnbrush = Button(mspaintroot, image=imgbrush, command=selectbrush)
    btnbrush.grid(row=0, column=2)
    imgrubber = PhotoImage(file='images/rubber.PNG')
    imgselectedrubber = PhotoImage(file='images/rubbersld.PNG')
    btnrubber = Button(mspaintroot, image=imgrubber, command=selectrubber)
    btnrubber.grid(row=0, column=1)
    colorbtn = Button(mspaintroot, text='Изменить цвет', command=changeC)
    colorbtn.grid(row=2, column=2, columnspan=2)
    c = Canvas(mspaintroot,width=800,height=700,bg='white',cursor='pencil')
    c.grid(row=1,column=0,columnspan=6)
    mspaintroot.bind('<B1-Motion>',paint)
    mspaintroot.mainloop()

