#Importing modules
from tkinter import *
import tkinter as tk
from pytube import YouTube

# Initializing UI
#--------------------------------------------------
root = Tk()
root.title("Media Downloader")
root.geometry("500x400+500+300")

# text field method
def text_field(textName, rowNum):
    title = Label(root, text=textName, font=('Arial', 16))
    title.grid(row=rowNum, column=0, padx=10, pady=10)

# Entry field & download button method
def entry_field(rowNum, action):
    link = Entry(root, width=50)
    link.grid(row=rowNum, column=0, padx=10)

    button = Button(root, text='Download', font=('Arial', 16), width=10, command=action)
    button.grid(row=rowNum, column=1, padx=10)

# Text fields
text_field("YouTube", 1)
text_field("Twitter", 3)
text_field("Instagram", 5)

# Entry fields
entry_field(2, None)
entry_field(4, None)
entry_field(6, None)


# Status message
status = Label(root, text="Status", font=('Arial', 16), fg='blue')
status.grid(row=7, column=0, padx=10, pady=10)
#--------------------------------------------------

root.mainloop()