import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import shutil

filepath = ''
filepath2 = ''

def quit():
    global app
    app.quit()

def check_file():
    check = os.path.isfile('data.txt')
    return check

def openFile():
    global gta_dir
    filepath = filedialog.askdirectory()
    with open('data.txt', 'w') as f:
        f.write(filepath)
    part1_text.set(filepath)
    gta_dir = filepath

def openFile2():
    global mod_file
    filepath2 = filedialog.askopenfilename()
    part2_text.set(filepath2)
    mod_file = filepath2

def autofill():
    global gta_dir
    with open('data.txt', 'r') as auto:
        variable = auto.readline()
        part1_text.set(variable)
        gta_dir = variable

def run():
    global gta_dir
    global mod_file
    x = gta_dir
    y = mod_file
    shutil.unpack_archive(y, x)

#Checks if text file exists
status = check_file()
if status == False:
    with open(r'data.txt', 'w') as fp:
        fp.close()

#Creates window
app = tk.Tk()

#Directory1
part1_text = StringVar()
part1_label= Label(app, text='GTA directory')
part1_label.grid(row = 0, column = 0, pady=10)
part1_entry = Entry(app, textvariable=part1_text, width = 75)
part1_entry.grid(row = 0, column = 1, pady=10)
#Directory2
part2_text = StringVar()
part2_label= Label(app, text='Mod file')
part2_label.grid(row = 1, column = 0, pady=10)
part2_entry = Entry(app, textvariable=part2_text, width = 75)
part2_entry.grid(row = 1, column = 1, pady=10)
#Button1
Confirm = Button(app, text="Open Directory", command = openFile)
Confirm.grid(row = 0, column = 2, pady=10)
#Button2
Confirm2 = Button(app, text="Open File", command = openFile2)
Confirm2.grid(row = 1, column = 2, pady=10)
#AddMod
AddMod = Button(app, text="Add the Mod", command = run)
AddMod.grid(row = 3, column = 1, pady=10)
#Quit
Quit = Button(app, text = "Close", command = quit)
Quit.grid(row = 3, column = 2, pady= 10)


#Defines window size
app.title('EasyGTA')
app.geometry('630x140')

#Automatically fills gta directory line if available
autofill()

#Starts program
app.mainloop()

