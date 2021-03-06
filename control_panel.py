from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
import sys, os, subprocess, time, random
from PIL import Image


def detect_cd_rom(hardware_types):
    if hardware_types.get() == 'CD-ROM контроллер':
        messagebox.showerror("", "Вставьте диск названный \"Windows 4 NOT CD-ROM\" и потом нажмите OK")
    else:
        messagebox.showinfo("",
                            "Новое оборудование поставлено успешно! Чтобы оно заработало вам надо перезагрузить ваш "
                            "компьютер")
        sys.exit(0)


def add_new_hardware():
    anh = Toplevel()
    anh.resizable(False, False)
    anh.title('Добавить новое оборудование')
    hrwInstallImg = PhotoImage(file='images/control_panel_icons/hrwInstallImg.png')
    Label(anh, image=hrwInstallImg).grid(row=0, column=0, rowspan=7)
    Label(anh, text='Выберите тип оборудования которое вы хотите установить.').grid(row=0, column=1, columnspan=3)
    Label(anh, text='Типы оборудования:').grid(row=1, column=1, columnspan=3)
    hardware_types = Combobox(anh, values=("CD-ROM контроллер", "Дисплей адаптер", "Контроллеры дискетами",
                                           "Контроллер жесткими дисками", "Клавиатура", "Драйверы технологии памяти "
                                                                                        "(MTD)",
                                           "Модем", "Мышка", "Многофункциональные адаптеры", "Сетевые адаптеры",
                                           "Остальные устройства", "Разъем PCMCIA", "Порты(COM & LPT)", "Принтер",
                                           "Контроллеры SCSI", "Звуковые, видео и игровые контроллеры",
                                           "Системные устройства"))
    hardware_types.current(0)
    hardware_types.grid(row=2, column=1, columnspan=3)
    Button(anh, text='< Назад', state=DISABLED).grid(row=8, column=1)
    Button(anh, text='Далее >', command=lambda: detect_cd_rom(hardware_types)).grid(row=8, column=2)
    anh.mainloop()


def install():
    targetFile = filedialog.askopenfile(initialdir='/').name
    os.system(targetFile)


def deleteprogram(programlist):
    select = list(programlist.curselection())
    select.reverse()
    for i in select:
        programlist.delete(i)


def add_programs():
    ap = Toplevel()

    programsetupimg = PhotoImage(file='images/control_panel_icons/add_programs_setupimg.png')
    deleteprogramimg = PhotoImage(file='images/control_panel_icons/delete_programs.png')

    ap.resizable(False, False)
    ap.title('Добавить/Удалить Программы')
    nb = Notebook(ap)
    nb.pack(fill=BOTH, expand=YES)
    inunframe = Frame(nb)

    Label(inunframe, image=programsetupimg).grid(row=0, column=0)
    Label(inunframe, text='Чтобы установить новую программу с дискеты или привода \nCD-ROM, нажмите «Установить».') \
        .grid(row=0, column=1, columnspan=3)
    Button(inunframe, text='Установить', command=install).grid(row=1, column=2)
    Label(inunframe, image=deleteprogramimg).grid(row=2, column=0)
    Label(inunframe, text='Следующее программное обеспечение может быть автоматически удалено \n'
                          'Windows. Чтобы удалить программу или изменить ее установленные \n'
                          'компоненты, выберите ее из списка и нажмите \n«Удалить».').grid(row=2, column=1,
                                                                                           columnspan=3)
    processes = [line.split() for line in subprocess.check_output("ps").splitlines()]
    programs = Listbox(inunframe)

    for i in range(1, len(processes) - 1):
        programs.insert(END, processes[i][3])

    programs.grid(row=3, column=0, columnspan=4)

    Button(inunframe, text='Удалить', command=lambda: deleteprogram(programs)).grid(row=4, column=2)

    nb.add(inunframe, text='Установить/Удалить')

    winsetupframe = Frame(nb)

    Label(winsetupframe, text='Чтобы добавить или удалить компонент, установите флажок.').grid(row=0, column=0,
                                                                                               columnspan=4)
    Label(winsetupframe, text='Компоненты:')
    Checkbutton(winsetupframe, text='Параметры доступности').grid(row=2, column=0, columnspan=4)
    Checkbutton(winsetupframe, text='Приложения').grid(row=3, column=0, columnspan=4)
    Checkbutton(winsetupframe, text='Связь').grid(row=4, column=0, columnspan=4)
    Checkbutton(winsetupframe, text='Дисковые инструменты').grid(row=5, column=0, columnspan=4)
    Checkbutton(winsetupframe, text='Microders Exchange').grid(row=6, column=0, columnspan=4)
    Checkbutton(winsetupframe, text='Microders факс').grid(row=7, column=0, columnspan=4)
    Checkbutton(winsetupframe, text='Многоязычная поддержка').grid(row=8, column=0, columnspan=4)
    Checkbutton(winsetupframe, text='Мультимедиа').grid(row=9, column=0, columnspan=4)
    Checkbutton(winsetupframe, text='Сеть Microders').grid(row=10, column=0, columnspan=4)

    Button(winsetupframe, text='OK', command=lambda: messagebox.showerror('', 'Вставьте диск '
                                                                              'названный \"Windows 4 NOT CD-ROM\" и '
                                                                              'нажмите OK')).grid(row=11, column=0)
    Button(winsetupframe, text='Отмена', command=lambda: ap.destroy()).grid(row=11, column=1)
    Button(winsetupframe, text='Применить', command=lambda: messagebox.showerror('', 'Вставьте диск '
                                                                                     'названный \"Windows 4 NOT CD-ROM\" и '
                                                                                     'нажмите OK')).grid(row=11,
                                                                                                         column=2)

    nb.add(winsetupframe, text='Установка Windows')

    startupframe = Frame(nb)

    floppyStartUpDisk = PhotoImage(file='images/control_panel_icons/floppy_startup_disk.png')

    Label(startupframe, image=floppyStartUpDisk).grid(row=0, column=0)

    Label(startupframe, text='Если у вас возникли проблемы с запуском Windows, вы можете \nиспользовать '
                             'загрузочный диск '
                             'для запуска компьютера, запуска \nдиагностических программ и устранения любых проблем. '
                             'Чтобы создать загрузочный диск,\n нажмите «Создать диск ...». '
                             'Вам понадобится одна дискета.').grid(row=0, column=1, columnspan=2)

    Button(startupframe, text='Создать диск...', command=lambda: messagebox.showerror('Ошибка создания загрузочного '
                                                                                      'диска',
                                                                                      'Диск «A» не является дисководом '
                                                                                      'для '
                                                                                      'гибких '
                                                                                      'дисков или подключен к сетевому '
                                                                                      'диску. '
                                                                                      'Windows не может создать '
                                                                                      'загрузочный '
                                                                                      'диск')).grid(row=1, column=2)

    nb.add(startupframe, text='Загрузочный диск')

    ap.mainloop()


