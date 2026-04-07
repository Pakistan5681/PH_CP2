from tkinter import *

root = Tk()
root.title("Portfollio")
root.configure(background="#010136")
root.minsize(300, 300)
root.maxsize(1920, 1080)
root.geometry("1920x1080+0+0")

def GTC_start():
    for widget in root.winfo_children():
        widget.destroy()

    frame = Frame(root, bg="#010136")
    frame.place(relx=0.5, rely=0.6, anchor="s")

    lbl = Label(frame, text="Get To Canada", font=("Times New Roman", 67, "bold"))
    lbl.config(fg="white", bg="#010136")
    lbl.grid(row=0, column=0, columnspan=2)
                        
    text_widget = Text(frame, height=10, width=40, wrap="word", font=("Times New Roman", 30, "bold"), bd=0, highlightthickness=0, relief="flat")
    text_widget.config(fg="white", bg = "#010136")
    text_widget.grid(row=1, column=0, padx=10, pady=10)

    paragraph = "Get to Canada is the game I made for my final project first semester. It is the coolest text-based program I've ever made and managed to win the golden duck by a landslide."
    text_widget.insert("1.0", paragraph)

    mainloop()

frame = Frame(root, bg="#010136")
frame.place(relx=0.5, rely=0.95, anchor="s")

lbl = Label(frame, text="Welcome to Pakistans Madhouse of Madness!", font=("Times New Roman", 67, "bold"))
lbl.config(fg="white", bg="#010136")
lbl.grid(row=0, column=0, columnspan=2)

btn = Button(frame, text="Get to Canada", command=GTC_start, width=40, height=10, font=("Times New Roman", 20, "bold"))
btn.config(fg="white", bg="gray")
btn.grid(row=1, column=0, padx=50, pady=50)

btn2 = Button(frame, text="Dino Game", width=40, height=10, font=("Times New Roman", 20, "bold"))
btn2.config(fg="white", bg="gray")
btn2.grid(row=1, column=1, padx=50, pady=50)

btn3 = Button(frame, text="Roguelike", width=40, height=10, font=("Times New Roman", 20, "bold"))
btn3.config(fg="white", bg="gray")
btn3.grid(row=2, column=0, padx=50, pady=50)

btn4 = Button(frame, text="3D Renderer", width=40, height=10, font=("Times New Roman", 20, "bold"))
btn4.config(fg="white", bg="gray")
btn4.grid(row=2, column=1, padx=50, pady=50)

lbl2 = Label(frame, text="Click a button to experience the absolute insanity of the mind of Pakistan! (Along with a lot of self-glaze).", font=("Times New Roman", 30, "bold"))
lbl2.config(fg="white", bg="#010136")
lbl2.grid(row=3, column=0, columnspan=2)

mainloop()



