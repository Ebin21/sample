import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # 1. The Display Screen
        # We use StringVar to update the text inside the entry widget programmatically
        self.equation = tk.StringVar()
        
        self.entry = tk.Entry(
            root, 
            textvariable=self.equation, 
            font=('Arial', 20), 
            bd=10, 
            insertwidth=2, 
            width=14, 
            borderwidth=4,
            justify='right'
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # 2. Button Layout Configuration
        # (Text, Row, Column, Color, Command)
        buttons = [
            ('C', 1, 0, '#ff6b6b', self.clear), 
            ('DEL', 1, 1, '#ff9f43', self.delete_last),
            ('/', 1, 2, '#feca57', lambda: self.append('/')), 
            ('*', 1, 3, '#feca57', lambda: self.append('*')),
            
            ('7', 2, 0, '#ecf0f1', lambda: self.append('7')), 
            ('8', 2, 1, '#ecf0f1', lambda: self.append('8')),
            ('9', 2, 2, '#ecf0f1', lambda: self.append('9')), 
            ('-', 2, 3, '#feca57', lambda: self.append('-')),
            
            ('4', 3, 0, '#ecf0f1', lambda: self.append('4')), 
            ('5', 3, 1, '#ecf0f1', lambda: self.append('5')),
            ('6', 3, 2, '#ecf0f1', lambda: self.append('6')), 
            ('+', 3, 3, '#feca57', lambda: self.append('+')),
            
            ('1', 4, 0, '#ecf0f1', lambda: self.append('1')), 
            ('2', 4, 1, '#ecf0f1', lambda: self.append('2')),
            ('3', 4, 2, '#ecf0f1', lambda: self.append('3')), 
            ('=', 4, 3, '#1dd1a1', self.calculate), # Equals spans 2 rows visually in some designs, keeping simple here
            
            ('0', 5, 0, '#ecf0f1', lambda: self.append('0')), 
            ('.', 5, 1, '#ecf0f1', lambda: self.append('.')),
        ]

        # 3. Create Buttons Loop
        for (text, row, col, color, command) in buttons:
            # If it's the '0' button or '=' button, we might want to adjust sizes, 
            # but for a simple grid, we stick to standard sizes.
            if text == '=':
                 btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), 
                                bg=color, command=command)
                 # Make Equals span two rows? Or just simple grid. Let's keep it simple.
                 btn.grid(row=row, column=col, rowspan=2, sticky="nsew", padx=5, pady=5)
            elif text == '0':
                 btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), 
                                bg=color, command=command)
                 btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
            else:
                btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), 
                                bg=color, command=command)
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Configure grid weights so buttons expand evenly
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)

    # --- Functions ---

    def append(self, value):
        current_text = self.equation.get()
        self.equation.set(current_text + value)

    def clear(self):
        self.equation.set("")

    def delete_last(self):
        current_text = self.equation.get()
        self.equation.set(current_text[:-1])

    def calculate(self):
        try:
            # eval() is a powerful function that parses the string expression
            expression = self.equation.get()
            result = eval(expression) 
            self.equation.set(result)
        except Exception:
            self.equation.set("Error")

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Initialize the application
    app = CalculatorApp(root)
    # Run the main event loop
    root.mainloop()