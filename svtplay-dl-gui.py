from tkinter import *
from tkinter import messagebox
import os

master = Tk()
master.title("svtplay-dl")
fullFrame = LabelFrame(master, text="SVT-Play Downloader GUI", padx=10, pady=10)
fullFrame.grid(padx=10, pady=10)
userFrame = LabelFrame(master, text="Username and password (if needed)", padx=10, pady=10)
userFrame.grid(padx=10, pady=10)

# Download function
def dlClick():
    commandLine = "svtplay-dl "
    if allCheck.get():
        commandLine = commandLine + "--all-episodes "
    if folderCheck.get():
        commandLine = commandLine + "--subfolder "
    if subCheck.get():
        commandLine = commandLine + "--subtitle "
    if forceCheck.get():
        commandLine = commandLine + "--force "
    if audioCheck.get():
        commandLine = commandLine + "--only-audio "
    if videoCheck.get():
        commandLine = commandLine + "--only-video "
    if tumbCheck.get():
        commandLine = commandLine + "--thumbnail "
    if silentCheck.get():
        commandLine = commandLine + "--silent "
    if verbCheck.get():
        commandLine = commandLine + "--verbose "
    if not len(quality.get()) == 0:
        commandLine = commandLine + "---quality " + quality.get() + " "
    if not len(username.get()) == 0:
        commandLine = commandLine + "--username " + username.get() + " "
    if not len(password.get()) == 0:
        commandLine = commandLine + "--password " + password.get() + " "
    commandRun = commandLine + link.get()
    #print(commandRun)
    os.system(commandRun)

# Qualitycheck function
def qualityCheck():
    os.system("svtplay-dl --list-quality " + link.get())

# Creating labels, entrys and buttons
linkLabel = Label(fullFrame, text="Adress:")
link = Entry(fullFrame, width=68)
qualityLabel = Label(fullFrame, text="Quality:")
quality = Entry(fullFrame, width=25)
dlButton = Button(fullFrame, text="Download", padx=120, command=dlClick)
listQuality = Button(fullFrame, text="Check available qualities (adress must be filled)", command=qualityCheck)
usernameLabel = Label(userFrame, text="Username:")
username = Entry(userFrame, width=50)
passwordLabel = Label(userFrame, text="Password:")
password = Entry(userFrame, width=50)

# Creating grid
linkLabel.grid(row=0, column=0,)
link.grid(row=0, column=1, columnspan=5, sticky=W)
qualityLabel.grid(row=1, column=0)
quality.grid(row=1, column=1, sticky=W)
listQuality.grid(row=1, column=2, columnspan=2)
allCheck = IntVar()
Checkbutton(fullFrame, text="All Episodes", variable=allCheck).grid(row=2, column=1, sticky=W)
folderCheck = IntVar()
Checkbutton(fullFrame, text="Subfolder", variable=folderCheck).grid(row=2, column=2, sticky=W)
subCheck = IntVar()
Checkbutton(fullFrame, text="Subtitles", variable=subCheck).grid(row=2, column=3, sticky=W)
forceCheck = IntVar()
Checkbutton(fullFrame, text="Overwrite", variable=forceCheck).grid(row=3, column=1, sticky=W)
audioCheck = IntVar()
Checkbutton(fullFrame, text="Only Audio", variable=audioCheck).grid(row=3, column=2, sticky=W)
videoCheck = IntVar()
Checkbutton(fullFrame, text="Only Video", variable=videoCheck).grid(row=3, column=3, sticky=W)
tumbCheck = IntVar()
Checkbutton(fullFrame, text="Thumbnails", variable=tumbCheck).grid(row=4, column=1, sticky=W)
silentCheck = IntVar()
Checkbutton(fullFrame, text="Silent", variable=silentCheck).grid(row=4, column=2, sticky=W)
verbCheck = IntVar()
Checkbutton(fullFrame, text="Verbose", variable=verbCheck).grid(row=4, column=3, sticky=W)
usernameLabel.grid(row=1, column=0,)
username.grid(row=1, column=1, columnspan=5, sticky=W)
passwordLabel.grid(row=2, column=0,)
password.grid(row=2, column=1, columnspan=5, sticky=W)
dlButton.grid(row=10, column=0, columnspan=6,)

# Start loop
master.mainloop()
