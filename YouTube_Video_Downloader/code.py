from tkinter import *        # IMPORTING LIBARIES
from pytube import YouTube

root = Tk()
root.geometry('500x300')  # Dimensions of tkinter tab
root.resizable(0,0)
root.title("MMM's Yotube downloader")
root.configure(bg='grey')
Label(root,text ='Youtube video downlader', font ='arial 20 bold', bg ='red').pack()
link = StringVar()

Label(root, text ='paste link here:', font ='arial 15 bold', bg = 'blue').place(x=160 , y=60)
link_enter = Entry(root, width = 70,textvariable =link).place(x=32,y=90)  # Youtube link entry label

# verifying the link and downloading the youtube vcideo
def downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download("C:\\Users\\sai\\Videos\\Captures")  #File location to download the video
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210) 
Button(root,text='download', font='arial 15 bold' ,bg ='lime', padx =2, command= downloader).place(x=180,y=150) # Trigger function

root.mainloop()

''' project by MMM '''
# Signing off