def dateTime():
    dt = Toplevel()
    dt.title("Свойства Даты/Времени")
    dt.resizable(False, False)

    nb = Notebook(dt)
    nb.pack(fill=BOTH, expand=YES)

    data_time_frame = Frame(nb)

    date = LabelFrame(data_time_frame, text='Дата')
    date.grid(row=0, column=0)

    monthes = Combobox(date, values=('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
                                     'Октябрь', 'Ноябрь', 'Декабрь'))
    monthes.grid(row=0, column=0)
    monthes.current()

    time_and_date = time.asctime()
    time_and_date = time_and_date.split()
    if time_and_date[1] == 'Jan':
        monthes.current(0)

    elif time_and_date[1] == 'Feb':
        monthes.current(1)

    elif time_and_date[1] == 'Mar':
        monthes.current(2)

    elif time_and_date[1] == 'Apr':
        monthes.current(3)

    elif time_and_date[1] == 'May':
        monthes.current(4)

    elif time_and_date[1] == 'Jun':
        monthes.current(5)

    elif time_and_date[1] == 'Jul':
        monthes.current(6)

    elif time_and_date[1] == 'Aug':
        monthes.current(7)

    elif time_and_date[1] == 'Sep':
        monthes.current(8)

    elif time_and_date[1] == 'Oct':
        monthes.current(9)

    elif time_and_date[1] == 'Nov':
        monthes.current(10)

    elif time_and_date[1] == 'Dec':
        monthes.current(11)

    year = Spinbox(date, from_=2020, to=3000)

    if time_and_date[4] >= '2020':
        year.insert(END, time_and_date[4])
    else:
        year.insert(END, 'error')

    year.grid(row=0, column=1)

    days = Frame(date, relief=SUNKEN)
    if time_and_date[1] == 'Jan' or time_and_date[1] == 'Mar' or time_and_date[1] == 'Apr' \
            or time_and_date[1] == 'May' or time_and_date[1] == 'Jul' or time_and_date[1] == 'Aug' \
            or time_and_date[1] == 'Oct' or time_and_date[1] == 'Dec':
        for dnf in range(1, 9):
            Button(days, text=dnf).grid(row=0, column=dnf)

        for dnf in range(7, 15):
            Button(days, text=dnf).grid(row=1, column=dnf - 7)

        for dnf in range(14, 22):
            Button(days, text=dnf).grid(row=2, column=dnf - 14)

        for dnf in range(22, 30):
            Button(days, text=dnf).grid(row=3, column=dnf - 22)

        for dnf in range(30, 32):
            Button(days, text=dnf).grid(row=4, column=dnf - 30)

    elif time_and_date[1] == 'Feb':
        for f in range(0, 8):
            Button(days, text=f).grid(row=0, column=f)

        for f in range(7, 15):
            Button(days, text=f).grid(row=1, column=f - 7)

        for f in range(14, 22):
            Button(days, text=f).grid(row=2, column=f - 14)

        for f in range(22, 28):
            Button(days, text=f).grid(row=3, column=f - 22)

    else:
        for o in range(0, 8):
            Button(days, text=o).grid(row=0, column=o)

        for o in range(7, 15):
            Button(days, text=o).grid(row=1, column=o - 7)

        for o in range(14, 22):
            Button(days, text=o).grid(row=2, column=o - 14)

        for o in range(22, 31):
            Button(days, text=o).grid(row=3, column=o - 22)

    days.grid(row=1, column=0, columnspan=2)

    time_frame = LabelFrame(data_time_frame, text='Время')
    time_frame.grid(row=0, column=1)

    timelbl = Label(time_frame, text=time_and_date[3])
    timelbl.grid(row=0, column=0)

    nb.add(data_time_frame, text='Дата/Время')

    Button(data_time_frame, text='OK', command=lambda: data_time_frame.destroy()).grid(row=4, column=0)
    Button(data_time_frame, text='Отменить', command=lambda: data_time_frame.destroy()).grid(row=4, column=1)

    while True:
        dt.update()
        dt.update_idletasks()
        time_and_date = time.asctime().split()
        timelbl['text'] = time_and_date[3]


