from tkinter import *
from gtts import gTTS
import os


# create tkinter window
root = Tk()


# styling the frame which helps to make our background stylish
frame1 = Frame(root, bg="lightpink", height="150")


#PLACE  the widgets in gui window
frame1.pack(fill=X)

frame2 = Frame(root, bg="lightgreen", height="750")
frame2.pack(fill=X)


#styling the label which show the text in our tkinter window
label = Label(frame1, text="Text to Speech Converter", font='bold',  bg="lightpink")
             
             
label.place(x=100, y=70)
# entry is used to enter the text
entry = Entry(frame2, width=45, bd=4 , font=14)
entry.place(x=130, y=52)
entry.insert(0, "")

# function which will convert the text to speech
def play():
    language = 'en'
    myobj = gTTS(text=entry.get(), lang=language, slow=False)
    myobj.save("convert.wav")
    os.system("convert.wav")


#create a button which holds our play function
btn = Button(frame2, text="SUBMIT", width=15, pady=10,font='bold',command=play, bg="Blue")
btn.place(x=220, y=120)

root.title("Text to Speech Converter")

root.geometry("600x550+350+200")

root.mainloop()