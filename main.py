#Importing modules
from tkinter import *
import tkinter as tk
from pytube import YouTube

# Initializing UI
root = Tk()
root.title("Media Downloader")
root.geometry("400x200+500+300")

title = Label(root, text="Insert Link Below:")
title.grid(row=0, column=0, padx=10, pady=10)

link = Entry(root, width=50)
link.grid(row=1, column=0)

button = Button(root, text='Download', width=10)
button.grid(row=1, column=1)

root.mainloop()