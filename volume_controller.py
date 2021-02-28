from tkinter import *
from tkinter.ttk import *
import alsaaudio
import sys


def volume(x):
    # if sys.platform == 'linux' or sys.platform == 'linux2':
    mix = alsaaudio.Mixer()
    x = float(x)
    x = int(x)
    mix.setvolume(x)


def start_volume_controller(mediamenu):
    mediamenu.destroy()
    mix = alsaaudio.Mixer()
    root = Toplevel()
    root.resizable(False, False)
    root.title("Настройки звука")
    boolvar = BooleanVar()

    speakerimg = PhotoImage(file='images/speakerimg.png')
    speakeroffimg = PhotoImage(file='images/speakeroffimg.png')

    Label(root, image=speakerimg).grid(row=0, column=0)
    Label(root, image=speakeroffimg).grid(row=2, column=0)

    currentVolume = mix.getvolume()

    volume_scale = Scale(root, from_=100, to=0, orient=VERTICAL, value=currentVolume[0], length=360, command=volume)
    volume_scale.grid(row=1, column=0)

    muteCheck = Checkbutton(root, text='Мут', offvalue=0, onvalue=1, variable=boolvar)
    muteCheck.grid(row=2, column=1)
    while True:
        root.update()
        root.update_idletasks()
        if boolvar.get():
            mix.setmute(1)
            volume_scale['state'] = DISABLED
        else:
            mix.setmute(0)
            volume_scale['state'] = NORMAL
