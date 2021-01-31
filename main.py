from windowsSetup import start
from tkinter.font import Font
import os, playsound
from sys import platform
from tkinter import *
from tkinter import messagebox
from PIL import Image
from settings import *
from ms_dos_prompt import startms_dos
from windows_explorer import explorer_start
from calculator import start_calc
from notepad import text_editor
from wordpad import word_editor
from paint import start_mspaint
import runner
from snake import start_snek
from internet_browser import start_browser
from media_player import start_media
from sound_recorder import App
from volume_controller import start_volume_controller
from scanDisk import start_scanDisk


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
Button(signin, text='Отмена', command=lambda: sys.exit(0), width=10).grid(row=1, column=2)
signin.mainloop()

welcomesignin = Tk()
welcomesignin.config(cursor='watch white')
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


def start_recorder():
    main = Toplevel()
    main.title('Запись звуков')
    main.geometry('200x100')
    app = App(main)
    main.mainloop()


def launchnotepad():
    fornotepad = Toplevel()
    te = text_editor(fornotepad)
    fornotepad.mainloop()


def launchword():
    forword = Toplevel()
    teword = word_editor(forword)
    forword.mainloop()


def detectosforparkour():
    if platform == 'linux' or platform == 'linux2':
        os.system("Mini_runner/run.x86_64")
    elif platform == 'win32':
        os.system('Mini_runner_for_windows/run/Mini_runner.exe')


def detectosforsolitaire():
    if platform == 'linux' or platform == 'linux2':
        os.system("Solitaire/run.x86_64")
    elif platform == 'win32':
        os.system('Solitaire_for_windows/run/tesiSolitaire.exe')


def opengames():
    gamesmenu = Toplevel()
    gamesmenu.resizable(False, False)
    gamesmenu.title("")
    Button(gamesmenu, text='Сапер', command=lambda: runner.start_minesweeper()).grid(row=0, column=0)
    Button(gamesmenu, text='Змейка', command=lambda: start_snek()).grid(row=1, column=0)
    Button(gamesmenu, text='Солитер', command=detectosforsolitaire).grid(row=2, column=0)
    Button(gamesmenu, text='Паркур', command=detectosforparkour).grid(row=3, column=0)
    gamesmenu.mainloop()


def opensystemtools():
    systemtoolsmenu = Toplevel()
    systemtoolsmenu.resizable(False, False)
    systemtoolsmenu.title("")
    Button(systemtoolsmenu, text='ScanDisk', command=lambda: start_scanDisk()).grid(row=0, column=0)
    systemtoolsmenu.mainloop()


def openaccessories():
    accessoriesmenu = Toplevel()
    accessoriesmenu.resizable(False, False)
    accessoriesmenu.title("")
    Button(accessoriesmenu, text='Игры', command=opengames).grid(row=0, column=0)
    Button(accessoriesmenu, text='Вещи интернетов', command=openinternetools).grid(row=1, column=0)
    Button(accessoriesmenu, text='Мультимедия', command=openmediamenu).grid(row=2, column=0)
    Button(accessoriesmenu, text='Системные вещи', command=opensystemtools).grid(row=3, column=0)
    Button(accessoriesmenu, text='Калькулятор', command=lambda: start_calc()).grid(row=4, column=0)
    Button(accessoriesmenu, text='Блокнот', command=lambda: launchnotepad()).grid(row=5, column=0)
    Button(accessoriesmenu, text='Редактор файлов разметки', command=lambda: launchword()).grid(row=6, column=0)
    Button(accessoriesmenu, text='Рисовалка', command=lambda: start_mspaint()).grid(row=7, column=0)
    accessoriesmenu.mainloop()


def openmediamenu():
    mediamenu = Toplevel()
    mediamenu.resizable(False, False)
    mediamenu.title("")
    Button(mediamenu, text='Медия плеер', command=lambda: start_media()).grid(row=0, column=0)
    Button(mediamenu, text='Запись звуков', command=lambda: start_recorder()).grid(row=1, column=0)
    Button(mediamenu, text='Настройки звука', command=lambda: start_volume_controller()).grid(row=2, column=0)
    mediamenu.mainloop()


def openinternetools():
    internetoolsmenu = Toplevel()
    internetoolsmenu.resizable(False, False)
    internetoolsmenu.title("")
    Button(internetoolsmenu, text='Браузер', command=lambda: start_browser()).grid(row=0, column=0)
    internetoolsmenu.mainloop()


def openstartup():
    startupmenu = Toplevel()
    startupmenu.resizable(False, False)
    startupmenu.title("")
    Label(startupmenu, text='(пусто)').grid(row=0, column=0)
    startupmenu.mainloop()


def openprograms():
    programsmenu = Toplevel()
    programsmenu.resizable(False, False)
    programsmenu.title("")
    Button(programsmenu, text='Приложения', command=openaccessories).grid(row=0, column=0)
    Button(programsmenu, text='StartUp', command=openstartup).grid(row=1, column=0)
    msdosbtn = Button(programsmenu, text='MS-DOS Prompt', command=lambda: startms_dos())
    msdosbtn.grid(row=2, column=0)
    windowsexplorerbtn = Button(programsmenu, text='Просмоторщик файлов Windows', command=lambda: explorer_start())
    windowsexplorerbtn.grid(row=3, column=0)
    programsmenu.mainloop()


def startclckd():
    startroot = Toplevel()
    startroot.resizable(False, False)
    startroot.title("")
    startwidth = screen_width-(screen_width + 250)
    startheight = screen_height - (screen_height - 1500)
    startroot.wm_attributes("-topmost", 1)
    programsbtn = Button(startroot, text="Программы", command=openprograms)
    programsbtn.grid(row=0, column=0)
    while True:
        startroot.update()
        startroot.update_idletasks()
        startroot.geometry("250x500+%s+%s" % (startwidth, startheight))


desktop = Tk()
if showWelcomeScreen:
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
            settingsfile = open("settings.py", "a")
            settingsfile.write("\nshowWelcomeScreen = False")
            settingsfile.close()
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
