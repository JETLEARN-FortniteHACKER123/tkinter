from tkinter import *
from click import command
import speech_recognition as sr
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *


Window = Tk()
#add title 
Window.title("Speech to Text Converter")
Window.geometry("800x400")


#heading
heading1 = Label(Window, text="Voice Notepad", font='bold')
heading1.grid(row=0, column=1, padx=20, pady=20)
#label and entry box to enter the text
label1 = Label(Window, text="Click button to start recording your speech: ")
label1.grid(row=1, column=0, padx=10)
#text label
Output_text = Text(Window, height=4, width=40)
Output_text.grid(row=1, column=1,  padx=20, pady=20)


#function
def translate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print( "Recording started, please speak now!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            
        except:
             text= " Sorry, could not understand audio/ recognise your voice"
        Output_text.delete(1.0, END)
        Output_text.insert(END, text)


def save():
    fout = asksaveasfile( defaultextension=".txt")  
    if fout:
        print(Output_text.get(1.0, END), file=fout)     
    else:
        messagebox.showinfo("Error", "Text not saved!")          


trans_button = Button(Window, text="Click on Me!...\n To Start Recording",font='bold', command=translate, width=20)
trans_button.grid(row=1, column=0, padx=20, pady=20)
save_button = Button(Window, text="Save the text", height=4, command=save, width=20)
save_button.grid(row=1, column=2, columnspan=3, pady=10)
Window.mainloop()