# Python YouTube Downloader at certain location
In this Python project, the user must copy the URL of the YouTube video they like to download and then enter it in the "paste link here" part. After clicking the download button, the video will begin downloading. A notice that reads "downloaded" appears in a pop-up window below the download button when the video has finished downloading.
# Process Flow
1. Import Libraries
	command line:

from tkinter import * 
from pytube import YouTube

In this python project, we import Tkinter and pytube modules.

2. Create display window
	Tk() used to initialize tkinter to create display window
geometry() used to set the window’s width and height
resizable(0,0) set the fix size of window
title() used to give the title of window
Label() widget use to display text that users can’t able to modify.
root is the name of the window
text which we display the title of the label
font in which our text is written
pack organized widget in block

3. Create field to enter link
	link is a string type variable that stores the youtube video link that the user enters.
Entry() widget is used when we want to create an input text field.
width sets the width of entry widget
textvariable used to retrieve the value of current text variable to the entry widget
place() use to place the widget at a specific position

4. Create function to start downloading
	Url variable gets the youtube link from the link variable by get() function and then str() will convert the link in string datatype.
The video is download in the first present stream of that video by stream.first() method.

Button() widget used to display button on the window.

text which we display on the label
font in which the text is written
bg sets the background color
command is used to call the function
root.mainloop() is a method that executes when we want to run the program.

# Python YouTube Downloader Output
![image](https://user-images.githubusercontent.com/73929680/186759876-e852e9a9-6835-4379-af39-ce9a9fa8a651.png)

Enter the URL in the entry box then press download button

# Final output
![image](https://user-images.githubusercontent.com/73929680/186760251-631ec22a-eb16-4ae5-b8b0-9ea3e1ed518d.png)

Final output after Downlading the video
