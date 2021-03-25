import turtle

colors = [
    "DarkOrange",
    "DarkOrange1",
    "DarkOrange2",
    "DarkOrange3",
    "DarkOrange4",
    "chartreuse",
    "chartreuse1",
    "chartreuse2",
    "chartreuse3",
    "chartreuse4",
]

def branch(plr, length=150, dl=0.6, n=7, angle=45, dd=1, offset=0):
    plr.color(colors[n % len(colors)])
    plr.left(angle)
    plr.forward(length * dl)
    if(n > 1):
        branch(plr, length * dl, dl, n - 1, angle * dd, dd, offset)
    else:
        plr.back(length * dl)
    plr.right(angle * 2 + offset)
    plr.forward(length * dl)
    if(n > 1):
        branch(plr, length * dl, dl, n - 1, angle * dd, dd, offset)
    else:
        plr.back(length * dl)
    plr.color(colors[(n + 1) % len(colors)])
    plr.left(angle + offset)
    plr.back(length)

wn = turtle.Screen()
wn.title("Fractal Tree")
wn.bgcolor("black")
wn.screensize(100, 100)
wn.delay(1)

plr = turtle.Turtle()
plr.shape("circle")
plr.color("white")
plr.turtlesize(stretch_wid=0.2, stretch_len=0.2)
plr.speed("fastest")

turtle.degrees()
plr.setheading(90)
branch(plr, n=11, length=300)

wn.mainloop()