def exitandapplybg(desktop, root, colour):
    root.destroy()
    try:
        desktop['bg'] = colour.get()
    except:
        messagebox.showerror('Дисплэй', 'Не удалось разпознать введенный вами цвет!')


def applybg(desktop, colour):
    try:
        desktop['bg'] = colour.get()
    except:
        messagebox.showerror('Дисплэй', 'Не удалось разпознать введенный вами цвет!')


def applysv(desktoplbl, screen_width, screen_height, screensavers):
    if screensavers.get() == 'Windows 4 NOT':
        # Opening image with Pillow
        screensavernormal = Image.open("images/screensavers/windows_4.png")
        width = screen_width
        height = screen_height
        # Resizing image
        screensaverresized = screensavernormal.resize((width, height - 125), Image.ANTIALIAS)
        # Saving resized image
        screensaverresized.save("images/screensavers/windows_4.png")
        # Opening image with tkinter
        fd = open('system/desktopbg.txt', 'w')
        fd.write('images/screensavers/windows_4.png')

        img = PhotoImage(file='images/screensavers/windows_4.png')

        desktoplbl.configure(image=img)
        desktoplbl.image = img

        fd.close()

    elif screensavers.get() == 'n00b':
        # Opening image with Pillow
        screensavernormal = Image.open("images/screensavers/n00b.png")
        width = screen_width
        height = screen_height
        # Resizing image
        screensaverresized = screensavernormal.resize((width, height - 125), Image.ANTIALIAS)
        # Saving resized image
        screensaverresized.save("images/screensavers/n00b.png")
        # Opening image with tkinter
        fd = open('system/desktopbg.txt', 'w')
        fd.write('images/screensavers/n00b.png')

        img = PhotoImage(file='images/screensavers/n00b.png')

        desktoplbl.configure(image=img)
        desktoplbl.image = img

        fd.close()

    else:
        desktoplbl.configure(image=None)
        desktoplbl.image = None


def exitandapplysv(desktoplbl, desktop, root, screen_width, screen_height, screensavers):
    if screensavers.get() == 'Windows 4 NOT':
        # Opening image with Pillow
        screensavernormal = Image.open("images/screensavers/windows_4.png")
        width = screen_width
        height = screen_height
        # Resizing image
        screensaverresized = screensavernormal.resize((width, height - 125), Image.ANTIALIAS)
        # Saving resized image
        screensaverresized.save("images/screensavers/windows_4.png")
        # Opening image with tkinter
        fd = open('system/desktopbg.txt', 'w')
        fd.write('images/screensavers/windows_4.png')

        img = PhotoImage(file='images/screensavers/windows_4.png')

        desktoplbl.configure(image=img)
        desktoplbl.image = img

        fd.close()

    elif screensavers.get() == 'n00b':
        # Opening image with Pillow
        screensavernormal = Image.open("images/screensavers/n00b.png")
        width = screen_width
        height = screen_height
        # Resizing image
        screensaverresized = screensavernormal.resize((width, height - 125), Image.ANTIALIAS)
        # Saving resized image
        screensaverresized.save("images/screensavers/n00b.png")
        # Opening image with tkinter
        fd = open('system/desktopbg.txt', 'w')
        fd.write('images/screensavers/n00b.png')

        img = PhotoImage(file='images/screensavers/n00b.png')

        desktoplbl.configure(image=img)
        desktoplbl.image = img

        fd.close()

    else:
        desktoplbl.configure(image=None)
        desktoplbl.image = None
        fd = open('system/desktopbg.txt', 'w')
        fd.write('')
        fd.close()

    root.destroy()


