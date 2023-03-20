from tkinter import *
from pytube import YouTube

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



root = Tk()
root.geometry = "500 X 300"  # Size of the gui created
root.resizable(800, 500)  # This allows the window to be adjustable with settings
root.title("Youtube MP4 downloader")  # Title

Label(root, text="Download Youtube videos for free (we don't steal info here", font="san-serif 14 bold").pack()
link = StringVar() # Variable Type
Label(root, text="Paste Your Link here", font="san-serif 15 bold").place(x=150, y=55)  # Text above the link input
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=85)  #Input area for the link to be pasted into

Button(root, text="Download", font="san-serif 15 bold", bg="red", padx=2, command="download").place(x=100, y=150)


def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="Downloaded", font="arial 15").place(x=100, y=120)

root.mainloop()





