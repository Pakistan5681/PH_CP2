import turtle as t
import pakistans_functions as pf
from time import sleep
from PIL import ImageGrab
from random import choice

# !!! The image saves to the 'Docs' file !!!

colors = ["red", "green", "yellow", "black", "white", "purple", "blue", "turquoise", "gold", "brown", "r", "orange", "khaki", "orchid", "salmon", "LimeGreen", "OliveDrab"]

print(" ")
print("Welcome to Pakistans Delightful Fractal Generator!")
print("This code generates a Serpinski Trangle. ")
print("When choosing a color, enter a common color name or type 'r' to randomize the color")
input("Hit enter to continue ")
print(" ")

color = pf.idiot_proof_specific("What color would you like to use for the fill? ", colors, "That color is invalid")
outline = pf.idiot_proof_specific("What color would you like to use for the outline? ", colors, "That color is invalid")
background = pf.idiot_proof_specific("What color would you like to use for the background? ", colors, "That color is invalid")
recursion = pf.idiot_proof_num_range("How many levels do you want on the fractal? Max 8 Min 1: ", 1, 8) 
saveImage = pf.idiot_proof_yes_no("Would you like to save the image? ")

colors = ["red", "green", "yellow", "black", "white", "purple", "blue", "turquoise", "gold", "brown", "orange"]
if color == 'r': color = choice(colors)
if outline == 'r': outline = choice(colors)
if background == 'r': background = choice(colors)

t.tracer(0,0); t.pendown(); t.fillcolor(color); t.teleport(-500, -400); t.hideturtle(); t.bgcolor(background); t.pencolor(outline) # Turtle Setup

screen = t.Screen()

root = screen._root; root.attributes('-topmost', True); root.attributes('-topmost', False) # Automatically opens the turtle screen

recursion += 1

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

        
drawTri(1)
t.update()

if saveImage:
    canvas = screen.getcanvas(); x = canvas.winfo_rootx(); y = canvas.winfo_rooty(); width = canvas.winfo_width(); height = canvas.winfo_height() # Sets the parameters for capturing the turtle canvas
    sleep(0.5)
    ImageGrab.grab(bbox=(x, y, x + width, y + height)).save("Docs/fractal_image.png")
    print("Image Saved to Docs!")

t.mainloop()
