import tkinter as tk
from tkinter import *
from tkinter import filedialog
import threading
import pyaudio
import wave
import os


class App():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100

    frames = []

    def __init__(self, master):
        self.isrecording = False
        self.startrecimg = PhotoImage(file='images/startrec.png')
        self.stoprecimg = PhotoImage(file='images/stoprec.png')
        self.button1 = tk.Button(master, image=self.startrecimg, command=self.startrecording)
        self.button2 = tk.Button(master, image=self.stoprecimg, command=self.stoprecording, state=DISABLED)

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)


    def startrecording(self):
        self.button1['state'] = DISABLED
        self.button2['state'] = NORMAL
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.sample_format, channels=self.channels, rate=self.fs,
                                  frames_per_buffer=self.chunk, input=True)
        self.isrecording = True

        t = threading.Thread(target=self.record)
        t.start()


    def stoprecording(self):
        self.isrecording = False
        self.button1['state'] = NORMAL
        self.button2['state'] = DISABLED
        self.filename = filedialog.asksaveasfile(title="Выберите путь сохранения")
        self.filename = self.filename.name
        os.remove(self.filename)
        self.filename = self.filename + ".wav"
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def record(self):
        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)