from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import tkinter as Tk
from tkinter.filedialog import askopenfilename
from pathlib import Path
import os
 

# Menu options
menu = ["Upload new file", "Read file", "List all files" ]
menuLength = len(menu)


def printUploadMenu():
    for i in range (menuLength):
        print(str((i+1)) + ". " + menu[i])
    print(str(menuLength+1) + ". Exit")

def googleDriveChooser():
    while True:
        printUploadMenu()
        val = input("Your choose: ")
        gauth = GoogleAuth()           
        drive = GoogleDrive(gauth)
        match val:
            case "1":
                # Tk().withdraw()
                filePath = askopenfilename()
                fileName = Path(filePath).stem + os.path.splitext(filePath)[-1] 
                gfile = drive.CreateFile({'title': fileName})
                gfile.SetContentFile(filePath)
                gfile.Upload()
                print("\n********************\n" + fileName + " successfully uploaded to Google Drive!\n********************\n\n")

            case "2":
                matched = False
                file_list = drive.ListFile().GetList()
                fileName = input('Please type file name: ')
                for file in file_list:
                    if fileName == file['title']:
                        file.GetContentFile(file['title'])
                        print("\n********************\n"+file['title']+"successfully downloaded from Google Drive!\n********************\n\n")
                        matched = True
                if not matched:
                    print("\n********************\nWrong file name\n********************\n\n")
            case "3":
                file_list = drive.ListFile().GetList()
                print("\n********************\n")
                for file in file_list:
                    print("File Name: %s - File ID: %s" % (file['title'], file['id']))
                print("\n********************\n\n")

            case _:
                if(val != str(menuLength+1)):
                    print("\n********************\nWrong option. Please try again!\n********************\n\n")
                else:
                    print("\n********************\nBye bye :)\n********************\n\n")
                    quit()

# Hello messages
print("********************\nHello and welcome to LumixAI GoogleDrive tool\n********************\n")
print("Please choose one option:")
googleDriveChooser()