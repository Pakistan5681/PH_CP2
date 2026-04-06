import tkinter as tk
from random import randint

root = tk.Tk()
root.title("Button Clicker")
root.configure(background="#010136")
root.minsize(300, 300)
root.maxsize(1920, 1080)
root.geometry("1920x1080+0+0")

root.count = 0
root.amount = 1
root.size = 13
def add():
    root.count += root.amount
    lbl["text"] = root.count

lbl = tk.Label(root, text="0", font=("Times New Roman", 67, "bold"))
lbl.config(fg="white", bg="#010136")
lbl.grid(row=960, column=100)

btn = tk.Button(root, text="CLICK ME", command=add, width=20, height=20, font=("Times New Roman", 10, "bold"))
btn.config(fg="white", bg="gray")
btn.grid(row=100, column=540)

root.mainloop()