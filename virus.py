'''
This is what will be ran at the target location.

IMPORTANT: Make sure dir here is the same as new_dir in injector.py
'''

import keyboard
from playsound import playsound


# dir should be the same as new_dir in injector.py
dir = 'C:\\Users\\OwenS\\OneDrive\\Documents\\Programs\\AudioVirus\\CopiedVirus'
audio_name = '\\Bruh.mp3'


print(f'Running in {dir}')
while True:
    keyboard.wait("space")
    playsound(dir + audio_name)

