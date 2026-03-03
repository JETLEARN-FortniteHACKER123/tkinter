from tkinter import * 
window = Tk()
window.geometry("100x100")


btn = Button(window,text="click me",bd='5',background='#237C82',command=window.destroy)
btn.pack(side="top" )
window.mainloop()
