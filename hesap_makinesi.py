import tkinter as tk

# Function to handle button click
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Creating main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying numbers
entry = tk.Entry(root, font="Arial 20", justify="right", bd=10, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Creating buttons
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        btn = tk.Button(root, text=char, font="Arial 20", padx=20, pady=20)
        btn.grid(row=r+1, column=c, sticky="nsew")
        btn.bind("<Button-1>", on_click)

# Run the application
root.mainloop()
