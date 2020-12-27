from windowsSetup import start
from tkinter.font import Font
import os, playsound
from tkinter import *
from tkinter import messagebox
from PIL import Image
from settings import *

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
welcomesigninimg2.save("system/welinimg.png")
# Opening image with tkinter
welcomesigninimg = PhotoImage(file="system/welinimg.png")
# Creating Label with saved image
Label(welcomesignin, image=welcomesigninimg).grid(row=0, column=0)
welcomesignin.update()
welcomesignin.update_idletasks()
playsound.playsound("sounds/startup.wav")
welcomesignin.destroy()


def startclckd():
    startroot = Tk()
    startwidth = screen_width-(screen_width + 250)
    startheight = screen_height - (screen_height - 1500)
    startroot.wm_attributes("-topmost", 1)
    shutdownmenubtn = Button(startroot, text="Shutdown")
    shutdownmenubtn.grid(row=6, column=0)
    while True:
        startroot.update()
        startroot.update_idletasks()
        startroot.geometry("250x500+%s+%s" % (startwidth, startheight))


desktop = Tk()
if showWelcomeScreen and not os.path.exists("system/welcomeFalse"):
    tips = Toplevel()
    bold_font = Font(family='Helvetica', size=20)
    very_bold_font = Font(family="Helvetica", size=20, weight='bold')
    tipImg = PhotoImage(file='images/tip.PNG')
    tips.wm_attributes("-topmost", 1)
    tips.title('Welcome')
    Label(tips, text="Приветствуем в", font=bold_font).grid(row=0, column=0)
    Label(tips, text="Windows", font=very_bold_font).grid(row=0, column=1)
    Label(tips, text='95', fg='white', font=very_bold_font).grid(row=0, column=3)
    frame = LabelFrame(tips, bg='#ffffcc')
    Label(frame, image=tipImg).grid(row=0, column=0)
    Label(frame, text='Вы знали...', bg='#ffffcc').grid(row=0, column=1)
    frame.grid(row=1, column=0, columnspan=5)
    tipLabel = Label(frame, text=tip1, bg='#ffffcc')
    tipLabel.grid(row=1, column=0, columnspan=2)

    def nextip():
        global tipNumber
        tipNumber += 1
        if tipNumber == 1:
            tipLabel["text"] = tip1
        elif tipNumber == 2:
            tipLabel["text"] = tip2
        elif tipNumber == 3:
            tipLabel["text"] = tip3
        elif tipNumber == 4:
            tipNumber = 1
            tipLabel["text"] = tip1

    nextTip = Button(tips, text='Следующая подсказка', command=nextip).grid(row=1, column=6)
    showing = IntVar()
    showcheckbox = Checkbutton(tips, text='Показывать это окно при последующих запусках Windows', variable=showing, onvalue=1, offvalue=0)
    showcheckbox.grid(row=2, column=0, columnspan=4)

    def close():
        if showing.get() == 0:
            os.mkdir('system/welcomeFalse')
        tips.destroy()

    closebtn = Button(tips, text='Закрыть', command=close)
    closebtn.grid(row=2, column=6)

desktop.title('Windows 4 or 95?')
desktop['bg'] = "dark blue"
desktop.geometry(ra)
taskbar = Frame(desktop, bg="gray")
taskbar.pack(side=BOTTOM, fill=X)
startbtn = Button(taskbar, text='Start', bg="light gray", activebackground="light gray", bd=7, command=startclckd)
startbtn.grid(column=0)
desktop.mainloop()
