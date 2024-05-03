import tkinter as tk
from tkinter import messagebox


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display input and result
        self.entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 14), bd=10, insertwidth=4,
                              width=20, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons for numeric input and operations
        buttons = [
            ('C', 1, 0),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
        ]

        for (text, row, col) in buttons:
            tk.Button(self.root, text=text, font=("Arial", 14), command=lambda t=text: self.on_button_click(t)).grid(
                row=row, column=col, sticky='nsew')

    def on_button_click(self, char):
        current_text = self.result_var.get()

        # Clear entry if an error message is displayed
        if "Error" in current_text:
            self.result_var.set("")
            current_text = ""

        if char == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif char == 'C':
            self.clear()
        else:
            self.result_var.set(current_text + char)

    def clear(self):
        self.result_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
