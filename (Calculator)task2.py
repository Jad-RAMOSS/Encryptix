import math as mt
import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Calculator Application")
        self.root.geometry("300x400")
        
        #changing the icon
        self.root.iconbitmap('icon.ico')
        
        self.title_label = tk.Label(root, text="Calculator", font=("Berlin Sans FB", 20))
        self.title_label.grid(row=0,column=0,columnspan=4,pady=10)
        
        self.task_text = tk.Text(root, height=1, width=30,wrap='word')
        self.task_text.grid(row=1,column=0,columnspan=4,pady=10)
        self.task_text.bind("<KeyRelease>", self.on_text_change)
        
        
        buttons =[
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3),
            ('0', 7, 0), ('.', 7, 1), ('=', 7, 2), ('+', 7, 3)
        ]
        # Create and place buttons
        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(root, text=text, width=5, height=2, command=self.evaluate)
            else:
                btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

        # Create and place clear button
        clear_btn = tk.Button(root, text='C', width=5, height=2, command=self.clear)
        clear_btn.grid(row=4, column=4, padx=5, pady=5)
        
    def button_click(self,value):
        current_text = self.task_text.get("1.0",tk.END).strip()
        self.task_text.delete("1.0",tk.END)
        self.task_text.insert(tk.END, current_text + str(value))

    def evaluate(self):
        try:
            result = eval(self.task_text.get("1.0",tk.END).strip())
            self.task_text.delete("1.0",tk.END)
            self.task_text.insert(tk.END,str(result))
        except:
            self.task_text.delete("1.0",tk.END)
            self.task_text.insert(tk.END,"Syntax Eror!")
    def clear(self):
        self.task_text.delete("1.0",tk.END)
                
    def on_text_change(event):
        widget = event.widget
        num_lines = int(widget.index('end-1c').split('.')[0])
        widget.configure(height = num_lines if num_lines > 2 else 2)
        widget.edit_modified(False)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
