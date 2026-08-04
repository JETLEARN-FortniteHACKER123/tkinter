import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr


def speak_now():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        messagebox.showinfo("Echo Chamber", text)
    except sr.UnknownValueError:
        messagebox.showinfo("Echo Chamber", "Sorry, I could not understand the audio. Please try again.")


root = tk.Tk()
root.title("Echo Chamber")
root.geometry("300x120")

button = tk.Button(root, text="Speak Now", command=speak_now)
button.pack(expand=True)

root.mainloop()
