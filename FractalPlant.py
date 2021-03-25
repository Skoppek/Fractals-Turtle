import turtle

str = 'X'
queue = []

def evolve(str):
    new_str = ''
    for ch in str:
        if(ch == 'X'):
            new_str += 'F+[[X]-X]-F[-FX]+X'
        elif(ch == 'F'):
            new_str += 'FF'
        elif(ch == '['):
            new_str += '['
        elif(ch == ']'):
            new_str += ']'
        elif(ch == '-'):
            new_str += '-'
        elif(ch == '+'):
            new_str += '+'

    return new_str

for n in range(5):
    str = evolve(str)

wn = turtle.Screen()
wn.bgcolor("black")

mrk = turtle.Turtle()
mrk.color("green")
mrk.shape("circle")
mrk.turtlesize(stretch_wid=0.2, stretch_len=0.2)
mrk.degrees()
mrk.speed("fastest")
mrk.penup()
mrk.setpos(-300, -300)
mrk.pendown()
mrk.seth(45)

for ch in str:
    if(ch == 'F'):
        mrk.forward(6)
    elif(ch == '-'):
        mrk.right(20)
    elif(ch == '+'):
        mrk.left(20)
    elif(ch == '['):
        queue.append([mrk.pos(), mrk.heading()])
    elif(ch == ']'):
        data = queue.pop()
        mrk.penup()
        mrk.setpos(data[0])
        mrk.seth(data[1])
        mrk.pendown()

wn.mainloop()