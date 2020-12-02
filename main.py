from windowsSetup import start
import os

if os.path.exists('setup/success'):
    pass
else:
    start()