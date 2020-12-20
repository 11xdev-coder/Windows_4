from windowsSetup import start
import os, playsound
from tkinter import *
from tkinter import messagebox
from PIL import Image

if os.path.exists('setup/success'):
    pass
else:
    start()


def checkname(name, rootForDestroy):
    usernameopen = open("userinfo/name.txt", "r")
    username = usernameopen.read()
    if name == username:
        rootForDestroy.destroy()
    else:
        messagebox.showerror("", "Введено не верное имя пользователя!")


signin = Tk()
# Screen Resolution
screen_width = signin.winfo_screenwidth()
screen_height = signin.winfo_screenheight()
ra = '%sx%s' % (screen_width, screen_height)
signin.title("")
Label(signin, text="В поле ввода снизу введите Ваше \nимя чтобы войти в систему").grid(row=0, column=0, columnspan=2)
Label(signin, text="Имя: ").grid(row=1, column=0)
name = Entry(signin)
name.grid(row=1, column=1)
Button(signin, text='OK', command=lambda: checkname(name.get(), signin), width=10).grid(row=0, column=2)
Button(signin, text='Отмена', command=lambda: signin.destroy(), width=10).grid(row=1, column=2)
signin.mainloop()

welcomesignin = Tk()
welcomesignin.geometry(ra)
welcomesignin.overrideredirect(1)
# Opening image with Pillow
welcomesigninimgnormal = Image.open("images/welcomeinimg.png")
width = screen_width
height = screen_height
# Resizing image
welcomesigninimg2 = welcomesigninimgnormal.resize((width, height), Image.ANTIALIAS)
# Saving resized image
welcomesigninimg2.save("images/welinimg.png")
# Opening image with tkinter
welcomesigninimg = PhotoImage(file="images/welinimg.png")
# Creating Label with saved image
Label(welcomesignin, image=welcomesigninimg).grid(row=0, column=0)
welcomesignin.update()
welcomesignin.update_idletasks()
playsound.playsound("sounds/startup.wav")
welcomesignin.destroy()
desktop = Tk()
desktop['bg'] = "dark blue"
desktop.geometry(ra)

taskbar = Frame(desktop, bg="gray")
taskbar.pack(side=BOTTOM, fill=X)
startbtn = Button(taskbar, text='Start', bg="light gray", activebackground="light gray", bd=7)
startbtn.grid(column=0)
desktop.mainloop()
