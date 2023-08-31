import tkinter as tk
from tkinter import messagebox
from tkinter import *

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x650+400+10")  # Set the window size and position
        self.root.resizable(False,False)
        
        # Icon
        image_icon = tk.PhotoImage(file="Image/task.png")
        self.root.iconphoto(False, image_icon)
        
        # Top bar
        top_image = tk.PhotoImage(file="Image/topbar.png")
        tk.Label(self.root, image=top_image).pack()
        
        # Dock
        dock_image = tk.PhotoImage(file="Image/dock.png")
        tk.Label(self.root, image=dock_image, bg="#32405b").place(x=30, y=25)
        
        # Note Image
        note_image = tk.PhotoImage(file="Image/task.png")
        tk.Label(self.root, image=note_image, bg="#32405b").place(x=340, y=25)
        
        # Heading
        heading = tk.Label(self.root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
        heading.place(x=130, y=20)
        
        self.entry = tk.Entry(self.root, font=('Helvetica', 16))
        self.entry.pack(fill=tk.BOTH, expand=True)
        
        self.add_button = tk.Button(self.root, text="Add Task", bg="#44c767", fg="white", font=('Helvetica', 12, 'bold'), command=self.add_task)
        self.add_button.pack(fill=tk.BOTH, expand=True)
        
        self.task_listbox = tk.Listbox(self.root, font=('Helvetica', 16), selectmode=tk.SINGLE, height=10)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)
        
        self.delete_button = tk.Button(self.root, text="Delete Task", bg="#d9534f", fg="white", font=('Helvetica', 12, 'bold'), command=self.delete_task)
        self.delete_button.pack(fill=tk.BOTH, expand=True)

        self.update_button = tk.Button(self.root, text="Update Task", bg="#f0ad4e", fg="white", font=('Helvetica', 12, 'bold'), command=self.update_task)
        self.update_button.pack(fill=tk.BOTH, expand=True)
        
        self.tasks = []  # Initialize tasks
        
        self.load_tasks()  # Load tasks from file
        
        self.save_tasks()  # Save tasks to file
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
    
    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
            self.save_tasks()
    
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
            self.save_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            updated_task = self.entry.get()
            if updated_task:
                self.tasks[index] = updated_task
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, updated_task)
                self.entry.delete(0, tk.END)
                self.save_tasks()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    app.run()
