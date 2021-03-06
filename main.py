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
from readme_file import start_readme
from control_panel import start_control

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


def start_recorder(mediamenu):
    mediamenu.destroy()
    main = Toplevel()
    main.title('Запись звуков')
    main.geometry('200x100')
    app = App(main)
    main.mainloop()


def launchnotepad(accessoriesmenu):
    accessoriesmenu.destroy()
    fornotepad = Toplevel()
    te = text_editor(fornotepad)
    fornotepad.mainloop()


def launchword(accessoriesmenu):
    accessoriesmenu.destroy()
    forword = Toplevel()
    teword = word_editor(forword)
    forword.mainloop()


def detectosforparkour(gamesmenu):
    gamesmenu.destroy()
    if platform == 'linux' or platform == 'linux2':
        os.system("linux_runner.x86_64")
    elif platform == 'win32':
        os.system('windows_runner.exe')


def detectosforsolitaire(gamesmenu):
    gamesmenu.destroy()
    if platform == 'linux' or platform == 'linux2':
        os.system("linux_solitaire.x86_64")
    elif platform == 'win32':
        os.system('windows_solitaire.exe')


def opengames(accessoriesmenu):
    accessoriesmenu.destroy()
    gamesmenu = Toplevel()
    gamesmenu.resizable(False, False)
    gamesmenu.title("")
    Button(gamesmenu, text='Сапер', command=lambda: runner.start_minesweeper(gamesmenu)).grid(row=0, column=0)
    Button(gamesmenu, text='Змейка', command=lambda: start_snek(gamesmenu)).grid(row=1, column=0)
    Button(gamesmenu, text='Солитер', command=lambda: detectosforsolitaire(gamesmenu)).grid(row=2, column=0)
    Button(gamesmenu, text='Паркур', command=lambda: detectosforparkour(gamesmenu)).grid(row=3, column=0)
    gamesmenu.mainloop()


def opensystemtools(accessoriesmenu):
    accessoriesmenu.destroy()
    systemtoolsmenu = Toplevel()
    systemtoolsmenu.resizable(False, False)
    systemtoolsmenu.title("")
    Button(systemtoolsmenu, text='ScanDisk', command=lambda: start_scanDisk(systemtoolsmenu)).grid(row=0, column=0)
    systemtoolsmenu.mainloop()


def openaccessories(programsmenu):
    programsmenu.destroy()
    accessoriesmenu = Toplevel()
    accessoriesmenu.resizable(False, False)
    accessoriesmenu.title("")
    Button(accessoriesmenu, text='Игры', command=lambda: opengames(accessoriesmenu)).grid(row=0, column=0)
    Button(accessoriesmenu, text='Вещи интернетов', command=lambda: openinternetools(accessoriesmenu)).grid(row=1,
                                                                                                            column=0)
    Button(accessoriesmenu, text='Мультимедия', command=lambda: openmediamenu(accessoriesmenu)).grid(row=2, column=0)
    Button(accessoriesmenu, text='Системные вещи', command=lambda: opensystemtools(accessoriesmenu)).grid(row=3,
                                                                                                          column=0)
    Button(accessoriesmenu, text='Калькулятор', command=lambda: start_calc(accessoriesmenu)).grid(row=4, column=0)
    Button(accessoriesmenu, text='Блокнот', command=lambda: launchnotepad(accessoriesmenu)).grid(row=5, column=0)
    Button(accessoriesmenu, text='Редактор файлов разметки', command=lambda: launchword(accessoriesmenu)).grid(row=6,
                                                                                                               column=0)
    Button(accessoriesmenu, text='Рисовалка', command=lambda: start_mspaint(accessoriesmenu)).grid(row=7, column=0)
    accessoriesmenu.mainloop()


def openmediamenu(accessoriesmenu):
    accessoriesmenu.destroy()
    mediamenu = Toplevel()
    mediamenu.resizable(False, False)
    mediamenu.title("")
    Button(mediamenu, text='Медия плеер', command=lambda: start_media(mediamenu)).grid(row=0, column=0)
    Button(mediamenu, text='Запись звуков', command=lambda: start_recorder(mediamenu)).grid(row=1, column=0)
    Button(mediamenu, text='Настройки звука', command=lambda: start_volume_controller(mediamenu)).grid(row=2, column=0)
    mediamenu.mainloop()


