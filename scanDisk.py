from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import time, os


def startScan(progressbar, closebtn, startbtn, root):
    closebtn['state'] = DISABLED
    startbtn['state'] = DISABLED
    for i in range(1, 99):
        progressbar.step(1)
        root.update()
        root.update_idletasks()
        time.sleep(0.2)
    if not os.path.exists("system32"):
        messagebox.showerror("ScanDisk", "Ваш компьютер под угрозой! ScanDisk возобновит файл \nsystem32, но ваш компьютер должен будет перезагрузится!")
        os.mkdir("system32")
        sys.exit(0)
    else:
        messagebox.showinfo("ScanDisk", "Сканирование диска завершено успешно!")
    progressbar.step(-99)
    closebtn['state'] = NORMAL
    startbtn['state'] = NORMAL


def start_scanDisk():
    root = Toplevel()
    root.resizable(False, False)
    root.title("ScanDisk")

    scpb = Progressbar(root, length=360)
    scpb.grid(row=0, column=0, columnspan=4)

    startbtn = Button(root, text='Начать', command=lambda: startScan(scpb, closebtn, startbtn, root))
    startbtn.grid(row=1, column=1)

    closebtn = Button(root, text='Закрыть', command=lambda: root.destroy())
    closebtn.grid(row=1, column=2)
    root.mainloop()

