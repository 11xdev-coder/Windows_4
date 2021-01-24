import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import *
from tkinter import filedialog
import numpy as np
import os


targetSavingath = ''
fs = 44100  # Sample rate
seconds = 9999  # Duration of recording
recording = np.ndarray


def start_rec(recordingLabel, stoprecbtn, startrecbtn):
    global recording
    # Editing Buttons state
    stoprecbtn['state'] = NORMAL
    startrecbtn['state'] = DISABLED
    recordingLabel['text'] = 'Запись: Идет...'
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)


def stop_rec(recordingLabel, stoprecbtn, startrecbtn):
    global targetSavingath
    global recording
    stoprecbtn['state'] = DISABLED
    startrecbtn['state'] = NORMAL
    recordingLabel['text'] = 'Запись: Не идет'
    write('output.wav', fs, recording)


def save_file(startrecbtn, targetPathLabel, stoprecbtn):
    global targetSavingath
    # Find out where the user wants to save the file
    targetSavingath = filedialog.asksaveasfile(title='Выбрать путь сохранения')
    targetSavingath = targetSavingath.name
    # Editing Buttons state and label text
    startrecbtn['state'] = NORMAL
    stoprecbtn['state'] = DISABLED
    targetPathLabel['text'] = "Файл: %s" % targetSavingath
    os.remove(targetSavingath)


def start_sound_recorder():
    root = Toplevel()
    # Some root settings
    root.resizable(False, False)
    root.geometry('600x150')
    ############################

    # Creating some images
    startrecimg = PhotoImage(file='images/startrec.png')
    stoprecimg = PhotoImage(file='images/stoprec.png')
    ############################

    # Creating menu
    main_menu = Menu()
    root.config(menu=main_menu)
    file_menu = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label='Файл', menu=file_menu)
    file_menu.add_command(label='Сохранить...', command=lambda: save_file(startrecbtn, targetPathLabel, stoprecbtn))
    ############################

    # Creating some UI
    targetPathLabel = Label(root, text='Файл: Не выбрано')
    targetPathLabel.grid(row=0, column=0, columnspan=5)

    recordingLabel = Label(root, text='Запись: Не идет')
    recordingLabel.grid(row=1, column=0, columnspan=5)

    startrecbtn = Button(root, image=startrecimg, state=DISABLED, command=lambda: start_rec(recordingLabel, stoprecbtn, startrecbtn))
    startrecbtn.grid(row=2, column=0)

    stoprecbtn = Button(root, image=stoprecimg, state=DISABLED, command=lambda: stop_rec(recordingLabel, stoprecbtn, startrecbtn))
    stoprecbtn.grid(row=2, column=1)

    root.mainloop()


tk = Tk()
start_sound_recorder()
tk.mainloop()
"""import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file """
