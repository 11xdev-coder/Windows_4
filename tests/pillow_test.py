from tkinter import *
from PIL import Image

img = Image.open("../images/welcomeinimg.png")
width = 100
height = 64
resized_img = img.resize((width, height), Image.ANTIALIAS)
width, height = resized_img.size
print(width, height)
root = Tk()
Label(root, image=resized_img).grid(row=0,column=0)
root.mainloop()
