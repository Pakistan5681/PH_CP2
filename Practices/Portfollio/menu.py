from tkinter import *
from modified_GTC import run_GTC
from dino_game import runFleshCubeII
from roglue import rungame
import threeD as t

def main_loop():
    root = Tk()
    root.title("Portfollio")
    root.configure(background="#010136")
    root.minsize(300, 300)
    root.maxsize(1920, 1080)
    root.geometry("1920x1080+0+0")

    def GTC_start(root):
        for widget in root.winfo_children():
            widget.destroy()

        frame = Frame(root, bg="#010136")
        frame.place(relx=0.5, rely=0.9, anchor="s")

        lbl = Label(frame, text="Get To Canada", font=("Times New Roman", 67, "bold"))
        lbl.config(fg="white", bg="#010136")
        lbl.grid(row=0, column=0, columnspan=2)

        text_widget = Text(frame, height=10, width=40, wrap="word", font=("Times New Roman", 30, "bold"), bd=0, highlightthickness=0, relief="flat")
        text_widget.config(fg="white", bg = "#010136")
        text_widget.grid(row=1, column=0, padx=10, pady=10)

        btn = Button(frame, text="Play", command=lambda:run_GTC(root), width=40, height=10, font=("Times New Roman", 20, "bold"))
        btn.config(fg="white", bg="gray")
        btn.grid(row=2, column=0, padx=10, pady=10)

        paragraph = "Get to Canada is the game I made for my final project first semester. It is the coolest text-based program I've ever made and managed to win the golden duck by a landslide. This game is played in the terminal."
        text_widget.insert("1.0", paragraph)

        mainloop()

    def dino_start(root):
        for widget in root.winfo_children():
            widget.destroy()

        frame = Frame(root, bg="#010136")
        frame.place(relx=0.5, rely=0.9, anchor="s")

        lbl = Label(frame, text="Flesh Cube II", font=("Times New Roman", 67, "bold"))
        lbl.config(fg="white", bg="#010136")
        lbl.grid(row=0, column=0, columnspan=2)

        text_widget = Text(frame, height=10, width=40, wrap="word", font=("Times New Roman", 30, "bold"), bd=0, highlightthickness=0, relief="flat")
        text_widget.config(fg="white", bg = "#010136")
        text_widget.grid(row=1, column=0, padx=10, pady=10)

        btn = Button(frame, text="Play", command=lambda:runFleshCubeII(root), width=40, height=10, font=("Times New Roman", 20, "bold"))
        btn.config(fg="white", bg="gray")
        btn.grid(row=2, column=0, padx=10, pady=10)

        paragraph = "Flesh Cube II is a game I made for the High Score Tracker assignment. It is a direct sequal to the critically acclaimed Flesh Cube, with upgrades like score saving. It is a pygame project."
        text_widget.insert("1.0", paragraph)

        mainloop()

    def rogue_start(root):
        for widget in root.winfo_children():
            widget.destroy()

        frame = Frame(root, bg="#010136")
        frame.place(relx=0.5, rely=0.9, anchor="s")

        lbl = Label(frame, text="Unnamed Roguelike", font=("Times New Roman", 67, "bold"))
        lbl.config(fg="white", bg="#010136")
        lbl.grid(row=0, column=0, columnspan=2)

        text_widget = Text(frame, height=10, width=40, wrap="word", font=("Times New Roman", 30, "bold"), bd=0, highlightthickness=0, relief="flat")
        text_widget.config(fg="white", bg = "#010136")
        text_widget.grid(row=1, column=0, padx=10, pady=10)

        btn = Button(frame, text="Play", command=lambda:rungame(root), width=40, height=10, font=("Times New Roman", 20, "bold"))
        btn.config(fg="white", bg="gray")
        btn.grid(row=2, column=0, padx=10, pady=10)

        paragraph = "This is a little game I made during class, when I likely should've been working on other things. It has a cool upgrade menu, ramping difficulty, and cool UI. It's a pygame project."
        text_widget.insert("1.0", paragraph)

        mainloop()

    def threedee_start(root):
        for widget in root.winfo_children():
            widget.destroy()

        frame = Frame(root, bg="#010136")
        frame.place(relx=0.5, rely=0.9, anchor="s")

        lbl = Label(frame, text="3D Renderer", font=("Times New Roman", 67, "bold"))
        lbl.config(fg="white", bg="#010136")
        lbl.grid(row=0, column=0, columnspan=2)

        text_widget = Text(frame, height=10, width=40, wrap="word", font=("Times New Roman", 30, "bold"), bd=0, highlightthickness=0, relief="flat")
        text_widget.config(fg="white", bg = "#010136")
        text_widget.grid(row=1, column=0, padx=10, pady=10)

        btn = Button(frame, text="Show", command=lambda:t.show_thing(root, t.screen, t.pMatrix), width=40, height=10, font=("Times New Roman", 20, "bold"))
        btn.config(fg="white", bg="gray")
        btn.grid(row=2, column=0, padx=10, pady=10)

        paragraph = "This is a 3D renderer I made during first semester, after watching a video on making a 3D renderer and thinking 'I could do that'. This is a simple demonstration where I draw and rotate the cube, but it could draw any shape given the right parameters. This is a oygame project."
        text_widget.insert("1.0", paragraph)

        mainloop()

    frame = Frame(root, bg="#010136")
    frame.place(relx=0.5, rely=0.95, anchor="s")

    lbl = Label(frame, text="Welcome to Pakistans Madhouse of Madness!", font=("Times New Roman", 67, "bold"))
    lbl.config(fg="white", bg="#010136")
    lbl.grid(row=0, column=0, columnspan=2)

    btn = Button(frame, text="Get to Canada", command=lambda:GTC_start(root), width=40, height=10, font=("Times New Roman", 20, "bold"))
    btn.config(fg="white", bg="gray")
    btn.grid(row=1, column=0, padx=50, pady=50)

    btn2 = Button(frame, text="Dino Game", command=lambda:dino_start(root), width=40, height=10, font=("Times New Roman", 20, "bold"))
    btn2.config(fg="white", bg="gray")
    btn2.grid(row=1, column=1, padx=50, pady=50)

    btn3 = Button(frame, text="Roguelike", command=lambda:rogue_start(root), width=40, height=10, font=("Times New Roman", 20, "bold"))
    btn3.config(fg="white", bg="gray")
    btn3.grid(row=2, column=0, padx=50, pady=50)

    btn4 = Button(frame, text="3D Renderer", command=lambda:threedee_start(root), width=40, height=10, font=("Times New Roman", 20, "bold"))
    btn4.config(fg="white", bg="gray")
    btn4.grid(row=2, column=1, padx=50, pady=50)

    lbl2 = Label(frame, text="Click a button to experience the absolute insanity of the mind of Pakistan! (Along with a lot of self-glaze).", font=("Times New Roman", 30, "bold"))
    lbl2.config(fg="white", bg="#010136")
    lbl2.grid(row=3, column=0, columnspan=2)

    mainloop()

main_loop()

