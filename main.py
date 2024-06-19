#Importing modules
from tkinter import *
from pytube import YouTube

class MediaDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Downloader")
        self.root.geometry("600x400+500+300")

        # Status message
        status = Label(root, text="Status: N/A", font=('Arial', 16), fg='blue')
        status.grid(row=7, column=0, padx=10, pady=10)

        # Text fields
        self.text_field("YouTube", 1)
        self.text_field("Twitter", 3)
        self.text_field("Instagram", 5)

        #Entry fields to place links
        youtubeLink = Entry(root, width=50)
        youtubeLink.grid(row=2, column=0, padx=10)
        twitterLink = Entry(root, width=50)
        twitterLink.grid(row=4, column=0, padx=10)
        instagramLink = Entry(root, width=50)
        instagramLink.grid(row=6, column=0, padx=10)

        # Initializing download buttons
        self.button(2, self.startDownload(youtubeLink, status))
        self.button(4, self.startDownload(None, status))
        self.button(6, self.startDownload(None, status))

    # text field method
    def text_field(self, textName, rowNum):
        title = Label(self.root, text=textName, font=('Arial', 16))
        title.grid(row=rowNum, column=0, padx=10, pady=10)

    # Entry field & download button method
    def button(self, rowNum, action):
        button = Button(self.root, text='Download', font=('Arial', 16), width=10, command=action)
        button.grid(row=rowNum, column=1, padx=10)

    # Method called when button is pressed
    def startDownload(self, link, status):
        # Placing another function inside because we do not want to call it when the program starts
        def download():
            try:
                # grabbing and downloading YouTube video
                ytLink = link.get()
                ytObject = YouTube(ytLink)
                video = ytObject.streams.get_highest_resolution()
                video.download()
                status.config(text="Status: Download completed!")
            except:
                # Throw error
                status.config(text="Invalid YouTube link")
                self.root.after(3000, lambda: status.config(text="Status: N/A"))
            self.root.after(3000, lambda: status.config(text="Status: N/A"))
        return download

if __name__ == "__main__":
    root = Tk()
    app = MediaDownloader(root)
    root.mainloop()