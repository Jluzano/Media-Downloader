#Importing modules
from tkinter import *
from pytube import YouTube

# Initializing UI
#--------------------------------------------------
root = Tk()
root.title("Media Downloader")
root.geometry("600x400+500+300")

# text field method
def text_field(textName, rowNum):
    title = Label(root, text=textName, font=('Arial', 16))
    title.grid(row=rowNum, column=0, padx=10, pady=10)

# Status message
status = Label(root, text="Status: N/A", font=('Arial', 16), fg='blue')
status.grid(row=7, column=0, padx=10, pady=10)

# Entry field & download button method
def button(rowNum, action):
    button = Button(root, text='Download', font=('Arial', 16), width=10, command=action)
    button.grid(row=rowNum, column=1, padx=10)

def startDownload(link, status):
    def download():
        try:
            ytLink = link.get()
            ytObject = YouTube(ytLink)
            video = ytObject.streams.get_highest_resolution()
            video.download()
            status.config(text="Status: Download completed!")
        except:
            status.config(text="Invalid YouTube link")
            root.after(3000, lambda: status.config(text="Status: N/A"))
        root.after(3000, lambda: status.config(text="Status: N/A"))
    return download

# Text fields
text_field("YouTube", 1)
text_field("Twitter", 3)
text_field("Instagram", 5)

youtubeLink = Entry(root, width=50)
youtubeLink.grid(row=2, column=0, padx=10)
twitterLink = Entry(root, width=50)
twitterLink.grid(row=4, column=0, padx=10)
instagramLink = Entry(root, width=50)
instagramLink.grid(row=6, column=0, padx=10)

# Entry fields
button(2, startDownload(youtubeLink, status))
button(4, None)
button(6, None)
#--------------------------------------------------

root.mainloop()