'''
Developer: Bishal jaiswal
copyright(c), 2022
fullDate: Monday, September 26, 2022
AppName: Music Player -onlyFor[ MP3 ]

'''

from tkinter import *
from pygame import mixer
from tkinter import filedialog, messagebox
import os
from PIL import Image, ImageTk

bColor = "#0f1a2b"

mixer.init()
root = Tk()
root.title("Music Player")
root.configure(bg=bColor)
root.geometry("920x670+240+30")
root.resizable(FALSE, FALSE)

# icon
root.iconbitmap("logo.ico")

# top


def setImage(photoName: str):  # Function to load image
    image = Image.open(photoName)
    photo = ImageTk.PhotoImage(image=image)
    return photo


topPhoto = setImage("top.png")

Label(root, image=topPhoto, bd=0, bg=bColor).pack()

# logo
logoPhoto = setImage("logo.png")
Label(root, image=logoPhoto, bg=bColor, bd=0).place(x=70, y=105)

# playButton
playButton = setImage("play.png")
Button(root, image=playButton, bg=bColor, bd=0,
       command=lambda: playMusic()).place(x=105, y=380)


def playMusic():
    musicName = musicList.get(ACTIVE)
    mixer.music.load(musicList.get(ACTIVE))
    mixer.music.play()
    status.config(text=f"Playing:  {musicName[0:-4]}")


# stopButton
stopButton = setImage("stop.png")
Button(root, image=stopButton, bg=bColor, bd=0,
       command=mixer.music.stop).place(x=30, y=500)

# resumeButton
resumeButton = setImage("resume.png")
Button(root, image=resumeButton, bd=0, bg=bColor,
       command=mixer.music.unpause).place(x=120, y=500)

# pauseButton
pauseButton = setImage("pause.png")
Button(root, image=pauseButton, bg=bColor, bd=0,
       command=mixer.music.pause).place(x=200, y=500)

# musicListBG
menu = setImage("menu.png")
Label(root, image=menu, bd=0, bg=bColor).pack(padx=10, pady=50, side=RIGHT)


# musicFrame
musicFrame = Frame(root, bd=2, relief=RIDGE)
musicFrame.place(x=330, y=350, width=560, height=250)

# readMusicFolde

Button(root, text="Open Folder", font="arial 10 bold", width=15, height=2,
       fg="white", bg="#21b3de", command=lambda: openFolder()).place(x=330, y=300)


def openFolder():
    path = filedialog.askdirectory()
    if path == "":
        messagebox.showerror("Error", "Make sure to select folder!")

    else:
        os.chdir(path)
        files = os.listdir(path)
        for file in files:
            if os.path.isfile(file) and file.endswith(".mp3"):
                musicList.insert(END, file)


scroll = Scrollbar(musicFrame)

# musicList
musicList = Listbox(musicFrame, font="arial 15 bold", fg="white", bg="#333333",
                    selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set, width=78)
scroll.config(command=musicList.yview)
scroll.pack(fill=Y, side=RIGHT)
musicList.pack(side=LEFT, fill=BOTH)

# statusBar
status = Label(root, text="", bg=bColor, fg="white",
               font="arial 12 bold italic")
status.place(x=10, y=330)


root.mainloop()
