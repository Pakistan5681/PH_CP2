import turtle as t
import pakistans_functions as pf

colors = ["red", "green", "yellow", "black", "white", "purple", "blue", "turquoise", "gold", "brown"]

color = pf.idiot_proof_specific("What color would you like to use? ", colors, "That color is invalid")
recursion = pf.idiot_proof_num_range("How many levels do you want on the fractal? Max 5 Min 2: ", 1, 5)

t.tracer(0, 0)
t.speed(1000)
t.pendown()
t.fillcolor(color)
t.teleport(-500, -400)

recursion += 1

def draw(level):
    if level == recursion:
        return recursion
    else:
        increment = 2 ** (level - 1)
        t.begin_fill()
        for y in range(3):
            for x in range(2): 
                t.forward(500 / increment)
                if x == 0: draw(level + 1)

            t.left(120)
        t.end_fill()

draw(1)
t.update()
t.mainloop()