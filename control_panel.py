from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
import sys, os, subprocess


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
                          'компоненты, выберите ее из списка и нажмите \n«Удалить».').grid(row=2, column=1, columnspan=3)
    processes = [line.split() for line in subprocess.check_output("ps").splitlines()]
    programs = Listbox(inunframe)

    for i in range(1, len(processes) - 1):
        programs.insert(END, processes[i][3])

    programs.grid(row=3, column=0, columnspan=4)

    Button(inunframe, text='Удалить', command=lambda: deleteprogram(programs)).grid(row=4, column=2)

    nb.add(inunframe, text='Установить/Удалить')


    win

    ap.mainloop()


def start_control():
    root = Toplevel()
    root.title('Панель управления')
    hardwareimg = PhotoImage(file='images/control_panel_icons/add_hardware.png')
    programsimg = PhotoImage(file='images/control_panel_icons/add_programs.png')
    Button(root, image=hardwareimg, command=lambda: add_new_hardware()).grid(row=0, column=0)
    Label(root, text='Добавить новое \nоборудование').grid(row=1, column=0)
    Button(root, image=programsimg, command=lambda: add_programs()).grid(row=0, column=1)
    Label(root, text='Добавить/Удалить \nпрограммы').grid(row=1, column=1)
    root.mainloop()


tk = Tk()
start_control()
tk.mainloop()