def openinternetools(accessoriesmenu):
    accessoriesmenu.destroy()
    internetoolsmenu = Toplevel()
    internetoolsmenu.resizable(False, False)
    internetoolsmenu.title("")
    Button(internetoolsmenu, text='Браузер', command=lambda: start_browser(internetoolsmenu)).grid(row=0, column=0)
    internetoolsmenu.mainloop()


def openstartup(programsmenu):
    programsmenu.destroy()
    startupmenu = Toplevel()
    startupmenu.resizable(False, False)
    startupmenu.title("")
    Label(startupmenu, text='(пусто)').grid(row=0, column=0)
    startupmenu.mainloop()


def openprograms(startroot):
    startroot.destroy()
    programsmenu = Toplevel()
    programsmenu.resizable(False, False)
    programsmenu.title("")
    Button(programsmenu, text='Приложения', command=lambda: openaccessories(programsmenu)).grid(row=0, column=0)
    Button(programsmenu, text='StartUp', command=lambda: openstartup(programsmenu)).grid(row=1, column=0)
    msdosbtn = Button(programsmenu, text='MS-DOS Prompt', command=lambda: startms_dos(programsmenu))
    msdosbtn.grid(row=2, column=0)
    windowsexplorerbtn = Button(programsmenu, text='Просмоторщик файлов Windows',
                                command=lambda: explorer_start(programsmenu))
    windowsexplorerbtn.grid(row=3, column=0)
    programsmenu.mainloop()


def openDocs(startroot):
    startroot.destroy()
    docsMenu = Toplevel()
    docsMenu.resizable(False, False)
    docsMenu.title("")
    Button(docsMenu, text='Прочитай меня', command=lambda: start_readme(docsMenu)).grid(row=0, column=0)
    docsMenu.mainloop()


def openSettings(startroot):
    startroot.destroy()
    setMenu = Toplevel()
    setMenu.resizable(False, False)
    setMenu.title("")
    Button(setMenu, text='Панель управления', command=lambda: start_control(desktop, desktoplbl, setMenu)).grid(row=0,
                                                                                                                column=0
                                                                                                                )
    setMenu.mainloop()


def startclckd():
    startroot = Toplevel()
    startroot.resizable(False, False)
    startroot.title("")
    startroot.protocol("WM_DELETE_WINDOW", lambda: print('Nope'))
    startwidth = screen_width - (screen_width + 250)
    startheight = screen_height - (screen_height - 1500)
    startroot.wm_attributes("-topmost", 1)
    programsbtn = Button(startroot, text="Программы", command=lambda: openprograms(startroot))
    programsbtn.grid(row=0, column=0)
    docsMenuBtn = Button(startroot, text="Документы", command=lambda: openDocs(startroot))
    docsMenuBtn.grid(row=1, column=0)
    setMenuBtn = Button(startroot, text="Настройки", command=lambda: openSettings(startroot))
    setMenuBtn.grid(row=2, column=0)
    Button(startroot, text='Закрыть', command=lambda: startroot.destroy()).grid(row=7, column=0)
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
    showcheckbox = Checkbutton(tips, text='Показывать это окно при последующих запусках Windows', variable=showing,
                               onvalue=1, offvalue=0)
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
desktop['bg'] = 'dark blue'

fd = open('system/desktopbg.txt', 'r')
img = PhotoImage(file=fd.read())

desktoplbl = Label(desktop, bg='dark blue', image=img)
desktoplbl.pack(expand=YES, fill=BOTH)

fd.close()

desktop.geometry(ra)
taskbar = Frame(desktop, bg="gray")
taskbar.pack(fill=X, side=BOTTOM)
startbtn = Button(taskbar, text='Start', bg="light gray", activebackground="light gray", bd=7, command=startclckd)
startbtn.grid(column=0)
desktop.mainloop()
