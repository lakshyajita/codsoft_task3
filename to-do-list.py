# A simple GUI To-Do List using Python's Tkinter library

from tkinter import *

def add():
      taskBox.insert(taskBox.size(),entryTask.get())
      entryTask.delete(0, END)

def delete():
      taskBox.delete(taskBox.curselection())

def markComplete():
      selected = taskBox.curselection()
      taskText = taskBox.get(selected)
      taskBox.delete(selected)
      taskBox.insert(END, taskText)
      taskBox.itemconfig(END, fg = 'grey')

window = Tk()
window.title("To-Do List")
window.geometry("420x420")
window.config(bg  = "#e6ecfa")


mainFrame = Frame(window, bg = "#a3c9f0", relief = SOLID, bd = 3, width = 350, height = 400)
mainFrame.pack(padx = 10, pady = 10)
mainFrame.pack_propagate(False)

Label(mainFrame,
      text = "My To-Do List",
      font = ('Constantia', 20, 'bold'),
      bg = "#a3c9f0",
      fg = "#140693",
      justify = CENTER).pack(pady = 10)

entryFrame = Frame(mainFrame, bg = '#a3c9f0')
entryFrame.pack()

entryTask = Entry(entryFrame, width = 25, relief = SUNKEN, bd = 2)
entryTask.grid(row = 0, column = 0, padx = 10)

addButton = Button(entryFrame,
                   text = 'Add',
                   font = ('Arial', 10, 'bold'),
                   bg = 'green',
                   fg = 'white',
                   activebackground = 'green',
                   activeforeground = 'white',
                   command = add)
addButton.grid(row = 0, column = 1, padx = 10)

taskboxFrame = Frame(mainFrame, bg = '#a3c9f0')
taskboxFrame.pack()

scrollbar = Scrollbar(taskboxFrame)
scrollbar.pack(side = RIGHT, fill = Y, pady = 15)

taskBox = Listbox(taskboxFrame,
                  font = ('Arial, 10'),
                  width = 30,
                  height = 10,
                  yscrollcommand = scrollbar.set,
                  selectbackground = "grey")
taskBox.pack(side = LEFT, pady = 15)
scrollbar.config(command=taskBox.yview)

buttonFrame = Frame(mainFrame, bg = '#a3c9f0')
buttonFrame.pack()

deleteButton = Button(buttonFrame,
                      text = 'Delete',
                      font = ('Arial', 10,'bold'),
                      bg = 'red',
                      fg = 'white',
                      width = 10,
                      relief = RAISED,
                      bd = 3,
                      activebackground = 'red',
                      activeforeground = 'white',
                      command = delete)
deleteButton.pack(padx = 10, pady = 10, side = RIGHT)

completedBtn = Button(buttonFrame,
                      text = 'Mark as completed',
                      font = ('Arial', 10, 'bold'),
                      bg = "#2585e6",
                      fg = 'white',
                      width = 17,
                      relief = RAISED,
                      bd = 3,
                      activebackground = '#2585e6',
                      activeforeground = 'white',
                      command = markComplete)
completedBtn.pack(padx = 10, pady = 10, side = LEFT)

window.mainloop()
