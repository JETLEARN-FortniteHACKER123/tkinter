

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


mainWin = Tk()
mainWin.title("Adress book")

#functions
myadressBook = {}

def clearAll():
    name.delete(0, END)
    phone.delete(0, END)
    email.delete(0, END)
    address.delete(0, END)
    birthday.delete(0, END)


def update():
    key = name.get()
    if key == "":
        messagebox.showinfo("Error", "Name field cannot be empty!")
    else:
        if key not in myadressBook.keys():
            book_list.insert(END, key)


        myadressBook[key] = (adress.get(), phone.get(), email.get(), birthday.get()) 

        clearAll()


def edit():
    clearAll()
    index = book_list.curselection()
    if index:
        selected_key = book_list.get(index[0])
        name.insert(0, selected_key)
        details = myadressBook[selected_key]
        adress.insert(0, details[0])
        phone.insert(0, details[1])
        email.insert(0, details[2])
        birthday.insert(0, details[3])
    else:
        messagebox.showinfo("Error", "Please select a contact to edit!")


def delete():
    index = book_list.curselection()
    if index:
        key = book_list.get(index[0])
        del myadressBook[key]
        book_list.delete(index[0])
        clearAll()
    else:
        messagebox.showinfo("Error", "Please select a contact to delete!")








bookName = Label(mainWin, text="My Adress Book", width=35)
bookName.grid(row=0, column=1, columnspan=3,pady=10)

openButton = Button(mainWin, text="Open")
openButton.grid(row=0, column=3,  pady=10)


book_list = Listbox(mainWin, width=30, height=15)
book_list.grid(row=2, column=0, columnspan=3, rowspan=5)


nameLabel = Label(mainWin, text="Name:")
nameLabel.grid(row=2, column=3)
name = Entry(mainWin)
name.grid(row=2, column=4,padx=5)


adressLabel = Label(mainWin, text="Adress: ")
adressLabel.grid(row=3, column=3)
adress = Entry(mainWin)
adress.grid(row=3, column=4,padx=5)

mobileLabel = Label(mainWin, text="Phone: ")
mobileLabel.grid(row=4, column=3)
phone = Entry(mainWin)
phone.grid(row=4, column=4,padx=5)

emailLabel = Label(mainWin, text="Email: ")
emailLabel.grid(row=5, column=3)
email = Entry(mainWin)
email.grid(row=5, column=4,padx=5)

birthdayLabel = Label(mainWin, text="Birthday: ")
birthdayLabel.grid(row=6, column=3)
birthday = Entry(mainWin)
birthday.grid(row=6, column=4,padx=5)


#buttons




#edit contact button
editButton = Button(mainWin, text="Edit",width=10, command=edit)
editButton.grid(row=7, column=0, pady=12 , padx=12)


#delete contact button
deleteButton = Button(mainWin, text="Delete",width=10, command=delete)
deleteButton.grid(row=7, column=4, pady=12 )

# update contact button
addbutton = Button(mainWin, text="Add/Update", command=update)
addbutton.grid(row=7, column=4, pady=12, )

#save button

savebutton = Button(mainWin, text="Save", width= 35)
savebutton.grid(row=8, column=1, columnspan=3, pady=10)
mainWin.mainloop()