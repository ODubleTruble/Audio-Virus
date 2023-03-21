import os
import shutil
import keyboard
import time
from playsound import playsound

cur_dir = os.path.split(os.path.abspath(__file__))[0]
new_dir = "D:\Virus" # NO SPACES
audio_name = "\\bruh.mp3"
audio_dir = new_dir + audio_name

if cur_dir != new_dir:
    if os.path.exists(new_dir):
        print("Virus Directory is already there.")
    else:
        os.mkdir(new_dir)
        print("Virus Directory created.")

    shutil.copy(__file__, new_dir)
    shutil.copy(cur_dir + audio_name, new_dir)
    
    time.sleep(1)
    os.system(f'start {new_dir}\\main.py')
else:
    while True:
        keyboard.wait("space")
        playsound(audio_dir)

#TIP. TO STOP PROGRAM, CLICK ON TERMINAL, THEN TYPE CONTROL C!
