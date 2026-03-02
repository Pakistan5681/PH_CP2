import turtle as t
import pakistans_functions as pf
from time import sleep
from PIL import ImageGrab
from random import choice
import os
import sys

saveImage = False
recursion = 0
screen = t.Screen()

def start():
    colors = ["red", "green", "yellow", "black", "white", "purple", "blue", "turquoise", "gold", "brown", "r", "orange", "khaki", "orchid", "salmon", "LimeGreen", "OliveDrab", "burlywood3", "bisque", "coral", "DarkGoldenrod", "chartreuse", "lemonchiffon", "honeydew4", "gainsboro"] # I just added all the weirdest color names from the turtle library on top of the standard colors

    print(" ")
    print("Welcome to Pakistans Delightful Fractal Generator!")
    print("This code generates a Serpinski Trangle. ")
    print(f"When choosing a color, enter a common color name or type '{pf.BOLD}{pf.UNDERLINE}r{pf.RESET}' to randomize the color")
    input("Hit enter to continue ")
    print(" ")

    color = pf.idiot_proof_specific("What color would you like to use for the fill? ", colors, "That color is invalid")
    outline = pf.idiot_proof_specific("What color would you like to use for the outline? ", colors, "That color is invalid")
    background = pf.idiot_proof_specific("What color would you like to use for the background? ", colors, "That color is invalid")
    recursion = pf.idiot_proof_num_range("How many levels do you want on the fractal? Max 8 Min 1: ", 1, 8) 
    saveImage = pf.idiot_proof_yes_no("Would you like to save the image? ")

    colors = ["red", "green", "yellow", "black", "white", "purple", "blue", "turquoise", "gold", "brown", "orange", "khaki", "orchid", "salmon", "LimeGreen", "OliveDrab", "burlywood3", "bisque", "coral", "DarkGoldenrod", "chartreuse", "lemonchiffon", "honeydew4", "gainsboro"]
    if color == 'r': color = choice(colors)
    if outline == 'r': outline = choice(colors)
    if background == 'r': background = choice(colors)

    t.tracer(0,0); t.pendown(); t.fillcolor(color); t.teleport(-500, -400); t.hideturtle(); t.bgcolor(background); t.pencolor(outline) # Turtle Setup

    root = screen._root; root.attributes('-topmost', True); root.attributes('-topmost', False) # Automatically opens the turtle screen

    recursion += 1 # Dont worry about this 

    def drawTri(level):
        if level == recursion:
            return recursion

        else:
            increment = 2 ** (level - 1)
            t.begin_fill()
            for y in range(3): # Draws trangle
                for x in range(2): # Draws line in two parts
                    t.forward(500 / increment)
                    if x == 0: drawTri(level + 1)

                t.left(120)
            t.end_fill()

    def end():
        t.update()

        if saveImage:
            canvas = screen.getcanvas(); x = canvas.winfo_rootx(); y = canvas.winfo_rooty(); width = canvas.winfo_width(); height = canvas.winfo_height() # Sets the parameters for capturing the turtle canvas
            sleep(0.5) # A small delay to allow the window to fully open

            if os.path.isdir("docs"): 
                saveString = "docs/fractal_image.png"
                print("Image Saved to docs!")
            else: 
                saveString = "fractal_image.png"
                print("Image Saved!")

            ImageGrab.grab(bbox=(x, y, x + width, y + height)).save(saveString) # Essentially takes a screenshot in the bounds of the turtle window

        t.mainloop()

    drawTri(1)
    end()


    