from tkinter import *
from tkinter.ttk import Combobox
import os


def whoami():
    file = open("userinfo/name.txt", 'r')
    print(file.read())
    return file.read()
    file.close()


def md(filepath):
    os.mkdir(filepath)


def rd(filepath):
    os.removedirs(filepath)


def dir(filepath):
    print(os.listdir(filepath))


def ls(filepath):
    print(os.listdir(filepath))


def apply(field, fonts):
    if fonts.get() == "6":
        field.config(font="Helvetica 6")
    elif fonts.get() == "7":
        field.config(font="Helvetica 7")
    elif fonts.get() == "8":
        field.config(font="Helvetica 8")
    elif fonts.get() == "9":
        field.config(font="Helvetica 9")
    elif fonts.get() == "10":
        field.config(font="Helvetica 10")
    elif fonts.get() == "11":
        field.config(font="Helvetica 11")
    elif fonts.get() == "12":
        field.config(font="Helvetica 12")
    elif fonts.get() == "13":
        field.config(font="Helvetica 13")
    elif fonts.get() == "14":
        field.config(font="Helvetica 14")
    elif fonts.get() == "15":
        field.config(font="Helvetica 15")
    elif fonts.get() == "16":
        field.config(font="Helvetica 16")
    elif fonts.get() == "17":
        field.config(font="Helvetica 17")
    elif fonts.get() == "18":
        field.config(font="Helvetica 18")
    elif fonts.get() == "19":
        field.config(font="Helvetica 19")
    elif fonts.get() == "20":
        field.config(font="Helvetica 20")
    elif fonts.get() == "21":
        field.config(font="Helvetica 21")
    elif fonts.get() == "22":
        field.config(font="Helvetica 22")


def copy_text(field):
    field.clipboard_clear()
    field.clipboard_append(field.selection_get())


def paste_text(field):
    field.insert(END, field.clipboard_get())


def startms_dos(programsmenu):
    programsmenu.destroy()
    root = Toplevel()
    copyimg = PhotoImage(file='images/ms_dos_copyimg.PNG')
    pasteimg = PhotoImage(file='images/ms_dos_pasteimg.PNG')
    root.title("MS-DOS Prompt")
    runbtn = Button(root, text='Run', command=lambda: exec(runcode.get(1.0, END)))
    copybtn = Button(root,image=copyimg, command=lambda: copy_text(runcode))
    copybtn.grid(row=0, column=0)
    pastebtn = Button(root, image=pasteimg, command=lambda: paste_text(runcode))
    pastebtn.grid(row=0, column=1)
    runbtn.grid(row=0, column=2)
    runcode = Text(root, font="Helvetica 18")
    runcode.grid(row=1, column=0, columnspan=3)
    Label(root, text="Размер шрифта:").grid(row=2, column=0)
    fonts = Combobox(root, values=["6", "7", '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22'])
    fonts.current(12)
    fonts.grid(row=3, column=0)
    applybtn = Button(root, text='Применить', command=lambda: apply(runcode, fonts))
    applybtn.grid(row=4, column=0)
    root.mainloop()