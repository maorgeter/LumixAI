from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import tkinter as Tk
from tkinter.filedialog import askopenfilename
from pathlib import Path
import os
 

# Hello messages
print("********************\nHello and welcome to LumixAI uploader\n********************\n")
print("Please choose where do you want upload your file:")

# Menu options
menu = ["Google Drive", "Mega.nz" ]
checker = False
menuLength = len(menu)

# Menu builder
for i in range (menuLength):
    print(str((i+1)) + ". " + menu[i])
print(str(menuLength+1) + ". Exit")

# User choose menu options
while(not checker):
    val = input("Your choose: ")
    match val:
        case "1":
            # Tk().withdraw()
            gauth = GoogleAuth()           
            drive = GoogleDrive(gauth)
            filePath = askopenfilename()
            print(Path(filePath).stem + os.path.splitext(filePath)[-1]) 
            gfile = drive.CreateFile({'title': 'Hello.txt'})
            gfile.SetContentFile('./maor.txt')
            gfile.Upload()
            checker = True
        case "2":
            print("Mega")
            checker = True
        case _:
            if(val != str(menuLength+1)):
                print("Wrong option. Please try again.")
            else:
                print("Bye bye :)")
                quit()