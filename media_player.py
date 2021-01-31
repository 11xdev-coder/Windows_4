from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pygame


targetPath = ''


def open_file(playbtn_name, stopbtn_name):
    global targetPath
    targetPath = filedialog.askopenfile().name
    playbtn_name['state'] = NORMAL
    stopbtn_name['state'] = NORMAL


def close_file(playbtn_name, stopbtn_name):
    global targetPath
    targetPath = ''
    playbtn_name['state'] = DISABLED
    stopbtn_name['state'] = DISABLED


def play_targeted_sound(targetPath):
    try:
        pygame.mixer.music.load(targetPath)
        pygame.mixer.music.play(loops=0)
    except:
        messagebox.showerror("МедияПлеер", "Не удалось воспроизвести файл:%s. Проверьте, является ли этот файл медия файлом" % targetPath)


def stop_targeted_sound():
    pygame.mixer.music.stop()


def start_media():
    global targetPath
    root = Toplevel()
    pygame.init()
    root.title("МедияПлеер")
    root.resizable(False, False)
    root.geometry('500x150')

    main_menu = Menu()
    root.config(menu=main_menu)
    file_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label='Файл', menu=file_menu)
    file_menu.add_command(label='Открыть...', command=lambda: open_file(playsoundbtn, stopsoundbtn))
    file_menu.add_separator()
    file_menu.add_command(label='Закрыть', command=lambda: close_file(playsoundbtn, stopsoundbtn))

    playsoundbtnimg = PhotoImage(file='images/playsoundbtn.png')
    stopsoundbtnimg = PhotoImage(file='images/stopsoundbtnimg.png')

    playsoundbtn = Button(root, image=playsoundbtnimg, state=DISABLED, command=lambda: play_targeted_sound(targetPath))
    playsoundbtn.grid(row=0, column=0)
    stopsoundbtn = Button(root, image=stopsoundbtnimg, state=DISABLED, command=lambda: stop_targeted_sound())
    stopsoundbtn.grid(row=0, column=1)
    root.mainloop()