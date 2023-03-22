'''
This file is the injector which only exists and runs from the source/original location.
It's purpose is to copy the ncessary files to the new location,
then execute some file in the new location before terminating.

IMPORTANT: Make sure new_dir here is the same as dir in virus.py.
'''

import os
import shutil
import time


cur_dir = input('Directory this script resides in: ')# Was os.path.split(os.path.abspath(__file__))[0]
new_dir = 'C:\\Users\\OwenS\\OneDrive\\Documents\\Programs\\AudioVirus\\CopiedVirus'
files_to_copy = ['\\virus.exe', '\\Bruh.mp3']
run_upon_termination = '\\virus.exe'


def termination_countdown(length):
    print('Terminating in...')
    for time_left in range(length, 0, -1):
        print(time_left)
        time.sleep(1)


def run_new_script():
    # Puts quotes around every directory in new_dir that has a space in it.
    dirs_in_new_dir = new_dir.split('\\')
    for i in range(len(dirs_in_new_dir)):
        if ' ' in dirs_in_new_dir[i]:
            dirs_in_new_dir[i] = f'"{dirs_in_new_dir[i]}"'
    new_dir_with_quotes = '\\'.join(dirs_in_new_dir)

    print(f'Running {new_dir}{run_upon_termination}')
    time.sleep(1)
    os.system(f'start {new_dir_with_quotes}{run_upon_termination}')


if os.path.exists(new_dir):
    print("The target directory already exists.")
    print("No actions will be taken.")
    termination_countdown(5)
else:
    print("The target directory doesn't exist.")
    print("Creating target location and copying files to it...")
    
    os.mkdir(new_dir)
    print("Target directory created.")
    for file_name in files_to_copy:
        shutil.copy(cur_dir + file_name, new_dir)
        print(f'Copied file {file_name[1:]}')
    print("All files copied.")
        
    run_new_script()
    
    termination_countdown(10)

