from tkinter import *


def start_readme(docsMenu):
    docsMenu.destroy()
    root = Toplevel()
    root.title('Прочитай меня')
    text_field = Text(root)
    text_field.grid()
    text_field.insert(END, "This project, is Windows 95 but it Windows 4 NOT =D. This \"os\" written in python and some games made in Unity. Join our Discord server! https://discord.gg/qpnWN47u")
    root.mainloop()
