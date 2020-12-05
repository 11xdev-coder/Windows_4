from windowsSetup import start
import os
from tkinter import *

if os.path.exists('setup/success'):
    pass
else:
    start()