def display(desktop, desktoplbl):
    d = Toplevel()
    d.resizable(False, False)
    d.title('Дисплэй')
    screen_width = d.winfo_screenwidth()
    screen_height = d.winfo_screenheight()

    nb = Notebook(d)

    bgframe = Frame(nb)

    Label(bgframe, text='Введите цвет фона:(английской раскладкой или RGB)').grid(row=0, column=0)
    colour = Entry(bgframe)
    colour.grid(row=1, column=0)

    Button(bgframe, text='OK', command=lambda: exitandapplybg(desktoplbl, d, colour)).grid(row=2, column=0)
    Button(bgframe, text='Отменить', command=lambda: d.destroy()).grid(row=2, column=1)
    Button(bgframe, text='Применить', command=lambda: applybg(desktoplbl, colour)).grid(row=2, column=2)

    svframe = Frame(nb)

    svlblframe = Label(svframe, text='Заставка')

    screensaversvalue = StringVar()
    svs = Combobox(svlblframe, values=('None', 'Windows 4 NOT', 'n00b'), textvariable=screensaversvalue)
    svs.current(0)
    svs.grid(row=0, column=0)

    svlblframe.grid(row=0, column=0)

    Button(svframe, text='OK', command=lambda: exitandapplysv(desktoplbl, desktop, d, screen_width, screen_height, svs)) \
        .grid(row=1, column=0)
    Button(svframe, text='Отменить', command=lambda: d.destroy()).grid(row=1, column=1)
    Button(svframe, text='Применить', command=lambda: applysv(desktoplbl, screen_width, screen_height, svs)) \
        .grid(row=1, column=2)

    nb.add(bgframe, text='Фон')
    nb.add(svframe, text='Заставка')
    nb.grid()

    d.mainloop()


def fonts():
    f = Toplevel()
    f.title('Шрифты')

    canvas = Canvas(f)
    scrollbar = Scrollbar(f, orient="vertical", command=canvas.yview)
    fontsframe = Frame(canvas)

    fontsframe.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=fontsframe, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    fonts = list(font.families())
    fontsindex = -1
    fontsTimg = PhotoImage(file='images/control_panel_icons/fontT.png')
    fontsAimg = PhotoImage(file='images/control_panel_icons/fontA.png')

    for i in range(0, len(fonts) - 1, 2):
        for r in range(0, 11):
            fontsindex += 1

            number = random.randint(0, 1)

            if number == 0:
                imageneeded = fontsTimg
            else:
                imageneeded = fontsAimg

            Label(fontsframe, image=imageneeded).grid(row=i, column=r)
            Label(fontsframe, text=fonts[fontsindex]).grid(row=i + 1, column=r)

    f.mainloop()


def start_control(desktop, desktoplbl, setMenu):
    # setMenu.destroy()
    root = Toplevel()
    root.title('Панель управления')

    hardwareimg = PhotoImage(file='images/control_panel_icons/add_hardware.png')
    programsimg = PhotoImage(file='images/control_panel_icons/add_programs.png')
    dateTimeImg = PhotoImage(file='images/control_panel_icons/date_time.png')
    displayImg = PhotoImage(file='images/control_panel_icons/display.png')
    fontsImg = PhotoImage(file='images/control_panel_icons/fonts.png')

    Button(root, image=hardwareimg, command=lambda: add_new_hardware()).grid(row=0, column=0)
    Label(root, text='Добавить новое \nоборудование').grid(row=1, column=0)
    Button(root, image=programsimg, command=lambda: add_programs()).grid(row=0, column=1)
    Label(root, text='Добавить/Удалить \nпрограммы').grid(row=1, column=1)
    Button(root, image=dateTimeImg, command=lambda: dateTime()).grid(row=0, column=2)
    Label(root, text='Дата/Время').grid(row=1, column=2)
    Button(root, image=displayImg, command=lambda: display(desktop, desktoplbl)).grid(row=0, column=3)
    Label(root, text='Дисплэй').grid(row=1, column=3)
    Button(root, image=fontsImg, command=lambda: fonts()).grid(row=0, column=4)
    Label(root, text='Шрифты').grid(row=1, column=4)
    root.mainloop()


tk = Tk()
start_control(1, 1, 3)
tk.mainloop()
