import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        print("Download Complete!")
    except:
        print("Youtube link is invalid")
    


#System Settings
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard),
customtkinter.set_default_color_theme('blue')

#Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app , text="Insert a youtube link")
title.pack(padx=10,pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=40, textvariable=url_var)
link.pack()

# download button
download = customtkinter.CTkButton(app,text="Downloal",command=startDownload)
download.pack(padx=10,pady=10)

# Run app
app.mainloop()