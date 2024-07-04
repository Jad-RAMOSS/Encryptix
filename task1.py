#Jad ElWahy
#Encyptix Task1
#ToDoApp

import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x700")

        #changing the icon
        self.root.iconbitmap('icon.ico')
        
        self.tasks = []
 
        self.title_label = tk.Label(root, text="To-Do List", font=("Brush Script MT", 20))
        self.title_label.pack(pady=10)

        self.task_text = tk.Text(root, height=2, width=20,wrap='word')
        self.task_text.pack(pady=10)
        self.task_text.bind("<KeyRelease>", self.on_text_change)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=25, height=10)
        self.task_listbox.pack(pady=10)

    def on_text_change(self, event):
        widget = event.widget
        num_lines = int(widget.index('end-1c').split('.')[0])
        widget.configure(height = num_lines if num_lines > 2 else 2)
        widget.edit_modified(False)

    def add_task(self):
        task = self.task_text.get("1.0",tk.END).strip()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_text.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            updated_task = self.task_text.get("1.0",tk.END).strip()
            if updated_task:
                self.tasks[selected_task_index] = updated_task
                self.update_task_listbox()
                self.task_text.delete("1.0", tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
