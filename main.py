from tkinter import *
import tkinter as tk
from pytube import YouTube

class downloader():
    def __init__(self, root):
        self.root = root
        self.root.title("Media Downloader")

        frame = Frame(self.root, bd=10, width=1000, height=100, relief=RIDGE)


        b = Button(frame, text="Download")
        b.grid(row=1, column=1)

if __name__ == '__main__':
    root = tk.Tk()
    application = downloader(root)
    root.mainloop()