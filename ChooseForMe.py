from tkinter import *
import random
import ctypes

font = "Cambria"

choicesList = []

def choose_random():
    if choicesList:
        frame.place_forget()
        resultFrame.place(x=0, y=100)
        animate_choices(100)

def animate_choices(remaining_elements):
    if remaining_elements > 0:
        previous_choice = ""
        if ":" in resultLbl.cget("text"):
            previous_choice = resultLbl.cget("text").split(": ")[1]
        
        while True:
            selectedChoice = random.choice(choicesList).upper()
            if selectedChoice != previous_choice:
                break
        resultLbl.config(text=selectedChoice)
        root.after(30, animate_choices, remaining_elements - 1)

def store_choice(event):
    choice = entry.get()
    if choice and len(choice) <= 19:
        choicesList.append(choice)
        entry.delete(0, END)
        update_listbox()
    if len(entry.get()) > 19:
        entry.delete(19, END)

def update_listbox():
    listbox.delete(0, END)
    for choice in choicesList:
        listbox.insert(END, choice.upper())

def delete_item(event):
    selectedIndex = listbox.curselection()
    if selectedIndex:
        index = selectedIndex[0]
        listbox.delete(index)
        choicesList.pop(index)
        entry.focus_set()

def clear_listbox(event):
    listbox.delete(0, END)
    choicesList.clear()
    entry.focus_set()

def returnFun():
    resultFrame.place_forget()
    frame.place(x=0, y=100)

def exit_window(*args):
    root.destroy()

root = Tk()
root.title("Choose For Me !")
WIDTH = int(root.winfo_screenwidth() * 0.25)
HEIGHT = int(root.winfo_screenheight() * 0.73)
root.geometry(f"{WIDTH}x{HEIGHT}+{root.winfo_screenwidth()//2 - WIDTH//2}+{root.winfo_screenheight()//2 - HEIGHT//2}")
root.resizable(False, False)
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')
root.iconbitmap(default='res/logo.ico')

titleFrame = Frame(root, width=WIDTH, height=100, bg="#0076ff")
titleFrame.place(x=0, y=0)

title = Label(titleFrame, text="CHOOSE FOR ME !", font=(font, 20, "bold"), bg="#0076ff", fg="white")
title.place(relx=0.5, rely=0.5, anchor=CENTER)

frame = Frame(root, width=WIDTH, height=HEIGHT - 100, bg="#e7e7e7")
frame.place(x=0, y=100)

entry = Entry(frame, width=30, font=(font, 20), justify="center")
entry.place(relx=0.5, rely=0.065, anchor=CENTER)
entry.focus_set()
entry.bind('<Return>', store_choice)

listbox = Listbox(frame, width=30, height=15, font=(font, 20), justify="center", bg="#e7e7e7", borderwidth=0, highlightthickness=0, selectborderwidth=0, selectbackground="blue", exportselection=False, relief="flat")
listbox.place(relx=0.5, rely=0.5, anchor=CENTER)
listbox.bind('<ButtonRelease-1>', delete_item)
listbox.bind('<Button-3>', clear_listbox)

chooseBtn = Button(frame, text="Choose", font=(font, 16), command=choose_random)
chooseBtn.place(relx=0.5, rely=0.91, anchor=CENTER)

resultFrame = Frame(root, width=WIDTH, height=HEIGHT - 100, bg="#e7e7e7")

resultLbl = Label(resultFrame, text="", font=(font, 30), bg="#e7e7e7")
resultLbl.place(relx=0.5, rely=0.45, anchor=CENTER)

returnBtn = Button(resultFrame, text="<", width=2, command=returnFun, font=(font, 20, "bold"))
returnBtn.place(x=10, y=10)

root.bind('<Escape>', exit_window)

root.mainloop()
