#!/usr/bin/env python3

import tkinter
from tkinter import *

master = tkinter.Tk()
master.geometry("750x500")

listbox = Listbox(master)
listbox.place(x=3, y=0)

enable = ['button 1', 'button 2', 'button 3']
list_for_listbox = ["one", "two", "three", "four"]

for item in list_for_listbox:
    listbox.insert(END, item)
    for y in enable:
        globals()["var{}{}".format(item, y)] = BooleanVar()
        globals()["checkbox{}{}".format(item, y)] = Checkbutton(master, text=y,
                                                                variable=globals()["var{}{}".format(item, y)])


def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    x = 0
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))

    for y in enable:
        for item in list_for_listbox:
            globals()["checkbox{}{}".format(item, y)].place_forget()
        globals()["checkbox{}{}".format(value, y)].place(x=300, y=0 + x)
        x += 50


listbox.bind('<<ListboxSelect>>', onselect)

print(enable)

mainloop()
