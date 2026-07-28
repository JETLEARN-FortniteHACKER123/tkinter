import tkinter
from tkinter import *
import random
from tkinter import messagebox

root = tkinter.Tk()


answers = ["apple", 'mango', 'banana', 'achieve','kolkata', 'evening', 'servant', 'reciever', 'london', 'ferrari', 'hollow', 'horror', 'master', 'morning', 'bottle', 'pen', 'router', 'copy', 'narrow', 'wide','dive' , 'love', 'block','right','simple', 'deaf','single', 'knight', 'hope']
words = ['plpea', 'gnoma', 'nnaaba', 'ehaevci', 'kloakta', 'gineevn', 'vtsraen', 'ecrveier', 'odnlon', 'rfrarei', 'hllowo', 'rohor', 'rtemsa', 'gniomrn', 'tleobt', 'nep', 'rteoru', 'ocpy', 'wraonr', 'deiw','dvei' , 'eolv', 'bclok','ghtrit','esilmp', 'afed','lgsnie', 'kthgni', 'peho']
num = random.randrange(0, len(words), 1 )
c=0
d=0
s=''
e1=Label(root)

def reset():
    global words, answers , num
    num = random.randrange(0, len(words), 1 )
    label.config(text=words[num])
    e1.delete(0, END)


def default():
    global words, answers, num
    label.config(text=words[num])


def checkans():
    global words ,  answers, num , c, d, s , l
    d = int(d)+1
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        c=int(c)+1
    else:
        messagebox.showerror("Error", "This is not a correct answer")
        s = "Score: " + str(c) + "/" + str(d)
        l.forget()
        l= Label(root, text=s, font=("Verdana", 20), bg="#000000", fg="#fff")
        l.pack(side=LEFT)
        reset()

root.geometry("500x500+500+150")    
root.title("Jumbled Dictionary game")  
root.configure(bg="#000000")

Label(root, text="JUMBLED DICTIONARY GAME", font=("Verdana", 28), bg="#000000", fg="#fff").pack(pady=5)
label = Label(root, font=("Verdana", 22), bg="#000000", fg="#fff")
label.pack(pady=30, ipady=10, ipadx=10)


ans = StringVar()
e1 = Entry(root, textvariable=ans, font=("Verdana", 20))
e1.pack(ipady=5, ipadx=5)
Button(root, text = "Check", font=("Cosmic sans ms", 20), width=10, bg="#333945", fg="#45CE50", relief="groove", command=checkans).pack(pady=40)
Button(root, text = "Reset", font=("Cosmic sans ms", 20), width=10, bg="#777E8B", fg="#E1DA00", relief="groove", command=reset).pack()

default()

root.mainloop()      

