import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To-Do List")
root.geometry("400x370")

def add_task():
    task = AddToDo.get()
    if task != "":
        ListBox.insert(tkinter.END, task)
        AddToDo.delete(0, tkinter.END)
        tkinter.messagebox.showinfo(title="Info!", message="task added: "+task)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = ListBox.curselection()[0]
        ListBox.delete(task_index)      
        tkinter.messagebox.showinfo(title="Info!", message="task deleted")
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def update_task():
    task = AddToDo.get()
    try:
        if task!="":
            task_index = ListBox.curselection()[0]
            ListBox.delete(task_index)
            ListBox.insert(tkinter.END,task)
            AddToDo.delete(0, tkinter.END)
            tkinter.messagebox.showinfo(title="Info!", message="task updated")
        else:
            tkinter.messagebox.showwarning(title="Warning!", message="You must enter updated task")
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


# Create GUI
FrameTasks = tkinter.Frame(root)
FrameTasks.pack()

ListBoxLabel = tkinter.Label(FrameTasks, font="Courier 20 bold", text="Your Todos: ")
ListBoxLabel.pack()

ListBox = tkinter.Listbox(FrameTasks, height=10, width=50)
ListBox.pack(side=tkinter.LEFT)

ScrollBar = tkinter.Scrollbar(FrameTasks)
ScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

ListBox.config(yscrollcommand=ScrollBar.set)
ScrollBar.config(command=ListBox.yview)


AddLabel = tkinter.Label(root, font="Courier 10 bold", text="Add Todo here: ")
AddLabel.pack()

AddToDo = tkinter.Entry(root, width=50)
AddToDo.pack(pady=7)


AddTaskBtn = tkinter.Button(root, text="Add task", width=12,  command=add_task)
AddTaskBtn.pack(pady=3)

DeleteTaskBtn = tkinter.Button(root, text="Delete task", width=12, command=delete_task)
DeleteTaskBtn.pack(pady=3)

UpdateTaskBtn = tkinter.Button(root, text="Update task", width=12, command=update_task)
UpdateTaskBtn.pack(pady=3)


root.mainloop()
