# Import tkinter for User Interface creation
# Import speech_recognition for google speech recognition services
# Import time for current date time
# Import os for get current working directory

import Tkinter as tk
from Tkinter import *
import speech_recognition as sr
import time
from time import ctime
import os

# Create root windows 
root = tk.Tk()
# Set Title of the Application
root.title("Voice Notepad")
# Set Application Icon
#root.iconbitmap(r'speech.ico')
# Fix size of the windows
root.resizable(width=False, height=False)

## Create Frame for Buttons
# First parameter-> main windows(or root), bg-> Frame background
frame_button = Frame(root, bg = 'gray')
frame_button.pack(side = LEFT, fill=BOTH)
# Create Frame for TextArea
frame_textarea = Frame(root, bg = 'gray')
frame_textarea.pack(side = LEFT, fill=BOTH)

# Create Textarea with given hight, width and padding within frame frame_textarea
# First parameter-> in which frame, height-> height of the textarea, width-> width of the textarea
TextArea = Text(frame_textarea, height=21, width=50)
TextArea.pack(padx=20, pady=20)

# Create Images for Set on Button
image_mike = tk.PhotoImage(file="mike.png")
image_export = tk.PhotoImage(file="download.png")
image_reset = tk.PhotoImage(file="reset.png")  

# Method to clear Textarea
def clearScreen():
    TextArea.delete('1.0', END)

# Create method to google speech recognition
def convertSpeechToText():    
    # call google speech recognition    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    insert_data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        
        insert_data = insert_data + " " + data
        # Write speech to text converted data into Textarea
        TextArea.insert(INSERT, insert_data)                
    except sr.UnknownValueError:
        # Catch and print exception for speech which was not recognised by google API
        insert_data="Google Speech Recognition could not understand audio"
        TextArea.insert(INSERT, insert_data) 
    except sr.RequestError as e:
        # Catch and print exception for failed to call google API
        insert_data="Could not request results from Google Speech Recognition service; {0}".format(e)
        TextArea.insert(INSERT, insert_data)  
    

# Method to write Textarea data into a new text file
def writeToFile():
    # get speech to text converted data from Textarea 
    speech_data=TextArea.get(1.0,END)[:-1]
    # speech_data= speech_data.strip() 

    # get current directory in which program stored
    save_path = os.getcwd()
    # get current time stampt to use for file name
    name_of_file = getFileName()
    # file name with directory name and extention
    completeName = os.path.join(save_path, name_of_file+".txt")
    # Open file 
    file1 = open(completeName, "w")
    # write Textarea data into the file
    file1.write(speech_data)
    # Close file 
    file1.close()    

# Method to get current timestamp
def getFileName():    
    ts = time.time()
    # Convert floating point timestamp into integer
    ts=int(ts)
    # Convert Integer into String
    ts=str(ts)
    # return current timestamp string
    return ts
 

# Create button for Export Textarea data into text file, Enable google speech to text API and call Clear Text area
# First parameter-> in which Frame, text->text show on button, image-> for set Image on Button, compound->top or left(placement of image over text on button)
# command->method which called on button press, height-> height of the button, width-> width of the button
btn_export = Button(frame_button, text='Export', image=image_export, compound="top", command=writeToFile, height=80, width=80)
btn_export.pack(pady = 20, padx = 20)
btn_speak = Button(frame_button, text="Speak", image=image_mike, compound="top", command=convertSpeechToText, height=80, width=80)
btn_speak.pack(pady = 20, padx = 20)
btn_reset = Button(frame_button, text="Reset", image=image_reset, compound="top", command=clearScreen, height=80, width=80)
btn_reset.pack(pady = 20, padx = 20)

# The method mainloop has an important role for TkInter, it is waiting for events and updating the GUI
root.mainloop()
