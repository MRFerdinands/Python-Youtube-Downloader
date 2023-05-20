import tkinter
import customtkinter
from pytube import YouTube
import threading
import os

def startDownloadMP4():
    def download_thread():
        try:
            ytlink = link.get()
            ytObject = YouTube(ytlink, on_progress_callback=OnPR)
            video = ytObject.streams.get_highest_resolution()

            title.configure(text=ytObject.title, text_color="white")
            finishLabel.configure(text="")
            video.download()
            finishLabel.configure(text="Downloaded MP4!", text_color="green")
        except:
            if ytlink == "":
                finishLabel.configure(text="Please input the right link!", text_color="red")
            else:
                finishLabel.configure(text="Download Error!", text_color="red")

    # Start the download in a separate thread
    download_thread = threading.Thread(target=download_thread)
    download_thread.start()

def startDownloadMP4low():
    def download_thread():
        try:
            ytlink = link.get()
            ytObject = YouTube(ytlink, on_progress_callback=OnPR)
            video = ytObject.streams.get_lowest_resolution()

            title.configure(text=ytObject.title, text_color="white")
            finishLabel.configure(text="")
            video.download()
            finishLabel.configure(text="Downloaded MP4!", text_color="green")
        except:
            if ytlink == "":
                finishLabel.configure(text="Please input the right link!", text_color="red")
            else:
                finishLabel.configure(text="Download Error!", text_color="red")

    # Start the download in a separate thread
    download_thread = threading.Thread(target=download_thread)
    download_thread.start()


def startDownloadMP3():
    def download_thread():
        try:
            ytlink = link.get()
            ytObject3 = YouTube(ytlink, on_progress_callback=OnPR)
            music = ytObject3.streams.filter(only_audio=True).first()
            title.configure(text=ytObject3.title, text_color="white")
            finishLabel.configure(text="")
            output_file = music.download()
            base, ext = os.path.splitext(output_file)
            new_file = base + ".mp3"
            os.rename(output_file, new_file)
            finishLabel.configure(text="Downloaded MP3!", text_color="green")
        except:
            if ytlink == "":
                finishLabel.configure(text="Please input the right link!", text_color="red")
            else:
                finishLabel.configure(text="Download Error!", text_color="red")

    # Start the download in a separate thread
    download_thread = threading.Thread(target=download_thread)
    download_thread.start()

     
def OnPR(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_down = total_size - bytes_remaining
    complet = bytes_down / total_size * 100
    per = str(int(complet))
    pNumber.configure(text=per + "%")
    pNumber.update()

    # Update PBar
    pBar.set(float(complet) / 100)

# Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("400x350")
app.title("Youtube Downloader")
app.resizable(False, False)

# Ui Element
title = customtkinter.CTkLabel(app, text="Insert Youtube Link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=370, height=40, textvariable=url_var)
link.pack()

# Finish Download
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack(pady=10)

# Proggress Number
pNumber = customtkinter.CTkLabel(app, text="0%")
pNumber.pack()

pBar = customtkinter.CTkProgressBar(app, width=400, height=20)
pBar.set(0)
pBar.pack(padx=10, pady=10)

# Button MP4
download = customtkinter.CTkButton(app, text="Download MP4 (Hightest Resolution)", command=startDownloadMP4, width=400)
download.pack(padx=10, pady=10)

# Button MP4
download144 = customtkinter.CTkButton(app, text="Download MP4 (Lowest Resolution)", command=startDownloadMP4low, width=400)
download144.pack(padx=10, pady=10)

# Button MP4
downloadmp3 = customtkinter.CTkButton(app, text="Download MP3", command=startDownloadMP3, width=400, fg_color="green", hover_color="grey")
downloadmp3.pack(padx=10, pady=10)

# Run App
app.mainloop()